import datetime
import os
import webbrowser

def remind_new_episode(weekday, airing_time, anime_title, episode_number, episode_link):
    current_day = datetime.datetime.now().weekday()

    if current_day == weekday:
        current_time = datetime.datetime.now().time()
        if current_time >= airing_time:
            print(f"It's time for a new episode of {anime_title}!")
            print(f"Episode {episode_number} is now available.")
            webbrowser.open(episode_link)

# Example usage:
weekday = 4  # Friday (0 is Monday, 1 is Tuesday, and so on)
airing_time = datetime.time(hour=19, minute=0)  # Set the airing time of the anime
anime_title = "My Favorite Anime"
episode_number = 8
episode_link = "https://9animetv.to/watch/i-got-a-cheat-skill-in-another-world-and-became-unrivaled-in-the-real-world-too-18343?ep=101364"

remind_new_episode(weekday, airing_time, anime_title, episode_number, episode_link)
