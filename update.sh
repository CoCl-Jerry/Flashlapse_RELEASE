sudo rm -r /home/pi/Documents/Flashlapse_RELEASE
if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
	cd /home/pi/Documents/backup/Flashlapse_RELEASE
	git pull
fi
sudo cp -r /home/pi/Documents/backup/Flashlapse_RELEASE /home/pi/Documents
