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

+ Source

The dataset is obtained from Data.gov – San Francisco International Airport (SFO) Aircraft Noise Reports
.
It contains publicly available data collected by the San Francisco International Airport Noise Office from 2018 to the present.

+ Columns Used:
- disturbance_date_time  
- reporter_city  
- reporter_postal_code  
- aircraft_pca_altitude  
- airport_id  
- operation_type  
- aircraft_type  
- hour  

**Description:**  
This dataset includes noise complaint records reported by residents near SFO.  
The selected columns help analyze complaint patterns by location, time, and flight characteristics.

**License:**  
Open Data Commons Public Domain Dedication and License (PDDL)






Analysis
Describe the notebooks and/or scripts used to perform the analysis. Specify the order in which the code should be run to reproduce the results.

Results
Include a short discussion of the findings and what they imply.

Authors
Your Name - @yourhandle
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Tools/libraries used
Tutorials or papers referenced
Inspiration or collaborators