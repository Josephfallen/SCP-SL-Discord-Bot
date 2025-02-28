#!/bin/bash

# Update package list
echo "Updating package list..."
sudo apt update

# Install Python3 and pip if not installed
echo "Checking for Python3 and pip..."
sudo apt install -y python3 python3-pip

# Install Discord.py
echo "Installing discord.py..."
pip3 install discord.py --break-system-packages

# Install MySQL Connector for Python
echo "Installing mysql-connector-python..."
pip3 install mysql-connector --break-system-packages

echo "Installing aiohttp"
pip3 install aiohttp --break-system-packages

echo "Installing pyyaml"
pip3 install pyyaml --break-system-packages

echo "Installing loguru"
pip3 install logguru --break-system-packages

echo "Installing matplotlib"
pip3 install matplotlib

echo "All moduals installed!"


# Done
echo "Setup is complete."
