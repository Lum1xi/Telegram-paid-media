from send import send
from config import send_time
import asyncio
import time

while True:
    asyncio.run(send())
    time.sleep(send_time)
