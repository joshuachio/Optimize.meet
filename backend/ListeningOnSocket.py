import socket
import json
import asyncio
import os
import websockets
import user_creation
import be_calendar
import be_events


activesessions = {}
pendings = {}
global errorstate
errorstate = 0

def websocket_process(msg):
    #Checks should all be there (Hopefully)
    msg = msg.json()
    #Login
    #Login Format: {'type': 'login', 'username': 'username', 'password': 'password'}
    if msg['type'] == 'login':
        sesh = user_creation.Session(msg['email'], msg['password'])
        if not sesh:
            errorstate = 1
        else:
            sesh.active = True
            activesessions[sesh] = sesh.userID
            return 0
    #Logout
    #Logout Format: {'type': 'logout', 'userID': 'userID'}
    if msg['type'] == 'logout':
        for sesh in activesessions:
            if sesh.userID == msg['userID']:
                activesessions.remove(sesh)
                os.remove()
                return 0
    #Update
    #Update Format: {'type': 'update', 'userID': 'userID', 'update': 'update'}
    if msg['type'] == 'update':
        if msg['userID'] in activesessions:
            pendings[msg['userID']] = msg['update']
            return 0




async def cronch(socket):
    async for message in socket:
        await websocket_process(message)

async def main():
    #Open socket
    socket = websockets.serve(cronch, 'localhost', 8765)
    #'ws:://localhost:8765'
    #Run Loop
    while True:
        for ID in pendings.keys():
            sesh = activesessions[ID]
            sesh.update(pendings[ID])
        await asyncio.sleep(1)

if __name__ == '__main()__':
    asyncio.get_event_loop.run_forever()

#Pre-Loop Activity

#Listen for openings
#Open sessions, store them named as their userID





#Active Session

#Check state
#Store an active if delta
#Update Local Copy
#Update Frontend
#wait for close
#if session closes
#sync local copy to firebase
#delete session
#Delete local copy (??)