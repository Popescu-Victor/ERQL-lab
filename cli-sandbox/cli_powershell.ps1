$csvPath = Read-Host -Prompt "Enter path to CSV file (Tab to autocomplete)"

$data = Import-Csv -Path $csvPath

$thirdColumnName = ($data | Get-Member -MemberType NoteProperty)[2].Name

$data | Select-Object -ExpandProperty $thirdColumnName -Unique | ForEach-Object {
    Write-Output $_
}