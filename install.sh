echo $(python3 --version)
echo 'Installing dependancies...'
pip3 install pyinstaller --user && \
	cd src && \
	~/.local/bin/pyinstaller cryptsnake.py --onefile && \
	echo "We're going to need your permission for creating a global link to cryptsnake"
	sudo rm /usr/bin/cryptsnake && \
	sudo cp dist/cryptsnake /usr/bin/cryptsnake
echo 'Cleaning dependancies...'
pip3 uninstall pyinstaller -y
echo 'Successfully installed!'
echo $(cryptsnake -h)
