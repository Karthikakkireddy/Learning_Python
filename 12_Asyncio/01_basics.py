import asyncio


async def take_process_order(number):
    print(f"Take order for customer #{number}")
    await asyncio.sleep(4)
    print(f"Order ready for  customer #{number}")

# for i in range(4):
#     asyncio.run(take_process_order(i))
#     # Out put
#     # Take order for customer #0
#     # Order ready for  customer #0
#     # Take order for customer #1
#     # Order ready for  customer #1
#     # Take order for customer #2
#     # Order ready for  customer #2
#     # Take order for customer #3
#     # Order ready for  customer #3

asyncio.run(take_process_order(1))
print("hello")
# Take order for customer #1
# Order ready for  customer #1
# hello