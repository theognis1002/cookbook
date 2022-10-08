find disk usage of major directories
sudo du -cha --max-depth=1 / | grep -E "M|G"