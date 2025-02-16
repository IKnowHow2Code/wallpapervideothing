# Video Wallpaper Script

A Python script that plays a video as your Windows desktop wallpaper. The script displays the video in a window while simultaneously updating your desktop wallpaper at regular intervals.
-ADDING EXE SOON
## Features

- Plays video in a window while updating desktop wallpaper
- Supports separate audio file playback (MP3)
- Video continues playing in a loop
- Press ESC to stop playback

## Limitations

- Low frame rate for wallpaper updates due to limitations. (1 update per second)
- Videos with non-standard aspect ratios may appear zoomed or stretched
- Small delay between video playback and wallpaper updates
- Video window must remain visible for script to work
- Audio and video may become slightly out of sync over time
- **Significant lag develops with longer videos** - the wallpaper will fall further and further behind the actual video playback over time

## Requirements

```bash
pip install opencv-python pillow pygame pywin32
```

## Usage

1. Place your video file (e.g., `everything.mp4`) in the same directory as the script
2. Place your audio file (e.g., `audio.mp3`) in the same directory
3. Run the script:
```bash
python app.py
```

## How It Works

The script works by:
1. Playing the video in a regular window at normal speed
2. Taking a screenshot of the current frame every second
3. Setting that screenshot as the desktop wallpaper
4. Playing the audio file on loop separately

## File Structure

Required files in the same directory:
- `app.py` (the script)
- `everything.mp4` (your video file)
- `audio.mp3` (your audio file)

## Known Issues

1. Aspect Ratio: Videos that don't match your desktop's aspect ratio will appear zoomed or stretched in the wallpaper
2. Performance: The wallpaper updates at 1 FPS regardless of the video's original frame rate
3. Synchronization: The wallpaper will always lag behind the actual video playback
4. Desynchronization: The lag between video and wallpaper gets worse over time with longer videos
5. Window Required: The video window must stay open for the script to work
## Troubleshooting

If you encounter issues:
1. Make sure both video and audio files are in the correct location
2. Try running the script as administrator
3. Check if your video file can be played by other media players
4. Ensure you have all required Python packages installed
5. For longer videos, you may need to restart the script periodically to reset the synchronization
