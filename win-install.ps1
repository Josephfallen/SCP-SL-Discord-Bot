echo "Welcome to the installer to get you going with SCP:SL Bot"
wait(5)
echo "Install beginning now"


@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

wait(5)

# Install Discord.py
echo "Installing discord.py..."
pip3 install discord.py --break-system-packages


wait(2)
# Install MySQL Connector for Python
echo "Installing mysql-connector-python..."
pip3 install mysql-connector --break-system-packages


wait(2)
echo "Installing aiohttp"
pip3 install aiohttp --break-system-packages


wait(2)
echo "Installing pyyaml"
pip3 install pyyaml --break-system-packages


wait(2)
echo "Installing loguru"
pip3 install logguru --break-system-packages


wait(2)
echo "Installing matplotlib"
pip3 install matplotlib


echo "If you wish to know about each modual please see the "modules.md" file."
wait(10)

wait(2)
echo "All moduals installed!"
