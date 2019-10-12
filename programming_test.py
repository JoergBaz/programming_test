#!/usr/bin/env python

#import packages
import asyncio      # for async IO
import websockets   # library for websockets protocoll

URI = "ws://echo.websocket.org"

async def communicate_with_uri(send):
    async with websockets.connect(URI) as websocket:
        await websocket.send(send)
        recieve = await websocket.recv()

    return recieve


if __name__ == "__main__":
    answer = asyncio.get_event_loop().run_until_complete(communicate_with_uri("test_string"))
    print(answer)