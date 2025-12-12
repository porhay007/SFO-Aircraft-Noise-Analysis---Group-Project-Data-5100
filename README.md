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

The dataset is obtained from Data.gov – San Francisco International Airport (SFO) Aircraft Noise Reports [San Francisco International Airport (SFO) Aircraft Noise Reports – Data.gov](https://catalog.data.gov/dataset/sfo-aircraft-noise-reports)
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

### 1. Data Cleaning & EDA (`Code/Data_cleaning.ipynb`)

- Filters noise reports to night-time hours (8 PM – 7 AM).
- Cleans missing or inconsistent data.
- Aggregates complaints by city, hour, operation type, and aircraft type.
- Visualizes complaint distribution by:
  - Neighborhood (`reporter_city`)
  - Aircraft type (`aircraft_type`)
  - Hour of night (`hour`)
  - Season of the year
  - Operation type (Arrival/Departure)

### 2. Predictive Modeling (`Code/Modeling.ipynb`)

- Joins US ZIP lat/lon and population data to compute distances to SFO and include population as a feature.
- Feature engineering includes:
  - Cyclical hour features (`hour_sin`, `hour_cos`)
  - Late-night indicator (`is_late_night`)
- Encodes categorical variables and transforms skewed complaint counts using `log1p`.
- Trains a **CatBoost Regressor** using 5-fold cross-validation.
- Evaluates model performance:
  - Mean R²: 0.62
  - Mean MAE: 56
- Performs scenario analysis (e.g., increasing aircraft altitude by 1000–5000 ft) to estimate potential reductions in complaints by neighborhood.

**Results:**

- The model identifies the neighborhoods most affected by night-time aircraft noise.

- Scenario analysis shows that increasing aircraft altitude reduces the number of predicted complaints, with Santa Cruz, Palo Alto, and Portola Valley experiencing the largest decreases.

- Feature importance indicates that altitude, distance to SFO, and operation type are key drivers of complaints.

**Authors:**
Porhay Rouen - @porhayrouen
Muykhim Ing - @MuykhimIng

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgements:**

- Python libraries: pandas, numpy, seaborn, matplotlib, scikit-learn, CatBoost

- Tutorials and Kaggle datasets used for SFO noise data

- Inspiration from local environmental data research
