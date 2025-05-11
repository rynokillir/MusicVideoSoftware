# Initialize.ps1 - Initializes the folder structure, downloads FFmpeg if missing.

function Ensure-Folder($name) {
    $path = ".\$name"
    if (!(Test-Path $path)) {
        New-Item -ItemType Directory -Path $path
        Write-Host "Created folder: $name"
    }
}

# Create necessary folders
Ensure-Folder "Image"
Ensure-Folder "Song-File"
Ensure-Folder "Metadata"
Ensure-Folder "Archive"
Ensure-Folder "Videos"

# Download and Install FFmpeg
$ffmpegPath = ".\ffmpeg\ffmpeg.exe"
if (-not (Test-Path $ffmpegPath)) {
    Write-Host "Downloading FFmpeg..."
    Invoke-WebRequest -Uri "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip" -OutFile "ffmpeg.zip"
    Expand-Archive -Path "ffmpeg.zip" -DestinationPath ".\ffmpeg"
    Remove-Item "ffmpeg.zip"
    Write-Host "FFmpeg installed."
}

Write-Host "Initialization complete. Ready to use MusicVideoSoftware!"
