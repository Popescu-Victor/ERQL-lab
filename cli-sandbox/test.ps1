Add-Type -AssemblyName System.Windows.Forms

$dialog = New-Object System.Windows.Forms.OpenFileDialog
$dialog.Filter = "CSV files (*.csv)|*.csv|All files (*.*)|*.*"
$dialog.Title = "Select a CSV file"

if ($dialog.ShowDialog() -eq "OK") {
    $csvPath = $dialog.FileName
    Write-Output "You selected: $csvPath"
} else {
    Write-Output "No file selected."
}


$continue = Read-Host "Do you want to process the CSV file? (Y/N)"
if ($continue -ne "Y") {
    Write-Output "Exiting script."
    exit
} else {
    $process_time = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
    New-Item -Path "$PSScriptRoot\Rendered File at $process_time.txt" -ItemType File -Force
    Write-Output "Processing CSV file..."
    $data = Import-Csv -Path $csvPath
    ($data | Get-Member -MemberType NoteProperty).Name
    $target_column = Read-Host "Enter the name of the column to extract"
    foreach ($row in $data) {
        Write-Output $row.$target_column | Out-File -Append -FilePath "$PSScriptRoot\Rendered File at $process_time.txt"
    }

}