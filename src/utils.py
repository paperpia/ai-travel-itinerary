# src/utils.py

import requests
from rich import print
from rich.markdown import Markdown

API_KEY = ""  # ⚠️ Replace with your own API key if needed

def display_current_weather(location):
    """Display real-time weather for a location using SheCodes Weather API"""
    api_url = f"https://api.shecodes.io/weather/v1/current?query={location}&key={API_KEY}"
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()

    temperature = round(data['temperature']['current'])
    condition = data['condition']['description']

    print(f"\nThe current temperature in [bold]{location}[/bold] is [bold]{temperature}°C[/bold], {condition}")

def generate_itinerary(origin, destination, duration):
    """Generate a travel itinerary using SheCodes AI API"""
    print(f"\n✍️ Generating itinerary from {origin} to {destination}...")

    prompt = f"""Generate a travel itinerary from {origin} to {destination} in {duration} days.
    This is a road trip, so keep it short—less than 15 lines.
    Add emojis for readability and make the UI pretty.
    Include an estimated cost and temperature for each day (in the currency of the country they're traveling in), such as hotels, fuel, etc."""
    
    context = "You are a travel specialist and know the best tourist spots around the world."
    api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={prompt}&context={context}&key={API_KEY}"

    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()

    itinerary = Markdown(data['answer'])
    print(itinerary)
