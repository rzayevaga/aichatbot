import asyncio
import importlib

from pyrogram import idle

from Aitech import LOGGER, Rzayev
from Aitech.modules import ALL_MODULES


async def anony_boot():
    try:
        await Branded.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("Aitech.modules." + all_module)

    LOGGER.info(f"𝐀𝐢 - ChatBot aktivdir..🌹")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("𝐀𝐢 - ChatBot Söndü..🥀")
