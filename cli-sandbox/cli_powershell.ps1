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


$data = Import-Csv -Path $csvPath

$thirdColumnName = ($data | Get-Member -MemberType NoteProperty)[2].Name

$data | Select-Object -ExpandProperty $thirdColumnName -Unique | ForEach-Object {
    Write-Output $_
}

