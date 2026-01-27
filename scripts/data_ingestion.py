import pandas as pd
from datetime import datetime
import os

def ingest_health_data(csv_path):
    """Load and validate health data"""
    df = pd.read_csv(csv_path)
    
    # Validate required columns
    required_cols = ['State', 'District', 'Village', 'Date', 
                     'Diarrhea', 'Fever', 'Vomiting']
    missing = [col for col in required_cols if col not in df.columns]
    
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    # Convert date to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Save to processed folder
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = f'data/processed/health_data_{timestamp}.csv'
    df.to_csv(output_path, index=False)
    
    print(f"✅ Ingested {len(df)} records → {output_path}")
    return df

# Test it
if __name__ == "__main__":
    df = ingest_health_data('data/raw/health_data_sample.csv')
    print(df.head())