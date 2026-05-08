import asyncio

async def take_process_order(number):
    print(f"Take order for customer #{number}")
    await asyncio.sleep(4)
    print(f"Order ready for  customer #{number}")

async def main():
    coroutines =[] 

    for i in range(5):
        coroutines.append(
            take_process_order(i)
        )

    await asyncio.gather(*coroutines)

asyncio.run(main())