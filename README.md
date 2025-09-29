Simple Discord Weather Bot


TL;DR

Simple Discord bot that lets you type !weather <zip_code> in your server to get the current weather (temperature, wind, and conditions) using WeatherAPI. Easy to set up with your own API keys in a .env file.
A lightweight Discord bot that fetches current weather information for a given U.S. ZIP code using WeatherAPI.



**Features**

Get current weather by typing !weather <zip_code> in your Discord server.

Displays location, temperature (°F), wind speed, and weather conditions.

Validates ZIP code input to ensure it’s 5 digits.

Handles API errors gracefully.

**Setup**

**Clone the repository:**

git clone https://github.com/bhenderson101/simple-discord-weather-bot.git


**Install dependencies:**

pip install -r requirements.txt


**Dependencies: discord.py, requests, python-dotenv**

**Create .env file in the project root with your API keys:

api=YOUR_WEATHERAPI_KEY
token=YOUR_DISCORD_BOT_TOKEN**


**Run the bot:**

python weatherapi.py


**Use the command in Discord:**

!weather 12345

Notes

Make sure your bot has Message Content Intent enabled in the Discord Developer Portal.

Do not commit your .env file to public repositories.
