import aiohttp

async def create_session():
    return aiohttp.ClientSession()
