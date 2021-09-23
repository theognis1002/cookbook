1. `apt-get purge <pkg_name>`
	- removes package alone with all configuration files
1. `uname -a`  or `lsb_release -a`
	- get current operating system and release
1. `passwd <user>`
	- change user password
1. `du -hs <dir>`
	- disk usage w human-readable and summarize flags. see total size of dir
1. `df -h`
	- disk space available in human-readable format
1. `screen`, `screen -ls`, `screen -r`
	- `sudo apt-get install screen`
1. `lsof -i :<port>`
	- find process that is running on a specific port
1. `ps aux | grep <process name>`, `ps -ef | grep <process name>`
	- get PID from process name
1. `kill -15 <PID>` - SIGTERM signal
1. `kill -9 <PID>` - SIGKILL signal
1. `killall <process name>`
