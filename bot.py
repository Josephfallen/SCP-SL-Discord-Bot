import logging
import discord
from discord.ext import commands
from config import load_config, sensitive_info
from commands import setup_commands
from status_handler import set_bot_status
from session_manager import create_session
import asyncio

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration
config = load_config()
BOT_TOKEN = sensitive_info["BOT_TOKEN"]
WAIT_TIME = config.get("WAIT_TIME", 60)

# Set up intents
intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.members = True
intents.presences = True

# Create bot instance
client = commands.Bot(command_prefix='!', intents=intents, help_command=None)

# Setup commands
setup_commands(client)

# Event: When bot is ready
@client.event
async def on_ready():
    logger.info("The bot is running.")
    session = await create_session()
    while True:
        await set_bot_status(client, session)
        await asyncio.sleep(WAIT_TIME)

# Run the bot
if __name__ == "__main__":
    try:
        client.run(BOT_TOKEN)
    except Exception as e:
        logger.error(f"Failed to start the bot: {e}")
