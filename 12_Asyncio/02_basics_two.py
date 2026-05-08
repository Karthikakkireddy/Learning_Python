import asyncio


async def take_process_order(number):
    print(f"Take order for customer #{number}")
    await asyncio.sleep(4)
    print(f"Order ready for  customer #{number}")

async def say_hello():
    print("hello")

# asyncio.run(take_process_order(1))
# asyncio.run(say_hello())
    # Take order for customer #1
    # Order ready for  customer #1
    # hello
# Two event loops got created seperately
# For async switching to happen: Both coroutines must exist inside SAME event loop.

async def main():
    await asyncio.gather(
            take_process_order(1),
            say_hello()
        )

asyncio.run(main())
    # Take order for customer #1
    # hello
    # Order ready for  customer #1