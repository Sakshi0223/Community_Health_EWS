import pandas as pd
import numpy as np
import glob
import os

def clean_data(df):
    """
    Clean and normalize health data
    """

    # Remove duplicate village-date entries
    df = df.drop_duplicates(subset=['Village', 'Date'])

    # Handle missing values safely
    if 'Water_Status' in df.columns:
        df['Water_Status'] = df['Water_Status'].fillna('Unknown')

    if 'Flood_Flag' in df.columns:
        df['Flood_Flag'] = df['Flood_Flag'].fillna(0)

    # Normalize symptom counts per 1000 population
    if 'Population' in df.columns:
        df['Diarrhea_Rate'] = (df['Diarrhea'] / df['Population']) * 1000
        df['Fever_Rate'] = (df['Fever'] / df['Population']) * 1000

    # Add seasonal indicators
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Is_Monsoon'] = df['Month'].isin([6, 7, 8, 9]).astype(int)

    return df


# Run test only when executed directly
if __name__ == "__main__":

    # Get latest processed file automatically
    processed_files = sorted(glob.glob("data/processed/health_data_*.csv"))

    if not processed_files:
        raise FileNotFoundError("❌ No processed data found. Run data_ingestion.py first.")

    latest_file = processed_files[-1]
    df = pd.read_csv(latest_file)

    df_clean = clean_data(df)

    os.makedirs("data/processed", exist_ok=True)
    output_path = "data/processed/health_data_clean.csv"
    df_clean.to_csv(output_path, index=False)

    print(f"✅ Data cleaned and saved to → {output_path}")
