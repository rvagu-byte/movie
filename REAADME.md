# 🎬 Netflix EDA Project — Exploratory Data Analysis

## 📌 Overview
This project performs a comprehensive **Exploratory Data Analysis (EDA)** on the Netflix Titles dataset (~8,800 entries). It uncovers patterns in content distribution, growth trends, genres, ratings, and duration.

Unlike a basic notebook, this project is built as a **modular, production-style pipeline** with clean code structure, automated tests, and reproducibility.

---

## 🎯 Objectives
- Analyze distribution of Movies vs TV Shows
- Study growth of Netflix content over time
- Identify top contributing countries
- Explore genre and rating patterns
- Understand movie duration trends
- Build a reusable EDA pipeline

---

## 📂 Project Structure
netflix-eda/
├── data/netflix_titles.csv
├── src/
│ ├── load.py
│ ├── clean.py
│ ├── analyse.py
│ └── visualise.py
├── tests/
│ ├── test_load.py
│ ├── test_clean.py
│ └── test_analyse.py
├── notebooks/eda_walkthrough.ipynb
├── outputs/plots/
├── docs/insights.md
├── main.py
├── requirements.txt
└── README.md



---

## ⚙️ Pipeline Flow
Raw CSV → Load → Clean → Analyse → Visualise → Insights

---

## 🔧 Modules Explanation

### Load (`load.py`)
- Reads dataset using pandas
- Validates required columns
- Checks missing values

### Clean (`clean.py`)
- Converts `date_added` to datetime
- Creates `year_added`
- Fixes invalid ratings (e.g., "74 min")
- Extracts numeric duration
- Splits multi-value columns (genres, countries)

### Analyse (`analyse.py`)
- Titles per year
- Top countries
- Genre counts
- Rating distribution
- Duration statistics

### Visualise (`visualise.py`)
- Generates and saves plots:
  - Content type distribution
  - Titles added per year
  - Top countries
  - Ratings distribution
  - Top genres
  - Duration histogram
  - Release trends

---

## 📊 Key Insights
- 70% content are Movies, 30% TV Shows
- United States is the largest contributor
- India ranks #2 in content production
- 2019 had the highest number of releases
- TV-MA is the most common rating
- "International Movies" is the top genre
- Most movies are 90–120 minutes long

---

## 🧪 Testing
- 28 unit tests using `unittest`
- Ensures correct data loading, cleaning, and analysis

Run:
python -m unittest discover -s tests -v



---

## 🚀 Installation & Usage

Clone:
git clone https://github.com/your-username/netflix-eda.git
cd netflix-eda



Install:
pip install -r requirements.txt



Run:
python main.py



---

## 📁 Outputs
- Plots → `outputs/plots/`
- Insights → `docs/insights.md`

---

## 🧠 Design Principles
- Single Responsibility Principle
- Modular Architecture
- Reproducibility
- Testability

---

## 🔮 Future Improvements
- Streamlit dashboard
- NLP on descriptions
- Actor/Director network analysis
- Recommendation system

---

## 👨‍💻 Author
Your Name

---

⭐ Star this repo if you found it useful!
