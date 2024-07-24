from asyncio import sleep
from getpass import getpass
from json import load
from asyncio import run
from os import _exit
from re import search 

from telethon.sync import TelegramClient

from telethon.errors import (
    SessionPasswordNeededError, UserBannedInChannelError
)

class Bot(TelegramClient):
    def __init__(
        self,
        phone_number: str,
        api_id: int,
        api_hash: str
    ) -> None:
        self.api_id: int = api_id
        self.api_hash: str = api_hash
        self.phone_number: str = phone_number
        
        self.client: TelegramClient = TelegramClient(
            self.phone_number,
            api_id = self.api_id,
            api_hash = self.api_hash
        )

        self.status: bool = True
        self.messages_delay: int = 300 # delay between each message
        self.groups_delay: int = 12000 # how often to send messages

    def load_json_file(self, file_name: str) -> object:
        try:
            with open(f'assets/{file_name}', 'rb') as file:
                return load(file)
        except Exception:
            print(f"[-] Error: File {file_name} not found.")
            return {}                  
            
    async def login(self) -> bool:
        try:
            await self.client.connect()
            
            if not await self.client.is_user_authorized():
                try:
                    await self.client.send_code_request(
                        str(self.phone_number)
                    )
                    await self.client.sign_in(
                        self.phone_number, 
                        input("[?] Access code: ")
                    )
                except SessionPasswordNeededError:
                    await self.client.sign_in(password=getpass())
            return True
        except Exception as e:
            print(f"[-] Login failed due to {type(e).__name__}: {str(e)}")
            return False
    
    async def send_message(self, local_chat_id):
        local_chat_entity = await self.client.get_entity(local_chat_id)
        
        for message_id, channel_ids in self.data[local_chat_id].items():
            try:
                text = await self.client.get_messages(
                    local_chat_entity, 
                    ids=int(message_id)
                )
                
                for channel_id in channel_ids:
                    # check if you are meant to reply to a topic or not
                    match = search(r'https://t.me/[^/]+/(\d+)', channel_id)
                    
                    if match:
                        channel_entity = await self.client.get_entity(channel_id.split('/' + match.group(1))[0])
                        await self.client.send_message(channel_entity, text, reply_to=int(match.group(1)))
                    else:
                        channel_entity = await self.client.get_entity(int(channel_id))
                        await self.client.send_message(channel_entity, text)
                    print(f"[+] Successfully forwarded {local_chat_id}{message_id} to {channel_id}!")
            except UserBannedInChannelError as e:
                print(f"[-] You have been banned from sending messages to groups/supergroups until {e.time}!")
                return
            except KeyboardInterrupt:
                return
            except Exception as e:
                print(f"[-] {local_chat_id} [{type(e).__name__}]: {str(e)}")
                pass
            await sleep(self.messages_delay)            
    
    async def main(self) -> None:        
        if not await self.login():
            print(f"[-] Exiting the program...")
            return

        while (self.status):
            try:
                self.data: object = self.load_json_file("data.json")
                
                for chat_id in self.data:
                    await self.send_message(chat_id)
                print(f"[+] Successfully forwarded all messages!\n\n")
                
                await sleep(self.groups_delay)
            except KeyboardInterrupt:
                self.status = False
                break
            except Exception as e:
                print(f"An issue occured [{type(e).__name__}]: {str(e)}")
                continue
        _exit(-3)
                
if __name__ == "__main__":
    bot = Bot("+<phone_number>", 999999, "api_hash") # replace with your credentials
    run(bot.main())
