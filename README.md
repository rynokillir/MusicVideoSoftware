# Music Video Software

This project automates the creation of music videos by combining audio, images, and metadata.

## Setup

1. **Initialize the project**:
    - Run `Initialize.ps1` to set up the required folder structure and download FFmpeg.
    - Folders created: `Image/`, `Song-File/`, `Metadata/`, `Archive/`, `Videos/`

2. **Create metadata**:
    - Run `Generate-Metadata.ps1` to create metadata for your song.

3. **Create the video**:
    - Place the song image and audio in the `Image/` and `Song-File/` folders, respectively.
    - Run `Create-MusicVideo.ps1` to generate the music video.

## Folder Structure

- `Image/` - Store your song’s cover art.
- `Song-File/` - Store your audio files (.wav or .mp3).
- `Metadata/` - Store song metadata in `.txt` files.
- `Archive/` - Stores used files once processed.
- `Videos/` - Store generated music videos.

## Requirements

- PowerShell 5+ (Windows).
- FFmpeg (automatically installed via `Initialize.ps1`).

## Troubleshooting

- Ensure the folder names and metadata format are correct.
