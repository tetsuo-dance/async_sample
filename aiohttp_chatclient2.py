import asyncio
import aiohttp
import sys
import tkinter as tk
from threading import *

root = tk.Tk()
root.title(u'chatroom')
root.geometry('400x300')

async def send_message(msg):
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("http://localhost:8080/ws") as ws:
            await ws.send_str(msg)
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    await ws.close()
                    break
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break


async def recieve_mesage():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("http://localhost:8080/ws") as ws:
            while True:
                try:
                    async for msg in ws:
                        if msg.type == aiohttp.WSMsgType.TEXT:
                            ListBox1.insert(tk.END, msg.data)
                            break
                        elif msg.type == aiohttp.WSMsgType.ERROR:
                            ListBox1.insert(tk.END, "somethin wrong with message")
                            break
                except KeyboardInterrupt:
                    break
            await ws.close()

def call_corutine(msg):
    loop_send = asyncio.new_event_loop()
    loop_send.run_until_complete(send_message(msg))

def recieve_thread(loop_recieve):
    loop_recieve.run_until_complete(recieve_mesage())

Static1 = tk.Label(text=u'▼　メッセージを入れてください。　▼')
Static1.pack()

# Entryを出現させる
Entry1 = tk.Entry(width=50)
Entry1.pack()

# メッセージ送信
Button1 = tk.Button(text=u'送信', width=50, command=lambda: call_corutine(Entry1.get()))
Button1.pack()

# リストボックスを設置してみる
ListBox1 = tk.Listbox(width=55, height=14)
ListBox1.pack()

loop_recieve = asyncio.new_event_loop()
t = Thread(target=recieve_thread,args=(loop_recieve,))
t.start()

tk.mainloop()



