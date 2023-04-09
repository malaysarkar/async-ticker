import asyncio
import logging
import os

import dotenv

from async_ticker import MainTicker

logging.basicConfig(level=logging.DEBUG)

# API credentials
dotenv.load_dotenv()
api_key = os.environ.get("API_KEY")
access_token = os.environ.get("ACCESS_TOKEN")

# Initialize main ticker
ws = MainTicker(api_key, access_token)

def on_ticks(ws, ticks):
    # Callback to receive ws ticks.
    logging.debug("Ticks: {}".format(ticks))

def on_connect(ws, response):
    # Callback on successful connect.
    ws.subscribe([738561, 5633])

    ws.set_mode(ws.MODE_LTP, [5633])
    ws.set_mode(ws.MODE_FULL, [738561])

ws.on_connect = on_connect
ws.on_ticks = on_ticks
asyncio.get_event_loop().run_until_complete(ws.create_connection(asyncio.get_event_loop()))
asyncio.get_event_loop().run_forever()