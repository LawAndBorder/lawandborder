# Law and Border

## Setup

0. Install the `zgulde` library

    ```
    pip install --upgrade zgulde
    ```

1. Download [the border crossing entry data here](https://data.transportation.gov/Research-and-Statistics/Border-Crossing-Entry-Data/keg4-3bc2/data).

2. Save the file as `data.csv`

3. Use the `acquire.py` script to get the data

    ```python
    import acquire

    canada_df, mexico_df = acquire.get_data()
    ```

## Primary Goals of this Project

- Deliver Time Series models and a complete project by the end of the day
- Predict the number of crossings by method by port for next year

## Minimum Viable Product

- End to end analysis including:
    - Exploration and model border crossings by crossing method by port to predict future crossings.
    - Time series analysis of crossings by method by port

## Project Planning First Steps

- Pull in the data from https://data.transportation.gov/Research-and-Statistics/Border-Crossing-Entry-Data/keg4-3bc2/data
- Define our goals of analysis
- Define what each observation (each row) contains
- Define what kinds of models we can or should produce.

## Need to haves

- Reproduceable acquire and prepare Python scripts
- Testable hypotheses
- Exploratory data analysis
- Time Series Analysis with a model for each

## Nice to Haves (if we have time)

- Multivariate Time Series Analysis Model
- Maggies Method for Time Series Anomaly Detection and "doing time series without the time"

## Thoughts

- Each observation (each) creates its own time series model

## Data Acquisition

- split by country so we have a Canada and Mexico dataset
- split by crossing method

## Data Preparation

## Exploratory Data Analysis

- Cluster by crossing_type and number of crossings `n_crossings`.
