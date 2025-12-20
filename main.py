import asyncio
from init_db import initialize_db

import bot

if __name__ == '__main__':
    initialize_db()
    asyncio.run(bot.run_discord_bot())
