from apscheduler.schedulers.blocking import BlockingScheduler
import pandas as pd
import sys
import os

# Allow imports from scripts folder
sys.path.append(os.path.dirname(__file__))

from data_ingestion import ingest_health_data
from data_cleaning import clean_data

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', minutes=1)  # FOR TESTING (every 1 min)
def daily_data_update():
    print("🔄 Running scheduled data update...")

    df = ingest_health_data("data/raw/health_data_sample.csv")
    df_clean = clean_data(df)

    df_clean.to_csv("data/processed/latest_clean_data.csv", index=False)

    print("✅ Scheduled update completed!")


if __name__ == "__main__":
    print("📅 Scheduler started (test mode). Press Ctrl+C to stop.")
    scheduler.start()
