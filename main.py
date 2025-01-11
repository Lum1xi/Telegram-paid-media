from send import send
from config import send_time
import asyncio
import time
asyncio.run(send())

while True:
    asyncio.run(send())
    time.sleep(send_time)