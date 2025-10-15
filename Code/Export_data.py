import pandas as pd

# ✅ Use the correct full path if relative path doesn't work
file_path = '/Users/macbookpro/Desktop/Group_Project/Aircraft_Noise_Reports.csv'

# Read large CSV file
data_frame = pd.read_csv(file_path, low_memory=False)

# ✅ Convert disturbance_date_time to datetime (handles AM/PM)
data_frame['disturbance_date_time'] = pd.to_datetime(
    data_frame['disturbance_date_time'], 
    format='%Y/%m/%d %I:%M:%S %p',
    errors='coerce'
)

# ✅ Filter between Jan 1 and Jan 10, 2025
start_date = '2025-01-01'
end_date = '2025-01-10'
filtered_df = data_frame[
    (data_frame['disturbance_date_time'] >= start_date) &
    (data_frame['disturbance_date_time'] <= end_date)
]

# ✅ Save to new file
output_path = '/Users/macbookpro/Desktop/Group_Project/Aircraft_Noise_Clean_Report.csv'
filtered_df.to_csv(output_path, index=False)

print("✅ Done! Filtered data saved to Aircraft_Noise_Clean_Report.csv")



