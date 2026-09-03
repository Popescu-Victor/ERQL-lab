$csvPath = Read-Host -Prompt "Enter path to CSV file (Tab to autocomplete)"
$csvPath = $csvPath -replace '"', '' # When using 'copy as path' in Windows Explorer, the path is wrapped in double quotes. Remove them.

$data = Import-Csv -Path $csvPath

$thirdColumnName = ($data | Get-Member -MemberType NoteProperty)[2].Name

$data | Select-Object -ExpandProperty $thirdColumnName -Unique | ForEach-Object {
    Write-Output $_
}