# 🤖 Multi-Agent AI Tools – Assistant Project

This project explores how to build a simple **multi-agent assistant** using external APIs like Google Search, OpenWeatherMap, and a basic calendar scheduler.

It is part of my hands-on learning journey in **Agentic AI**, where I build autonomous tools that can access external information and respond intelligently to tasks.

---

## 🧩 What It Does

The main script `multi_agent.py` uses 3 tools:

- `search_tool.py`: Looks up information using web search
- `weather_tool.py`: Fetches weather data for a city
- `calendar_tool.py`: Handles event scheduling

These tools simulate how different agents work together to complete tasks. It mimics a basic real-world AI assistant that can retrieve info, organize tasks, and report back to the user.

---

## 🛠 How to Run It

1. **Clone the repository**

```bash
git clone https://github.com/thearakim68/agent_api_project.git
cd agent_api_project
```

2. **Create and activate virtual environment**

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. **Install requirements**

```bash
pip install -r requirements.txt
```

4. **Add your environment variables**  
Create a `.env` file in the root folder and include your API keys:

```env
OPENWEATHER_API_KEY=your_openweather_api_key
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_cse_id
```

5. **Run the assistant**

```bash
python multi_agent.py
```

---

## 🧪 Sample Output

```
Search results: AI in Cambodia is growing with local startups and universities supporting research.
Weather info: The weather in Phnom Penh is 31°C with scattered clouds.
Event: Event 'UX Workshop' scheduled for 2025-10-27 10:00 AM.
```

---

## 🧱 Project Structure

```
agent_api_project/
│
├── .env                        # API Keys (not tracked by Git)
├── .gitignore                  # Ignored files/folders
├── README.md                   # Project overview and setup
├── requirements.txt            # Python dependencies
│
├── multi_agent.py              # Main runner combining all tools
│
├── search_tool.py              # Web search functionality
├── weather_tool.py             # Weather query tool
├── calendar_tool.py            # Calendar scheduling mock tool
│
└── env/                        # Virtual environment (ignored)
```

---

## ⚙️ Tech Stack

- Python 3.11+
- OpenAI + Agentic AI pattern
- OpenWeatherMap API
- Google Programmable Search API (or DuckDuckGo fallback)
- Dotenv for environment variable management

---

## 🙋 About Me

**Kim Theara** – UX/UI Designer | AI Builder | Researcher

- 🌐 [Portfolio](https://theara-me.webflow.io/)
- 🔗 [LinkedIn](https://www.linkedin.com/in/kimtheara-productdesign-ai-expert/)
- 🧑‍💻 [Medium](https://medium.com/@thearakim68)