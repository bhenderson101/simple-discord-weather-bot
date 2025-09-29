import requests
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv("weather.env")

weatherapikey = os.getenv("api")
discordtoken = os.getenv("token")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


async def get_weather(zip_code):
    

    url = f'http://api.weatherapi.com/v1/current.json?key={weatherapikey}&q={zip_code}&aqi=no'
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

    else:
        print(response.status_code)

    formatted_output = f'Location: {weather_data["location"]["name"]}, {weather_data["location"]["region"]}\n Temp: {weather_data["current"]["temp_f"]}\u00b0F\n Wind: {weather_data["current"]["wind_mph"]} mph\n Weather: {weather_data["current"]["condition"]["text"]}'
    

    return formatted_output, response.status_code

@bot.event
async def on_ready():
    print(f'Bot is online and ready, {bot.user.name}')

@bot.command(name="weather")
async def bot_weather(ctx, zip_code: str=None):
        if not zip_code:
             await ctx.send("Weather command should be formatted as !weather zipcodehere")  

        if not zip_code.isdigit():
            await ctx.send("Zip code must be numbers only.")
            return

        if len(zip_code) != 5:
            await ctx.send("Zip code must be 5 digits long.")
            return
        
        else:
            status = None
            try:
                result, status = await get_weather(zip_code)
            except:
                 await ctx.send("Something went wrong, please try again")
                 return
                
        if status != 200:
            await ctx.send(f"API connection error returned: {status}")
        else:
            await ctx.send(result)
    
  
bot.run(discordtoken)
