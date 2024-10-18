# SCPSL-Discord-Bot
### SCPSL Discord Bot is a Player Count bot written in python for Discord.
##
### Requirements

* Verified SCP:SL Gameserver

* Something to run the bot 24/7

* Python 3.5.3 or higher

* Discord Server

##
### Get your server account id and the api key

1. Run the command `!id` or `!id show` in your SCP:SL server Local Admin console
>[!WARNING]
> Do not use Remote Admin (The one in game)
2. Run the command `!api show` or `!api reset` if you haven't used your Server API Key in the past in your SCP:SL Local Admin console

##
### Get a bot token

  1. You need to go to the [Discord Developer Portal](https://discord.com/developers/applications) then click New Application in the top right corner.
  
  2. Click on create and then click on the left side, bot.
  
  3. Name the bot and give it it's name and profile picture.
  
  4. Get the token by clicking on reset token.
##
### Put your info into `key.py`
  1. The info you'll need at this point will be, Discord Bot token, Server Account ID, and Server API Token.
  2. Put this info in the labled fields
    
    SERVER_ID = 'Server Account ID'
    API_KEY = 'Server API Token'
    BOT_TOKEN = 'Discord Bot Token'

##
### Then run `dependt.py` to install the required Dependencies.
  1. Open the folder containing all the bot's code, and click `dependt.py` or if you are on linux, `python3 dependt.py`
  2. File will auto run and auto close (windows), On linux it will run it and then will return you back to your command line

##
## Run the bot
  
   On Windows you can just open main.py

   On Debian/Ubuntu you can just open the bot via the terminal. You need to navigate to the directory where the bot is located and use the command
   
    `python3 main.py`


##
## Contact for issues
If you have issues contact joseph_fallen on discord

