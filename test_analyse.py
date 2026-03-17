{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Netflix Titles — EDA Walkthrough\n",
    "\n",
    "This notebook walks through the full EDA pipeline interactively.\n",
    "Run cells top-to-bottom after running `pip install -r requirements.txt`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys, os\n",
    "sys.path.insert(0, os.path.abspath('..'))\n",
    "\n",
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt\n",
    "plt.rcParams['figure.dpi'] = 110"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Load & validate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from src.load import load_data, dataset_summary\n",
    "\n",
    "df_raw = load_data('../data/netflix_titles.csv')\n",
    "dataset_summary(df_raw)\n",
    "df_raw.head(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Clean & feature-engineer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from src.clean import clean_data\n",
    "\n",
    "df = clean_data(df_raw)\n",
    "print('New columns:', [c for c in df.columns if c not in df_raw.columns])\n",
    "df[['title','type','year_added','month_added','duration_int']].head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Summary statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from src.analyse import print_summary_stats\n",
    "print_summary_stats(df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Visualisations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from src.visualise import plot_dashboard\n",
    "fig = plot_dashboard(df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from src.visualise import plot_content_type, plot_titles_added\n",
    "plot_content_type(df)\n",
    "plot_titles_added(df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from src.visualise import plot_top_countries, plot_ratings\n",
    "plot_top_countries(df)\n",
    "plot_ratings(df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from src.visualise import plot_top_genres, plot_duration_histogram, plot_release_year_trend\n",
    "plot_top_genres(df)\n",
    "plot_duration_histogram(df)\n",
    "plot_release_year_trend(df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Ad-hoc exploration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Movies vs TV Shows added over time\n",
    "import pandas as pd\n",
    "pivot = (\n",
    "    df.dropna(subset=['year_added'])\n",
    "    .groupby(['year_added', 'type'])\n",
    "    .size()\n",
    "    .unstack(fill_value=0)\n",
    ")\n",
    "pivot[pivot.index >= 2015].plot(kind='bar', figsize=(10, 4), color=['#3266ad','#1d9e75'])\n",
    "plt.title('Movies vs TV Shows Added per Year')\n",
    "plt.xticks(rotation=35)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Top 5 countries breakdown by type\n",
    "from src.clean import explode_countries\n",
    "\n",
    "top5 = ['United States', 'India', 'United Kingdom', 'Canada', 'France']\n",
    "country_df = explode_countries(df)\n",
    "filtered = country_df[country_df['country'].isin(top5)]\n",
    "pivot2 = filtered.groupby(['country', 'type']).size().unstack(fill_value=0)\n",
    "pivot2.loc[top5].plot(kind='barh', figsize=(8, 4), color=['#3266ad','#1d9e75'])\n",
    "plt.title('Movies vs TV Shows — Top 5 Countries')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
