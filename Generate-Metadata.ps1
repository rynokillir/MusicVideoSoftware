# Generate-Metadata.ps1 - Walks the user through metadata creation.

function Get-Metadata {
    $metadata = @{}
    $metadata["title"] = Read-Host "Enter the title of the song"
    $metadata["artist"] = Read-Host "Enter the artist's name"
    $metadata["album"] = Read-Host "Enter the album name (optional)"
    $metadata["genre"] = Read-Host "Enter the genre (optional)"
    $metadata["year"] = Read-Host "Enter the release year (optional)"

    return $metadata
}

$metadata = Get-Metadata

# Save metadata as a .txt file in the Metadata folder
$metadataFile = ".\Metadata\$($metadata["title"]).txt"
$metadata | ForEach-Object { Add-Content -Path $metadataFile -Value "$($_.Key)=$($_.Value)" }

Write-Host "Metadata saved to: $metadataFile"
