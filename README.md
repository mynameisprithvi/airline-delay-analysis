# Airline Departure Delay Analysis (EDA + Statistics)

## Objective
This project was completed as part of a structured data analysis coursework and focuses on
foundational exploratory analysis techniques applied to airline departure delay data. The
analysis explores how delays vary across airlines and seasons, with an emphasis on identifying
systematic patterns and validating observations statistically rather than predicting individual
flight delays.

### Data Availability
The raw and processed datasets (~800MB) are not included in this repository due to size
constraints. They are available for reference via Google Drive:

[Google Drive link: https://drive.google.com/drive/folders/1xn9mnF0doqKMbutwo-MwALw35Q3lQ3i5?usp=drive_link ]

All preprocessing steps are documented in the repository scripts.


## Key Questions
- Do average departure delays differ across airlines?
- Is there a seasonal pattern in departure delays across months?
- Are airline-specific effects stronger than seasonal effects?

## Dataset
The dataset contains flight-level information including airline identifiers, departure delay
times, and temporal features such as month. The data is observational and does not include
controls for airport, route, or weather conditions.

## Methodology
- Exploratory Data Analysis (EDA) using aggregation and visualization
- Airline-level and month-level comparisons of mean departure delays
- Heatmap analysis of airline × month delay patterns
- One-way ANOVA to statistically test whether mean delays differ across airlines

## Key Findings
- Mean departure delays vary significantly across airlines, indicating systematic operational
  differences.
- Departure delays exhibit clear seasonality, with higher average delays during winter months.
- Airline identity appears to contribute more to delay variability than month-to-month seasonality.
- A one-way ANOVA confirms statistically significant differences in mean delays across airlines
  (p < 0.001), supporting the observed visual patterns.

## Limitations
- The analysis is observational and does not imply causality.
- Important factors such as airport congestion, route structure, weather, and time of day
  are not controlled for.
- Results should be interpreted as descriptive patterns rather than performance rankings.

## Project Structure

- notebooks/
  - airline_delay_eda_and_stats.ipynb
- scripts/
  - data_loading.py
  - preprocessing.py
- data/
  - raw/
  - processed/
- README.md


## Tools Used
- Python
- pandas, NumPy
- matplotlib, seaborn
- SciPy (statistical testing)

## Status
Complete. This project focuses on exploratory analysis and statistical validation rather than
predictive modeling.




