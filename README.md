# US Accidents Data Dashboard

An interactive web dashboard for analyzing US traffic accident data, built with Streamlit and Plotly.

## Overview

This project provides a multi-page dashboard to explore patterns in traffic accidents across the United States. Users can filter by state and navigate through four analysis sections.

## Pages

- **Overview** — Total accident count, affected states, year-over-year trend, and top 20 states by accident volume.
- **State Analysis** — Per-state breakdown of severity distribution and top cities by accident count.
- **Time Analysis** — Accident patterns by hour of day, day of week, and month of year.
- **Weather Analysis** — Top weather conditions linked to accidents and weather vs. severity breakdown.

## Tech Stack

- Python 3.x
- Streamlit
- Pandas
- Plotly Express

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/KRISH2507/US_Dataset.git
   cd US_Dataset
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install streamlit pandas plotly
   ```

4. Run the app:
   ```
   streamlit run app.py
   ```

## Dataset

Place `US_Accidents.csv` inside the `data/` folder. The CSV must include columns: `Start_Time`, `State`, `City`, `Severity`, `Weather_Condition`.

## Project Structure

```
US_Dataset/
├── app.py
├── data/
│   └── US_Accidents.csv
├── Krish_Squad84_US_Accidents_Dataset.ipynb
└── README.md
```
