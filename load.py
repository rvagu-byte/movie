# Netflix EDA — Findings & Insights

## 1. Content composition

Netflix's catalogue is predominantly movies (69.6 %, ~6,131 titles) versus TV shows
(30.4 %, ~2,676 titles). This reflects the platform's origin as a DVD-rental / streaming
service that built its initial library from feature films before commissioning original series.

---

## 2. Library growth over time

| Year | Titles added |
|------|-------------|
| 2015 | 82 |
| 2016 | 429 |
| 2017 | 1,188 |
| 2018 | 1,649 |
| **2019** | **2,016** ← peak |
| 2020 | 1,879 |
| 2021 | 1,498 |

**Interpretation:** Netflix aggressively expanded its catalogue from 2016–2019, coinciding with
its international roll-out to 130+ countries (January 2016). The slight dip in 2020–2021 likely
reflects COVID-19 production shutdowns and a strategic shift toward fewer, higher-budget originals.

---

## 3. Global production footprint

| Rank | Country | Titles |
|------|---------|--------|
| 1 | United States | 3,690 |
| 2 | India | 1,046 |
| 3 | United Kingdom | 806 |
| 4 | Canada | 445 |
| 5 | France | 393 |

**Interpretation:** India's strong #2 position is no accident — Netflix signed major deals with
Bollywood studios and regional language content creators from 2018 onwards, making South Asia
a key growth market.

---

## 4. Audience ratings

**TV-MA** (mature audiences) accounts for 36 % of the catalogue. Combined with **TV-14**
(a further 25 %), over 60 % of Netflix content is aimed at teen-and-above audiences.
Family-friendly ratings (TV-Y, TV-Y7, G, PG, TV-G) collectively represent only ~13 %.

This confirms Netflix's positioning as an adult-entertainment platform rather than a
family-first service.

---

## 5. Genre landscape

The top genre tag is **International Movies** (2,752 titles) — i.e. non-English-language
films — which confirms Netflix's investment in global content. Classic domestic genres
(Dramas, Comedies, Action & Adventure) follow closely.

---

## 6. Movie runtime distribution

- **Median:** ~99 minutes
- **Mean:** ~99 minutes (approximately symmetric distribution)
- **Peak bucket:** 90–120 minutes (the Hollywood standard)
- Very few movies exceed 150 minutes (~2 % of the movie catalogue)

The distribution is approximately normal with a slight right skew, typical of feature-film
catalogues worldwide.

---

## 7. Release year vs addition year

Most titles on Netflix were originally released between **2015–2019** — mirroring the window
in which Netflix rapidly expanded. Older content (pre-2010) makes up a small fraction,
suggesting Netflix licenses recent rather than archival titles.

---

## 8. Missing data

| Column | Missing % |
|--------|-----------|
| director | ~30 % |
| cast | ~10 % |
| country | ~8 % |
| date_added | ~0.1 % |
| rating | ~0.04 % |

The high director null rate is expected — TV shows often list no single director.
Country nulls mostly correspond to niche or unreported co-productions.

---

## Recommended next steps

- **Sentiment analysis** on descriptions to identify tonal trends by genre.
- **Time-series forecasting** of monthly additions.
- **Network analysis** of director–actor collaborations.
- **NLP topic modelling** on the `description` field.
