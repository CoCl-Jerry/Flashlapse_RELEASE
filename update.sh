if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
	sudo rm -r /home/pi/Documents/Flashlapse_RELEASE
	cd /home/pi/Documents
	git clone -b MO63130 https://github.com/CoCl-Jerry/Flashlapse_RELEASE.git
fi
