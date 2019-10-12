#!/usr/bin/env python

#import packages
import asyncio      # for async IO
import websockets   # library for websockets protocoll
import json         # handle json file

URI = "ws://echo.websocket.org"

async def communicate_with_uri(send):
    async with websockets.connect(URI) as websocket:
        # send string to URI
        await websocket.send(send)

        # recieve answer from URI
        recieve = await websocket.recv()

    return recieve

async def send_json_to_uri(json_file):
    async with websockets.connect(URI) as websocket:
        # open json file
        with open(json_file, "r") as f:
                obj = json.load(f)
        
        # dump json object to string
        # use websocket protocol for sending json string
        await websocket.send(json.dumps(obj))

        # recieve answer from URI
        recieve = await websocket.recv()

        # convert recieved string into list
        data = json.loads(recieve)

    return data




if __name__ == "__main__":
    data = asyncio.get_event_loop().run_until_complete(send_json_to_uri("DevicesList.json"))
    print(data)