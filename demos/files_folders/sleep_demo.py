

import time
import asyncio


time.sleep(2)

while True:
    if not check_for_something():
        asyncio.sleep(2)