#!/usr/bin/env python

#import packages
import asyncio                   # for async IO
import websockets                # library for websockets protocoll
import json                      # handle json file
from collections import Counter  # count occurences

URI = "ws://echo.websocket.org"
NEEDED_KEYS = {"id", "tadd", "name", "sn"} # required keys in json object

async def communicate_with_uri(send):
    """ Sends string 'send' to 'URI' and returns servers answer """
    async with websockets.connect(URI) as websocket:
        # send string to URI
        await websocket.send(send)

        # recieve answer from URI
        recieve = await websocket.recv()

    return recieve

def has_keys(entry, needed_keys):
    """ Returns true if a given entry contains all keys, else this function returns false """
    return needed_keys.issubset(
        set(map(str.casefold, entry.keys()))
        )

async def get_occurences(json_file):
    """ Returns occurences in entry 'category' and prints ID into terminal from the given json file """ 
    async with websockets.connect(URI) as websocket:
        # open json file
        with open(json_file, "r") as f:
                json_obj = json.load(f)
        
        # dump json object to string
        # use websocket protocol for sending json string
        await websocket.send(json.dumps(json_obj))

        # recieve answer from URI
        recieve = await websocket.recv()

        # convert recieved string into json object
        data = json.loads(recieve)

        # initialize empty counter
        occurences = Counter() 

        # for loop over all entries in json file
        for entry in data: # entry is of type dictionary
            if has_keys(entry, NEEDED_KEYS):
                occurences.update([entry["category"]]) # update counter 
                print(f'Read ID: {entry["id"]}') # print "id" to terminal
                print([entry["category"]])

    return occurences


if __name__ == "__main__":
    data = asyncio.get_event_loop().run_until_complete(get_occurences("DevicesList.json"))
    print(data)