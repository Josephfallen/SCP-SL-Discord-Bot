import logging
import discord
import aiohttp
import json
from utilities import save_data_to_json
from config import sensitive_info

logger = logging.getLogger(__name__)

async def set_bot_status(client, session):
    try:
        server_id = sensitive_info["SERVER_ID"]
        api_key = sensitive_info["API_KEY"]
        async with session.get(f"https://api.scpslgame.com/serverinfo.php?id={server_id}&key={api_key}&players=true") as response:
            raw_text = await response.text()
            data = json.loads(raw_text)
            if data["Success"]:
                players = data["Servers"][0]["Players"]
                total_players, total_slots = map(int, players.split("/"))
                status = discord.Status.online if total_players > 0 else discord.Status.idle
                activity_message = f"{total_players}/{total_slots} players online"
                await client.change_presence(status=status, activity=discord.Game(name=activity_message))
                save_data_to_json(data, 'player_data.json')
    except Exception as e:
        logger.error(f"Error fetching status: {e}")
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="Error fetching data"))
