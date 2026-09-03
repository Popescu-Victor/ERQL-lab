function Show-Menu {
    param([string[]]$Options)
    $selected = 0
    $keyInfo = $null

    while ($keyInfo.VirtualKeyCode -ne 13) { # 13 = Enter
        Clear-Host
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

$files = Get-ChildItem -File | Select-Object -ExpandProperty Name
$choice = Show-Menu -Options $files
Write-Host "You selected: $choice"