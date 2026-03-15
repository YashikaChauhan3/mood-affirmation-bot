# 🌟 Mood Affirmation Bot

A Python bot that sends you a **daily motivational SMS** every morning automatically — powered by the Twilio API.

---

## 💬 How It Works

1. Run the script once
2. It sends you an SMS immediately (so you can test it)
3. Every day at 8:00 AM it automatically sends a fresh affirmation
4. Every message is logged to `mood_log.csv` for tracking over time

---

## 🛠️ Tech Stack

- Python 3
- Twilio API (SMS)
- schedule (daily automation)
- csv (mood logging)

---

## ⚙️ Setup

### 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/mood-affirmation-bot.git
cd mood-affirmation-bot

### 2. Install dependencies
pip install -r requirements.txt

### 3. Set up Twilio
- Sign up at twilio.com (free trial gives $15 credit)
- Buy a US phone number (~$1.15 deducted from free credit)
- Verify your personal number in Twilio Console
- Get your Account SID and Auth Token from the Console

### 4. Create your .env file
cp .env.example .env

Fill in your credentials:
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_us_number
MY_PHONE_NUMBER=your_personal_number_with_country_code

### 5. Run the bot
python main.py

Keep the terminal open — it will send an SMS immediately
then automatically every day at 8:00 AM.

---

## 📁 Project Structure

mood-affirmation-bot/
├── main.py             # Scheduler + SMS logic
├── affirmations.py     # Mood → affirmation data
├── requirements.txt
├── .env.example        # Template for environment variables
└── README.md

---

## 🚀 Planned Enhancements
- [ ] Two-way SMS bot — text your mood, get a personalized reply (Flask + ngrok)
- [ ] Web dashboard to visualize mood history from CSV
- [ ] Deploy to Render/Railway so it runs 24/7 without keeping terminal open

---

## 📝 License
MIT