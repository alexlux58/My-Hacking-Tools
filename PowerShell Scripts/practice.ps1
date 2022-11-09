$computerName = hostname
Write-Output $computerName

# Invoke-Command -ComputerName $computerName {$env:computername}
# Invoke-Command -ComputerName $computerName -ScriptBlock {get-eventlog -logname security | select-object -first 10}

Invoke-Command -ComputerName $computerName -ScriptBlock {get-process | where {$_.name -eq "notepad"}}