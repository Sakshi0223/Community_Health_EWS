import pandas as pd
import numpy as np
from datetime import datetime

# Generate 30 days of sample village health data
villages = ['Mawlynnong', 'Cherrapunji', 'Dawki', 'Shillong Rural', 'Tura']

dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
data = []

for village in villages:
    for date in dates:
        # Simulate monsoon spike in symptoms
        is_monsoon = date.month in [6, 7, 8, 9]
        base_rate = 10 if is_monsoon else 3

        data.append({
            'State': 'Meghalaya',
            'District': 'East Khasi Hills',
            'Village': village,
            'Date': date.strftime('%Y-%m-%d'),
            'Diarrhea': np.random.poisson(base_rate),
            'Fever': np.random.poisson(base_rate + 2),
            'Vomiting': np.random.poisson(base_rate - 1),
            'Water_Status': np.random.choice(['Safe', 'Contaminated', 'Unknown']),
            'Flood_Flag': 1 if is_monsoon and np.random.rand() > 0.7 else 0,
            'Population': 500
        })

df = pd.DataFrame(data)

output_path = "/content/drive/MyDrive/Community_Health_EWS/data/raw/health_data_sample.csv"
df.to_csv(output_path, index=False)

print("✅ Sample data generated and saved to:", output_path)
