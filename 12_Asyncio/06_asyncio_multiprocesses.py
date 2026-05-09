import asyncio
from concurrent.futures import ProcessPoolExecutor
import time


def encrypt(data):
    return f"Data is encrypted {data[::-1]}"

async def main():
    loop_for_processes = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop_for_processes.run_in_executor(
            pool, 
            encrypt,
            "credit_card_1234"
        )
        print(result)
        
if __name__ == "__main__":
    asyncio.run(main())