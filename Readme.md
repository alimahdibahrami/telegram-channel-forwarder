# Telegram Channel Forwarder

A Python script that forwards messages from one Telegram channel to another using the Telethon library. This script supports both text and media messages and keeps track of the last forwarded message to avoid duplicates.

## Features

- **Forward text and media messages**: Forward text and media messages from a source channel to a destination channel.
- **Track last sent message**: Keeps track of the last sent message to avoid duplicate forwarding.
- **Persistent Telegram session**: The session is saved locally, so you don’t need to re-enter the login code every time you run the script. This prevents getting temporarily blocked by Telegram for too many login requests.
- **Resume from the last sent message**: If the program stops for any reason (e.g., internet issues), it can resume from the last sent message after restarting.
- **Random delay between messages**: Random delay between messages to avoid being flagged by Telegram.

## Prerequisites

- Python 3.7 or higher
- Telethon library

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/telegram-channel-forwarder.git
   cd telegram-channel-forwarder
   ```

2. **Install Dependencies**

   Install the required Python libraries using pip:

   ```bash
   pip install telethon
   ```

## Getting Started

1. **Obtain API Credentials from Telegram**

   To use this script, you need to get your `api_id` and `api_hash` from the [Telegram API Development Tools](https://my.telegram.org/apps).

2. **Configure the Script**

   Open the `script.py` file and fill in the following variables:

   ```python
   api_id = 'YOUR_API_ID'
   api_hash = 'YOUR_API_HASH'
   phone_number = '+YOUR_PHONE_NUMBER'
   session_name = 'YOUR_SESSION_NAME'
   source_channel_id = 'SOURCE_CHANNEL_ID'
   destination_channel_id = 'DESTINATION_CHANNEL_ID'
   ```

3. **Run the Script**

   Run the script with Python:

   ```bash
   python script.py
   ```

   The script will ask for a login code sent to your Telegram app if it is the first time you are running it. Enter the code to authenticate.

## How It Works

- The script connects to the Telegram client using the provided credentials.
- It fetches messages from the specified source channel and forwards them to the destination channel.
- A JSON file (`last_message.json`) is used to keep track of the last sent message, ensuring no message is sent twice.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/alimahdibahrami/telegram-channel-forwarder/blob/main/LICENSE) file for details.