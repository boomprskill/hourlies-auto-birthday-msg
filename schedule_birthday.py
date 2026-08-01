import os
import requests
from datetime import datetime, timedelta

# SET INFO
GITHUB_USER = "boomprskill" # Change this into your Github username
REPO_NAME = "hourlies-happy-birthday-message-schedule" # Change this into your own repository name
BRANCH = "main" # Usually 'main' or 'master'

# Make Alias for the characters folder
C = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/{BRANCH}/characters"

# Get Discord Webhook URL from secrets (check README.md at Setup Instructions)
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

# NOTE: Just put only the filename in "image"
characters = [
    {
        "name": "Bonnie Oryx", # Set display name for your characters
        "image": "Bonnie-Oryx.webp", # Write only the file name for all of the characters
        "date": "12-14" # Set birthday date as the schedule when the message should be delivered (Format: MM-DD)
    },
    {
        "name": "Violet Aurora", 
        "image": "Violet-Aurora.webp",
        "date": "10-31"
    },
    {
        "name": "Cassaura Pudjiastuti",
        "image": "Cassaura-Pudjiastuti.webp",
        "date": "05-12"
        
    },
    {
        "name": "Matrie Yoshka",
        "image": "Matrie-Yoshka.webp",
        "date": "09-18"
    },
    {
        "name": "Misaki Momo",
        "image": "Misaki-Momo.webp",
        "date": "04-05"
    },
    {
        "name": "Natsu Iro",
        "image": "Natsu-Iro.webp",
        "date": "12-11"
    },
    {
        "name": "Citra Nurdiyanti",
        "image": "Citra-Nurdiyanti.webp",
        "date": "06-29"
    },
    {
        "name": "Anzheilla Romanova",
        "image": "Anzheilla-Romanova.webp",
        "date": "03-21"
    },
    {
        "name": "Pota Meridiem",
        "image": "Pota-Meridiem.webp",
        "date": "02-14"
    },
    {
        "name": "Thomas Sanders",
        "image": "Thomas-Sanders.webp",
        "date": "08-09"
    },
    {
        "name": "Rowty Theta",
        "image": "Rowty-Theta.webp",
        "date": "10-25"
    },
    {
        "name": "Hawari (Hourlies)",
        "image": "Hawari-(Hourlies).webp",
        "date": "01-01"
    },
]

def check_and_send():
    # Get UTC + 7 time, you can change this code for your own desired timezone
    local_time = datetime.utcnow() + timedelta(hours=7)
    today = local_time.strftime("%m-%d")

    # Print current the time when the script executed
    print(f"Server time (UTC): {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}")
    print(f"Target time (GMT+7): {local_time.strftime('%Y-%m-%d %H:%M')}")
    print(f"Checking birthdays for: {today}")

    found_birthday = False

    # Check all of the listed characters
    for char in characters:

        # Run the condition when the birthday is match with the time when this script is running
        if char["date"] == today:
            found_birthday = True

            # Create the full image url (See line 11)
            full_image_url = f"{C}/{char['image']}"

            # Create the birthday message
            birthday_message = f"HAPPY BIRTHDAY - {char['name']}!🐰🤍"

            # Create the required data for the Webhook to send
            data = {
                "content": "🎉 **Happy Birthday!** 🎂",
                "embeds": [
                    {
                        "title": "It's a special day!",
                        "description": birthday_message,
                        "color": 16750848,
                        "image": {"url": full_image_url},
                        "footer": {"text": "-Hour Dev • 2026"}
                    }
                ]
            }
            
            # Send the payload to Discord and capture the server's response status
            response = requests.post(WEBHOOK_URL, json=data)

            # Check the status of the sended message
            if response.status_code == 204:
                print(f"Successfully sent post for {char['name']}") # Confirm if the message successfully send with the character name
            else:
                print(f"Failed to send. Status: {response.status_code}") # Send the failed message with the error code if the process is not successful

    # This inform to us if there is no birthday found when the script executed
    if not found_birthday:
        print("No birthdays found for today.")

if __name__ == "__main__":
    check_and_send()
