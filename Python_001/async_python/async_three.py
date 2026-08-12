import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")


async def main():
    urls = ["https://jsonplaceholder.typicode.com/todos/1"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls ]
        await asyncio.gather(*tasks)

asyncio.run(main())