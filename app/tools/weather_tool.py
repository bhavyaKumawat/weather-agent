import requests
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from dataclasses import dataclass   
from langchain.tools import tool, ToolRuntime

weather = OpenWeatherMapAPIWrapper()


@tool
def get_user_location() -> str:
    """Get the user's location from their IP."""
    response = requests.get("https://ipinfo.io/json")
    data = response.json()
    return f"{data['city']}, {data['country']}"

tools = [weather.run, get_user_location]


if __name__ == "__main__":
    weather_data = weather.run("London,GB")
    print(weather_data)
