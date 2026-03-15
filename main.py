import os
import random
import csv
import schedule
import time
from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv
from affirmations import AFFIRMATIONS, VALID_MOODS

load_dotenv()

def log_to_csv(mood, affirmation):
    file_exists = os.path.isfile("mood_log.csv")
    with open("mood_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "mood", "affirmation"])  # header
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), mood, affirmation])

def send_affirmation():
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token  = os.environ["TWILIO_AUTH_TOKEN"]
    from_number = os.environ["TWILIO_PHONE_NUMBER"]
    to_number   = os.environ["MY_PHONE_NUMBER"]

    client = Client(account_sid, auth_token)

    # Pick a random mood since no one is typing
    mood = random.choice(VALID_MOODS)
    affirmation = random.choice(AFFIRMATIONS[mood])

    message_body = (
        f"🌟 Good Morning! ({mood.capitalize()} energy today)\n\n"
        + affirmation
        + "\n\n— Your Morning Bot 🤖"
    )

    message = client.messages.create(
        body=message_body,
        from_=from_number,
        to=to_number
    )

    log_to_csv(mood, affirmation)  # save to CSV
    print(f"[{datetime.now()}] ✅ SMS sent! Mood: {mood} | SID: {message.sid}")

# Schedule it every day at 8:00 AM
schedule.every().day.at("08:00").do(send_affirmation)

print("🤖 Bot is running... Press Ctrl+C to stop.")
print("   Will send SMS every day at 08:00 AM.")

# Run once immediately so you can test it right now
send_affirmation()

while True:
    schedule.run_pending()
    time.sleep(60)  # check every minute
