# Aircraft Noise Impact Analysis Near San Francisco International Airport (SFO)

## Project Overview

- Objective

To analyze and predict aircraft noise complaints near San Francisco International Airport (SFO) in order to understand which neighborhoods are most affected and identify key factors contributing to night-time disturbances.

- Domain

Environmental Data Analysis / Transportation

- Problem Statement

Communities living under busy flight paths near SFO experience frequent aircraft noise, especially at night, which impacts their sleep and overall well-being. This project aims to investigate which neighborhoods report the most night-time complaints (8 PM – 7 AM) and how factors like aircraft type, altitude, operation type, and runway contribute to these patterns.

## Project Structure

```text
project-root/
├── data/                 # Raw and processed data
│   ├── Aircraft_Noise_Reports.csv
│   ├── Cleaned_Aircraft_Noise_Night_SFO.csv
│   └── uszips.csv
├── code/                 # Jupyter notebooks and scripts
│   ├── SFO_Aircraf_Noise_Complaint.ipynb
├── reports/              # Generated visualizations
│   └── Sample.pdf
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

```

## Data

**Source:**

The dataset is obtained from Data.gov – San Francisco International Airport (SFO) Aircraft Noise Reports [San Francisco International Airport (SFO) Aircraft Noise Reports – Data.gov](https://catalog.data.gov/dataset/aircraft-noise-reports)
.
It contains publicly available data collected by the San Francisco International Airport Noise Office from 2018 to the present.

**Description:**  
This dataset records aircraft noise complaints made by residents living near SFO flight paths.
For this project, the following columns were used:

- disturbance_date_time : Date and time when the noise disturbance occurred
- reporter_city : City of the person who reported the complaint
- reporter_postal_code : Postal code of the complainant’s address
- aircraft_pca_altitude : Altitude of the aircraft during the disturbance
- airport_id : Identifier of the airport (e.g., SFO)
- operation_type : Type of operation (Arrival or Departure)
- aircraft_type : Aircraft model/type (e.g., Boeing 737, Airbus A320)
- hour : Extracted hour of disturbance, used for night-time analysis (8 PM – 7 AM)

**Additional Data:**

To enhance predictive modeling, we incorporated US ZIP code data containing latitude, longitude, and population information. By joining this dataset with the noise complaints using the reporter’s postal code, we were able to:

- Compute the distance from each neighborhood to San Francisco International Airport (SFO), allowing the model to account for proximity effects on complaint frequency.

- Include population as a feature, providing context for neighborhood size and potential complaint density.

Fields used from the ZIP code dataset:

- zip : Postal code of the area

- lat : Latitude of the ZIP code centroid

- lng : Longitude of the ZIP code centroid

- population : Total population of the ZIP code area

Source: [US Zip Code Database – SimpleMaps](https://simplemaps.com/data/us-zips)

**License:**  
Open Data Commons Public Domain Dedication and License (PDDL)

**Analysis:**

The analysis is split into two main parts:

### 1. Data Cleaning & EDA (`Code/SFO_Aircraf_Noise_Complaint.ipynb`)

- Filters complaints to night-time hours (8 PM – 7 AM)
- Cleans missing or inconsistent data and removes duplicates
- Aggregates complaints by city, hour, operation type, and aircraft type
- Visualizes distribution of complaints:
  - By neighborhood (reporter_city) – top and least affected
  - By aircraft type – highest and lowest complaint-generating types
  - By hour of night – peak and lowest complaint hours 
  - By season – Winter, Spring, Summer, Fall
  - By operation type – Arrivals vs Departures (Arrivals account for 88.7% of complaints)

### 2. Predictive Modeling (`Code/Modeling.ipynb`)

- Joins US ZIP lat/lon and population data to compute distances to SFO and include population as a feature.
- Feature engineering includes:
  - Cyclical hour features (`hour_sin`, `hour_cos`)
  - Late-night indicator (`is_late_night`)
- Encodes categorical variables and transforms skewed complaint counts using `log1p`.
- Trains a **CatBoost Regressor** using 5-fold cross-validation.
- Evaluates model performance:
  - Mean R²: 0.5896
  - Mean MAE: 57.95
- Scenario analysis: increasing aircraft altitude by 1,000 ft reduces predicted complaints, especially in Santa Cruz, Palo Alto, and Portola Valley
- Key drivers of complaints: altitude, distance to SFO, operation type

**Results:**

- Most affected neighborhoods: Palo Alto, Portola Valley, Santa Cruz, Los Altos
- Time patterns: Complaints peak at 8–9 PM and 6–7 AM, lowest between 2–4 AM
- Operation type: Arrivals are the primary source of complaints (88.7%)
- Aircraft type: A few large commercial jets generate most complaints; smaller aircraft contribute minimally
- Mitigation insights: Increasing aircraft altitude by 1,000 ft can meaningfully reduce complaints, with largest benefits for neighborhoods directly under flight paths

**Authors:**
Porhay Rouen - @porhayrouen
Muykhim Ing - @MuykhimIng

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgements:**

- **Python libraries**: pandas, numpy, seaborn, matplotlib, scikit-learn, CatBoost

- **Data Sources**: Primary noise complaint data was obtained from Data.gov – SFO Aircraft Noise Reports and additional ZIP code data (latitude, longitude, population) was sourced from SimpleMaps.

- **Inspiration and guidance**: This project was inspired by and developed using tutorials and examples from the DATA-5100 course materials by **Dr. Brian Fischer**.
