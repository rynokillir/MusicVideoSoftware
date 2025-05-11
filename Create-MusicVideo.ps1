# Create-MusicVideo.ps1 - Combines image, audio, and metadata to create a video.

# Get the metadata for the song
function Get-Metadata {
    $metadataFile = ".\Metadata\$(Read-Host 'Enter song title')"
    if (Test-Path $metadataFile) {
        $metadata = Get-Content $metadataFile | ConvertFrom-StringData
    } else {
        Write-Host "Metadata file not found."
        exit
    }
    return $metadata
}

# Ensure FFmpeg is available
$ffmpegPath = ".\ffmpeg\ffmpeg.exe"
if (-not (Test-Path $ffmpegPath)) {
    Write-Host "FFmpeg not found. Please initialize the project first."
    exit
}

# Get metadata and inputs
$metadata = Get-Metadata
$imagePath = ".\Image\$(Read-Host 'Enter image file name')"
$audioPath = ".\Song-File\$(Read-Host 'Enter audio file name')"

# Check for file existence
if (!(Test-Path $imagePath) -or !(Test-Path $audioPath)) {
    Write-Host "Required files not found."
    exit
}

# Create video using FFmpeg
$outputPath = ".\Videos\$($metadata["title"]).mp4"
$ffmpegArgs = "-loop 1 -framerate 2 -t 30 -i $imagePath -i $audioPath -c:v libx264 -preset fast -c:a aac -b:a 192k -metadata title='$($metadata["title"])' -metadata artist='$($metadata["artist"])' -metadata album='$($metadata["album"])' -metadata genre='$($metadata["genre"])' -metadata year='$($metadata["year"])' $outputPath"

# Run FFmpeg to create the video
& $ffmpegPath $ffmpegArgs

Write-Host "Video created: $outputPath"
