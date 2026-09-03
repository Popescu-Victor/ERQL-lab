Add-Type -AssemblyName System.Windows.Forms

function Show-Menu {
    param([string[]]$Options)
    $selected = 0
    $keyInfo = $null

    while ($keyInfo.VirtualKeyCode -ne 13) { # 13 = Enter
        Clear-Host
        Write-Host "Use arrow keys to select a column, then press Enter:`n"
        for ($i = 0; $i -lt $Options.Count; $i++) {
            if ($i -eq $selected) {
                Write-Host "> $($Options[$i])" -ForegroundColor Cyan
            } else {
                Write-Host "  $($Options[$i])"
            }
        }
        $keyInfo = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
        if ($keyInfo.VirtualKeyCode -eq 38 -and $selected -gt 0) { $selected-- }         # Up
        if ($keyInfo.VirtualKeyCode -eq 40 -and $selected -lt $Options.Count - 1) { $selected++ } # Down
    }
    return $Options[$selected]
}

$dialog = New-Object System.Windows.Forms.OpenFileDialog
$dialog.Filter = "CSV files (*.csv)|*.csv|All files (*.*)|*.*"
$dialog.Title = "Select a CSV file"

if ($dialog.ShowDialog() -eq "OK") {
    $csvPath = $dialog.FileName
    Write-Output "You selected: $csvPath"
} else {
    Write-Output "No file selected."
    exit
}

$continue = Read-Host "Do you want to process the CSV file? (Y/N)"
if ($continue -ne "Y") {
    Write-Output "Exiting script."
    exit
} else {
    $process_time = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
    $outFile = "$PSScriptRoot\Rendered File at $process_time.txt"
    New-Item -Path $outFile -ItemType File -Force | Out-Null

    Write-Output "Processing CSV file..."
    $data = Import-Csv -Path $csvPath

    $columnNames = ($data | Get-Member -MemberType NoteProperty).Name
    $target_column = Show-Menu -Options $columnNames

    Clear-Host
    Write-Output "Extracting column: $target_column"

    foreach ($row in $data) {
        $row.$target_column | Out-File -Append -FilePath $outFile
    }

    Write-Output "Done. Output written to: $outFile"
}