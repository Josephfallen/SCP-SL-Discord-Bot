import discord
from discord.ext import commands
from utilities import load_json_data
import logging
import time  # Import time module
import io  # Import io module
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import json  # Import json for JSON handling

logger = logging.getLogger(__name__)

# Constants (Make sure to define these at the top)
QUERY_INTERVAL = 11  
DATA_FILE = 'data.json'  # Path to your JSON file
SERVER_INDEX = 0  # Index of the server to check
BOT_VERSION = '4.3.0'  

last_query_time = 0  # Initialize last_query_time

def setup_commands(client):
    # Basic commands
    @client.command(name='ping')
    async def ping(ctx):
        embed = discord.Embed(
            title="Ping",
            description=f"Pong! {round(client.latency * 1000)}ms",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @client.command(name='help')
    async def help_command(ctx):
        embed = discord.Embed(
            title="Help Menu",
            description=(
                "`!ping` - Check the bot's latency.\n"
                "`!help` - Display this help message.\n"
                "`!players` - Display the amount of players currently in the server.\n"
                "`!version` - Displays the bot's current version.\n"
                "`!json_test` - Test reading from the JSON file.\n"
            ),
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    # Command to display player count
    @client.command(name='players')
    async def player_count(ctx):
        global last_query_time

        current_time = time.time()
        
        # Check if QUERY_INTERVAL has passed since the last query
        if current_time - last_query_time >= QUERY_INTERVAL:
            try:
                # Read data from the file
                data = load_json_data(DATA_FILE)
                if data.get("Success"):
                    # Update the last query time
                    last_query_time = current_time

                    # Proceed to generate the player count plot
                    player_count = data["Servers"][SERVER_INDEX]["Players"]
                    total_players, total_slots = map(int, player_count.split("/"))

                    # Create the plot
                    fig, ax = plt.subplots(figsize=(10, 5))
                    fig.patch.set_facecolor('#1c1c1c')  # Background color of the figure

                    # Set the text in the middle
                    plt.text(0.5, 0.5, f'{total_players:,} / {total_slots:,}\nPlayers Online', 
                             horizontalalignment='center', verticalalignment='center', 
                             fontsize=50, color='#4CAF50', fontweight='bold',
                             transform=ax.transAxes)

                    # Remove axes
                    ax.axis('off')

                    # Save the plot to a BytesIO object
                    buf = io.BytesIO()
                    plt.savefig(buf, format='png', bbox_inches='tight', transparent=True)
                    buf.seek(0)
                    plt.close(fig)

                    # Send the plot as a file in Discord
                    await ctx.send(file=discord.File(fp=buf, filename='player_count.png'))
                else:
                    embed = discord.Embed(
                        title="Player Count",
                        description="Failed to fetch player count from the API. Please try again later.",
                        color=discord.Color.red()
                    )
                    await ctx.send(embed=embed)
            except Exception as e:
                logger.error(f"Error fetching player count: {e}")
                embed = discord.Embed(
                    title="Player Count Error",
                    description="An error occurred while fetching player count.",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Player Count",
                description=f"Please wait {QUERY_INTERVAL} seconds between queries.",
                color=discord.Color.yellow()
            )
            await ctx.send(embed=embed)

    @client.command(name='json_test')
    async def json_test(ctx):
        try:
            # Load data from the JSON file
            data = load_json_data(DATA_FILE)
            
            # Function to censor sensitive information
            def censor_sensitive_info(data):
                if isinstance(data, dict):
                    # Remove or obscure sensitive information
                    data = {k: (v if k not in ["port", "ID"] else "REDACTED") for k, v in data.items()}
                    # Recursively process nested dictionaries
                    for key, value in data.items():
                        if isinstance(value, dict):
                            data[key] = censor_sensitive_info(value)
                        elif isinstance(value, list):
                            data[key] = [censor_sensitive_info(item) if isinstance(item, dict) else item for item in value]
                elif isinstance(data, list):
                    data = [censor_sensitive_info(item) if isinstance(item, dict) else item for item in data]
                return data
            
            # Censor the sensitive information
            censored_data = censor_sensitive_info(data)
            
            # Create an embed with the censored data
            embed = discord.Embed(
                title="JSON Test",
                description=f"Data loaded from JSON file:\n```json\n{json.dumps(censored_data, indent=4)}```",
                color=discord.Color.green()
            )
        except Exception as e:
            embed = discord.Embed(
                title="JSON Test",
                description=f"Error: {e}",
                color=discord.Color.red()
            )
        
        await ctx.send(embed=embed)

    @client.command(name='version')
    async def version(ctx):
        embed = discord.Embed(
            title="Bot Version",
            description=f"**Current Version:** {BOT_VERSION}",
            color=discord.Color.gold()
        )
        await ctx.send(embed=embed)
