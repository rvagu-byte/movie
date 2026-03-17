# 🎬 Netflix Titles — Exploratory Data Analysis

A complete EDA project on the Netflix Titles dataset (~8,800 titles), covering data cleaning,
univariate/bivariate analysis, trend exploration, and publication-ready visualisations.

---

## 📁 Project structure

```
netflix-eda/
│
├── data/
│   └── netflix_titles.csv          # Raw dataset
│
├── src/
│   ├── __init__.py
│   ├── load.py                     # Data loading & validation
│   ├── clean.py                    # Cleaning & feature engineering
│   ├── analyse.py                  # Aggregation & stats helpers
│   └── visualise.py                # All plot functions
│
├── notebooks/
│   └── eda_walkthrough.ipynb       # Interactive notebook walkthrough
│
├── outputs/
│   └── plots/                      # Saved figures (PNG)
│
├── tests/
│   ├── test_load.py
│   ├── test_clean.py
│   └── test_analyse.py
│
├── docs/
│   └── insights.md                 # Written findings & interpretations
│
├── main.py                         # Run the full EDA pipeline
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Quick start

```bash
# 1. Clone / download the repo
git clone https://github.com/yourname/netflix-eda.git
cd netflix-eda

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the full pipeline
python main.py

# 5. (Optional) Launch the notebook
jupyter notebook notebooks/eda_walkthrough.ipynb
```

All plots are saved to `outputs/plots/`.

---

## 📊 Analyses covered

| Analysis | Description |
|---|---|
| Content type split | Movies vs TV Shows proportion |
| Library growth | Titles added to Netflix per year |
| Country distribution | Top producing nations |
| Ratings breakdown | Audience age-rating distribution |
| Genre popularity | Most common genre tags |
| Movie duration | Runtime histogram |
| Release year trend | Original release year distribution |
| Missing data report | Null counts per column |

---

## 🔍 Key findings

- **Netflix is movie-heavy** — 69.6 % of the catalogue are films.
- **2019 was peak addition year** with 2,016 titles added.
- **India is #2** globally for content production (1,046 titles), reflecting Bollywood investment.
- **TV-MA dominates ratings** (36 %), confirming a mature-audience focus.
- **International Movies** is the single largest genre tag (2,752 titles).
- Most movies run **90–120 minutes** — the classic feature sweet spot.

---

## 🛠 Tech stack

- **Python 3.9+**
- pandas · numpy · matplotlib · seaborn
- jupyter (optional, for the notebook)
- pytest (for tests)

---

## 📄 License

MIT
