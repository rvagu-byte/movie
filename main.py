"""
src/clean.py
------------
Data cleaning and feature engineering for the Netflix dataset.
"""

from __future__ import annotations

import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the raw DataFrame.

    Steps performed
    ---------------
    1. Strip leading/trailing whitespace from all string columns.
    2. Parse ``date_added`` to datetime.
    3. Extract ``year_added`` and ``month_added`` from ``date_added``.
    4. Normalise the ``rating`` column (remove rows where rating looks
       like a duration, e.g. "74 min").
    5. Extract ``duration_int`` (numeric minutes for movies, numeric
       seasons for TV shows).

    Parameters
    ----------
    df : pd.DataFrame
        Raw DataFrame returned by :func:`src.load.load_data`.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with additional derived columns.
    """
    df = df.copy()

    # 1. Strip whitespace
    str_cols = df.select_dtypes(include="object").columns
    for col in str_cols:
        df[col] = df[col].str.strip()

    # 2. Parse date_added
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

    # 3. Derived time columns
    df["year_added"] = df["date_added"].dt.year.astype("Int64")
    df["month_added"] = df["date_added"].dt.month.astype("Int64")

    # 4. Fix bad rating values (e.g. "74 min" misplaced from duration)
    valid_ratings = {
        "G", "PG", "PG-13", "R", "NC-17", "NR", "UR",
        "TV-Y", "TV-Y7", "TV-Y7-FV", "TV-G", "TV-PG",
        "TV-14", "TV-MA",
    }
    df["rating"] = df["rating"].where(df["rating"].isin(valid_ratings), other=pd.NA)

    # 5. Numeric duration
    df["duration_int"] = _extract_duration_int(df)

    return df


def _extract_duration_int(df: pd.DataFrame) -> pd.Series:
    """Return integer duration (minutes for movies, seasons for TV shows)."""
    result = pd.Series(pd.NA, index=df.index, dtype="Int64")

    movie_mask = df["type"] == "Movie"
    tv_mask = df["type"] == "TV Show"

    result[movie_mask] = (
        df.loc[movie_mask, "duration"]
        .str.extract(r"(\d+)", expand=False)
        .astype("Int64")
    )
    result[tv_mask] = (
        df.loc[tv_mask, "duration"]
        .str.extract(r"(\d+)", expand=False)
        .astype("Int64")
    )
    return result


def explode_genres(df: pd.DataFrame) -> pd.DataFrame:
    """Return a long-format DataFrame with one genre per row.

    Useful for genre frequency analysis.
    """
    genres = (
        df[["show_id", "title", "type", "listed_in"]]
        .copy()
        .dropna(subset=["listed_in"])
    )
    genres["genre"] = genres["listed_in"].str.split(",")
    genres = genres.explode("genre")
    genres["genre"] = genres["genre"].str.strip()
    return genres.reset_index(drop=True)


def explode_countries(df: pd.DataFrame) -> pd.DataFrame:
    """Return a long-format DataFrame with one country per row."""
    countries = (
        df[["show_id", "title", "type", "country"]]
        .copy()
        .dropna(subset=["country"])
    )
    countries["country"] = countries["country"].str.split(",")
    countries = countries.explode("country")
    countries["country"] = countries["country"].str.strip()
    return countries.reset_index(drop=True)
