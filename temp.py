import httpx
import asyncio
async def task1():
    await client.get("https://slow-site.com")  # this takes 3s
    print("Task 1 done")

async def task2():
    await asyncio.sleep(1)
    print("Task 2 done")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
