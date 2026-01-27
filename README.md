# 🏥 Smart Community Health Monitoring & Early Warning System

## 📍 Focus Area
Rural Northeast India (Assam, Meghalaya, Tripura)

## 🧩 Problem Statement
Water-borne diseases such as diarrhea, fever, and vomiting are common in rural Northeast India, especially during monsoon and flood seasons. Due to limited infrastructure and delayed reporting, outbreaks are often detected late, leading to increased health risks.

This project proposes a **software-only, data-driven early warning system** that collects community-level health and water-condition data and provides early outbreak risk indicators.

---

## 🎯 Phase 1 Objective
The objective of **Phase 1** is to build a **cloud-based data infrastructure** that can:

- Collect daily health and water-condition data
- Validate, clean, and normalize the data
- Store processed data systematically
- Automate daily data ingestion using scheduling

---

## 📊 Data Sources (Phase 1 – Simulated)
Since real-world data collection takes time, **synthetic sample data** was generated for Phase 1.

### Sample Data Includes:
- State, District, Village
- Date
- Diarrhea, Fever, Vomiting counts
- Water status (Safe / Contaminated / Unknown)
- Flood indicator
- Population

Sample data represents **5 rural villages over 30 days**.

---

## 🔄 Phase 1 Workflow

1. **Sample Data Generation**
   - `generate_sample_data.py` creates synthetic rural health data

2. **Data Ingestion**
   - `data_ingestion.py` validates and stores data in processed format

3. **Data Cleaning & Normalization**
   - `data_cleaning.py` removes duplicates, handles missing values, normalizes symptom rates

4. **Automation**
   - `scheduler.py` runs daily ingestion and cleaning automatically using APScheduler

---

## ▶️ How to Run Phase 1 (Google Colab)

### Step 1: Install dependencies
```bash
pip install -r requirements.txt
