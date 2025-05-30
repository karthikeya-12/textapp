import asyncio

async def run_po():
    from textapp.one.po import main
    await main()
if __name__ == "__main__":
    asyncio.run(run_po())