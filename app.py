import cv2
import ctypes
import time
import threading
import os
import pygame
from PIL import Image

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

class VideoWallpaper:
    def __init__(self, video_path, audio_path):
        self.video_path = video_path
        self.audio_path = audio_path
        self.running = True
        self.temp_frame = "temp_frame.jpg"
        self.current_frame = None
        
        # Initialize video
        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            raise Exception(f"Could not open video: {video_path}")
            
        # Get video properties
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_time = 1 / self.fps
        print(f"Video FPS: {self.fps}")
            
        # Initialize audio
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        
    def update_wallpaper(self):
        """Thread function to update wallpaper every second"""
        while self.running:
            if self.current_frame is not None:
                # Save current frame and set as wallpaper
                cv2.imwrite(self.temp_frame, self.current_frame)
                set_wallpaper(os.path.abspath(self.temp_frame))
            time.sleep(0.1)  # Update every second
            
    def play_video(self):
        """Thread function to play video at correct speed"""
        last_frame_time = time.time()
        
        while self.running:
            current_time = time.time()
            elapsed = current_time - last_frame_time
            
            if elapsed >= self.frame_time:
                ret, frame = self.cap.read()
                if not ret:
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    last_frame_time = current_time
                    continue
                    
                self.current_frame = frame
                cv2.imshow('Video', frame)
                last_frame_time = current_time
                
                if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
                    self.running = False
                    break
            else:
                # Small sleep to prevent CPU overuse
                time.sleep(max(0, self.frame_time - elapsed))
                
    def play(self):
        # Start audio
        pygame.mixer.music.play(-1)  # -1 for infinite loop
        
        # Start wallpaper update thread
        wallpaper_thread = threading.Thread(target=self.update_wallpaper)
        wallpaper_thread.daemon = True
        wallpaper_thread.start()
        
        # Play video in main thread
        try:
            self.play_video()
        except KeyboardInterrupt:
            pass
        finally:
            self.stop()
            
    def stop(self):
        self.running = False
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        self.cap.release()
        cv2.destroyAllWindows()
        
        # Clean up temp file
        try:
            os.remove(self.temp_frame)
        except:
            pass

if __name__ == "__main__":
    video_path = "everything.mp4"
    audio_path = "audio.mp3"
    
    print("Starting video wallpaper...")
    print("Press ESC to stop")
    
    try:
        wallpaper = VideoWallpaper(video_path, audio_path)
        wallpaper.play()
    except Exception as e:
        print(f"Error: {e}")