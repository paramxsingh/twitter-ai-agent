# 🤖 Twitter AI Agent

An AI-powered agent that generates and posts engaging tweets automatically using OpenAI and the Twitter API. It includes hashtag optimization, scheduling capabilities, and a basic dashboard to track performance.


## 🚀 Features

- ✨ AI-generated tweet content using OpenAI
- 🐦 Auto-posting to Twitter via Tweepy
- 🏷 Hashtag optimization (extendable)
- 📊 Basic Streamlit dashboard for monitoring
- ⚙️ Easily configurable via `.env` and `config.py`


## 📁 Project Structure

twitter-ai-agent/
├── ai/                  # AI-powered tweet generation
├── twitter/             # Authentication and tweet posting
├── dashboard/           # (Optional) Streamlit dashboard
├── utils/               # Helper functions
├── main.py              # Entry point for execution
├── config.py            # Environment variable config
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/paramxsingh/twitter-ai-agent.git
cd twitter-ai-agent

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Create `.env` File

Create a `.env` file with your API keys:

API_KEY=your_twitter_api_key
API_SECRET=your_twitter_api_secret
ACCESS_TOKEN=your_twitter_access_token
ACCESS_SECRET=your_twitter_access_secret
OPENAI_KEY=your_openai_api_key

### 4. Run the Agent

python main.py

This will generate a tweet and post it to your Twitter account.

## 📊 Optional: Run the Dashboard


streamlit run dashboard/app.py


## 🧠 Powered By

* [OpenAI](https://openai.com/)
* [Tweepy](https://docs.tweepy.org/)
* [Streamlit](https://streamlit.io/)

## 📄 License

MIT License

## 💡 Future Improvements

* Tweet scheduling
* Image and meme generation
* Auto-reply to DMs or tweets
* Analytics from Twitter API (likes, retweets, followers)
* And many more to come...
