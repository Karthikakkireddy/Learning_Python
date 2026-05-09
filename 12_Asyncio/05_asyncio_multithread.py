import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def take_order_old(name):
    print(f"Order taken for customer {name}")
    time.sleep(3)
    print(f"Order ready for customer {name}")

async def main():
    loop_for_threads = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        await loop_for_threads.run_in_executor(
            pool,
            take_order_old,
            "Karthik"
        )


asyncio.run(main())
