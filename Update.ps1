# Update.ps1 - Checks for missing folders and updates FFmpeg if needed.

# Ensure necessary folders exist
function Ensure-Folder($name) {
    $path = ".\$name"
    if (!(Test-Path $path)) {
        New-Item -ItemType Directory -Path $path
        Write-Host "Created missing folder: $name"
    }
}

Ensure-Folder "Image"
Ensure-Folder "Song-File"
Ensure-Folder "Metadata"

# Check for FFmpeg updates
$ffmpegPath = ".\ffmpeg\ffmpeg.exe"
if (!(Test-Path $ffmpegPath)) {
    Write-Host "FFmpeg not found. Downloading..."
    .\Initialize.ps1
} else {
    Write-Host "FFmpeg is up-to-date."
}

Write-Host "Update complete."
