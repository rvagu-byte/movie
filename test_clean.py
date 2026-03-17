"""
main.py
-------
Run the complete Netflix EDA pipeline.

Usage
-----
    python main.py                          # uses default data path
    python main.py --data path/to/data.csv  # custom data path
    python main.py --no-show                # skip interactive display
"""

from __future__ import annotations

import argparse
import os
import sys

import matplotlib.pyplot as plt

from src.load import load_data, dataset_summary
from src.clean import clean_data
from src.analyse import print_summary_stats
from src.visualise import (
    plot_content_type,
    plot_titles_added,
    plot_top_countries,
    plot_ratings,
    plot_top_genres,
    plot_duration_histogram,
    plot_release_year_trend,
    plot_dashboard,
)

DEFAULT_DATA_PATH = os.path.join("data", "netflix_titles.csv")
DEFAULT_OUTPUT_DIR = os.path.join("outputs", "plots")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Netflix EDA pipeline")
    parser.add_argument(
        "--data",
        default=DEFAULT_DATA_PATH,
        help=f"Path to the CSV dataset (default: {DEFAULT_DATA_PATH})",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory for saved plots (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Do not display interactive plot windows",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print("\n Netflix EDA Pipeline")
    print(" " + "─" * 40)

    # ── 1. Load ───────────────────────────────────────────────────────────────
    print("\n[1/4] Loading data …")
    df_raw = load_data(args.data)
    dataset_summary(df_raw)

    # ── 2. Clean ──────────────────────────────────────────────────────────────
    print("\n[2/4] Cleaning data …")
    df = clean_data(df_raw)
    print(f"  Added columns : year_added, month_added, duration_int")

    # ── 3. Analyse ────────────────────────────────────────────────────────────
    print("\n[3/4] Running analysis …")
    print_summary_stats(df)

    # ── 4. Visualise ──────────────────────────────────────────────────────────
    print(f"\n[4/4] Generating plots → {args.output}")
    out = args.output

    plot_dashboard(df, output_dir=out)
    plot_content_type(df, output_dir=out)
    plot_titles_added(df, output_dir=out)
    plot_top_countries(df, output_dir=out)
    plot_ratings(df, output_dir=out)
    plot_top_genres(df, output_dir=out)
    plot_duration_histogram(df, output_dir=out)
    plot_release_year_trend(df, output_dir=out)

    print("\n Done! All plots saved.\n")

    if not args.no_show:
        plt.show()


if __name__ == "__main__":
    main()
