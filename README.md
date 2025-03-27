# 🌎 AI-Powered Travel Itinerary Generator

A Python application that uses AI and real-time weather data to generate a fun, emoji-filled, cost-estimated **road trip itinerary** between two destinations.

Built as a final project for the SheCodes Python and AI Bootcamp by **PAM**.

---

## ✨ Features

- 🌤️ Real-time weather information using the SheCodes Weather API  
- ✈️ Automatically generated, multi-day road trip itineraries  
- 💸 Estimated daily travel costs (fuel, hotel, etc.)  
- 📱 User-friendly terminal UI with styled Markdown using the `rich` library  
- 🤖 AI-generated travel plans powered by SheCodes AI API  

---

## 🧠 How It Works

1. The user inputs their **origin**, **destination**, and **number of days**.
2. The app fetches real-time weather data for both locations.
3. It sends a request to an AI API with a custom prompt to generate a fun and useful itinerary.
4. The response is rendered in a styled format using Markdown and emoji.

---

## 🛠 Tech Stack

- **Python 3**
- `requests` – to interact with APIs  
- `rich` – for beautiful terminal output  
- SheCodes Weather & AI APIs

---

## 🚀 Getting Started

1. Clone the repo:

```bash
git clone https://github.com/piamclaughlin/ai-travel-itinerary.git
cd ai-travel-itinerary
