# src/main.py

from rich import print
from src.utils import display_current_weather, generate_itinerary

def welcome_user():
    print("[magenta]🌍 Welcome to the AI Travel Itinerary Generator![/magenta]")

def credit():
    print("[blue]Created by [bold]PAM[/bold] – Thank you for using the app![/blue]")

def run():
    welcome_user()

    origin = input("\nWhere are you traveling from? ")
    destination = input("Where are you traveling to? ")
    duration = input("How many days is your trip? (Enter a number only, e.g. 3): ")

    if origin and destination and duration.isdigit():
        display_current_weather(origin)
        display_current_weather(destination)
        generate_itinerary(origin, destination, duration)
    else:
        print("[red]❌ Invalid input. Please enter valid origin, destination, and numeric duration.[/red]")

    credit()

if __name__ == "__main__":
    run()
