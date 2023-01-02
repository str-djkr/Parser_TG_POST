from telethon.sync import TelegramClient, events, errors
import asyncio
import re
import os 


api_id = 000000     #take from your api
api_hash = ''       #take from your api
phone = ''

channels = 'https://t.me/test1_start' #from (may be an array)
my_channel = 'https://t.me/test1_second'  #your channel

tags = '' #what to add to the forwarded

client = TelegramClient('session_name',
                    api_id,
                    api_hash)
client.start()
async def dowl_POST():
    for message in await client.get_messages(my_channel, limit=1):
        os.chdir("E:\\Parser_TG_POST\\Post_photo") #disk path
        await message.download_media()
        os.getcwd()


with TelegramClient(phone, api_id, api_hash) as client:
    print("Activated")

    @client.on(events.NewMessage(chats=channels))
    async def Messages(event):
        if not event.grouped_id\
                and not event.message.forward:
            text = event.raw_text
            try:
                await client.send_message(
                    entity=my_channel,
                    file=event.message.media,
                    message=text + tags,
                    parse_mode='md',
                    link_preview=False)
                await dowl_POST()
                    
            except errors.FloodWaitError as e:
                print(f'ERROR 01: {e.seconds} seconds')
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print('ERROR 02:', e)
                
        elif event.message.text and not event.message.media\
            and not event.message.forward\
                and not event.grouped_id:
            try:
                await client.send_message(
                    entity=my_channel,
                    message=text + tags,
                    parse_mode='md',
                    link_preview=False)
                await dowl_POST()

            except errors.FloodWaitError as e:
                print(f'ERROR 01: {e.seconds} seconds')
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print('ERROR 02:', e)
        elif event.message.forward:
            try:
                await event.message.forward_to(my_channel)
                await dowl_POST()
            except errors.FloodWaitError as e:
                print(f'ERROR 01: {e.seconds} seconds')
            except Exception as e:
                print('ERROR 02:', e)

    @client.on(events.Album(chats=channels))
    async def Album(event):
        text = event.original_update.message.message
        print(text)
        try:
            await client.send_message(
                entity=my_channel,
                file=event.messages,
                message=text + tags,
                parse_mode='md',
                link_preview=False)
            await dowl_POST()

        except errors.FloodWaitError as e:
            print(f'ERROR 01: {e.seconds} seconds')
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print('ERROR 02:', e)

    client.run_until_disconnected()
    print('OFLINE')
