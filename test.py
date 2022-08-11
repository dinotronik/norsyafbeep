import datetime, asyncio, time

async def sucdick():
    while True:
        while datetime.datetime.now().hour == 11 and datetime.datetime.now().minute == 22:
            print("bruh")
        await asyncio.sleep(1)