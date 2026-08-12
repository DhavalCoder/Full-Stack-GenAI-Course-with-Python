import asyncio

async def brew_chai():
    print("Brewing chai ....")
    await asyncio.sleep(2)
    print("Chai is Ready")

asyncio.run(brew_chai())    