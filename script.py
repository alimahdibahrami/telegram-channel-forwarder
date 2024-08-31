import asyncio  # Importing asyncio for asynchronous operations
from telethon import TelegramClient  # Importing the TelegramClient from the Telethon library for interacting with Telegram API
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument  # Importing necessary Telegram types for handling media messages
import json  # Importing JSON module to handle reading and writing JSON files
import os  # Importing os module to interact with the operating system (e.g., file operations)
import random  # Importing random module to add random delays

# Initial settings for Telegram API access
api_id = 'YOUR_API_ID'  # Your Telegram API ID
api_hash = 'YOUR_API_HASH'  # Your Telegram API Hash
phone_number = '+YOUR_PHONE_NUMBER'  # Your phone number with country code
session_name = 'YOUR_SESSION_NAME'  # Session name for the Telegram client

# Channel IDs for the source and destination channels
source_channel_id = 'SOURCE_CHANNEL_ID'  # Source channel ID
destination_channel_id = 'DESTINATION_CHANNEL_ID'  # Destination channel ID

# File to store the ID of the last sent message
last_message_file = 'last_message.json'

async def handle_telegram_session(client):
    """
    Main function to handle fetching messages from the source channel and sending them to the destination channel.
    It keeps track of the last sent message to avoid duplicates.
    """
    # Retrieving the last sent message ID
    last_message = None
    if os.path.exists(last_message_file):
        with open(last_message_file, 'r') as f:
            try:
                last_message = json.load(f)
            except json.JSONDecodeError:
                last_message = None

    # Fetching all messages from the source channel starting from the first message
    async for message in client.iter_messages(source_channel_id, reverse=True):
        if last_message and message.id <= last_message['id']:
            continue  # Skip messages that have already been sent

        # Sending text messages to the destination channel
        if message.text:
            await client.send_message(destination_channel_id, message.text)
        # Sending media messages (photos or documents) to the destination channel
        if message.media:
            if isinstance(message.media, (MessageMediaPhoto, MessageMediaDocument)):
                await client.send_file(destination_channel_id, message.media)

        # Save the last sent message ID
        with open(last_message_file, 'w') as f:
            json.dump({'id': message.id}, f)
        
        print(f"Message {message.id} sent successfully")

        # Random delay between 3 to 10 seconds between each message to avoid being flagged by Telegram
        await asyncio.sleep(random.uniform(3, 10))

async def main():
    """
    Main function to initialize the Telegram client and manage user authorization.
    """
    try:
        # Creating the client and connecting to Telegram
        async with TelegramClient(session_name, api_id, api_hash) as client:
            # If the session file does not exist, request the login code
            if not await client.is_user_authorized():
                await client.send_code_request(phone_number)
                code = input('Enter the code you received: ')
                await client.sign_in(phone_number, code)

            # Execute the main session handling function
            await handle_telegram_session(client)
    except Exception as e:
        print(f"An error occurred: {e}")

# Running the main function
asyncio.run(main())
