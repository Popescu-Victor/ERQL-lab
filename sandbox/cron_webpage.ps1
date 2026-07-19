# Opens a web page in the default browser
$url = "https://example.com"
Start-Process $url

$action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument '-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "C:\Scripts\OpenWebPage.ps1"'

$trigger = New-ScheduledTaskTrigger -Daily -At "9:00AM"

Register-ScheduledTask -TaskName "OpenDailyWebPage" `
    -Action $action -Trigger $trigger -Description "Opens a web page every day"
