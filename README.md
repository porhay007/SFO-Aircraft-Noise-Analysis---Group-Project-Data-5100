# Aircraft Noise Impact Analysis Near San Francisco International Airport (SFO)

## Project Overview
+ Objective

To analyze and predict aircraft noise complaints near San Francisco International Airport (SFO) in order to understand which neighborhoods are most affected and identify key factors contributing to night-time disturbances.

+ Domain

Environmental Data Analysis / Transportation

+ Problem Statement

Communities living under busy flight paths near SFO experience frequent aircraft noise, especially at night, which impacts their sleep and overall well-being. This project aims to investigate which neighborhoods report the most night-time complaints (8 PM – 7 AM) and how factors like aircraft type, altitude, operation type, and runway contribute to these patterns.

## Project Structure

├── data/                 # Raw and processed data
├── code/                 # Jupyter notebooks and Python scripts
├── reports/              # Generated reports and visualizations
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

## Data

**Source:** 

The dataset is obtained from Data.gov – San Francisco International Airport (SFO) Aircraft Noise Reports [San Francisco International Airport (SFO) Aircraft Noise Reports – Data.gov](https://catalog.data.gov/dataset/sfo-aircraft-noise-reports)
.
It contains publicly available data collected by the San Francisco International Airport Noise Office from 2018 to the present.

**Description:**  
This dataset records aircraft noise complaints made by residents living near SFO flight paths.
For this project, the following columns were used:

- disturbance_date_time      : Date and time when the noise disturbance occurred
- reporter_city              : City of the person who reported the complaint
- reporter_postal_code       : Postal code of the complainant’s address
- aircraft_pca_altitude      : Altitude of the aircraft during the disturbance
- airport_id                 : Identifier of the airport (e.g., SFO)
- operation_type             : Type of operation (Arrival or Departure)
- aircraft_type              : Aircraft model/type (e.g., Boeing 737, Airbus A320)
- hour                       : Extracted hour of disturbance, used for night-time analysis (8 PM – 7 AM)

**Access:**

Due to GitHub’s file size limitations, only a sample file (/data/sample_aircraft_noise.csv) containing 100 records is included in this repository for demonstration purposes.
The full cleaned dataset is publicly available on Kaggle:
👉 Aircraft Noise Report SFO – Kaggle

**License:**  
Open Data Commons Public Domain Dedication and License (PDDL)






**Analysis:**
Describe the notebooks and/or scripts used to perform the analysis. Specify the order in which the code should be run to reproduce the results.

**Results:**
Include a short discussion of the findings and what they imply.

**Authors:**
Your Name - @yourhandle
License
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgements:**
Tools/libraries used
Tutorials or papers referenced
Inspiration or collaborators