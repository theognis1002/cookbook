
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root. Exiting"
    exit 1
fi