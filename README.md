# 🚀 Serverless Data Engineering Pipeline for Event Analytics

## 📌 Overview
This project implements an end-to-end serverless data engineering pipeline on AWS to process, transform, and analyze event management data. The system ingests raw CSV files, performs ETL operations, and delivers actionable insights through interactive dashboards.

---

## 🎯 Problem Statement
Event data is often managed using traditional methods, leading to:
- Data fragmentation across multiple CSV files
- Inconsistent formats and poor data quality
- Manual and time-consuming data processing
- Difficulty in generating meaningful insights

---

## 💡 Solution
A serverless ETL pipeline was built using AWS services to:
- Centralize data in a data lake
- Automate data cleaning and transformation
- Enable fast querying using SQL
- Provide visualization-ready datasets

---

## 🏗️ Architecture

Raw CSV Data  
↓  
Amazon S3 (Raw Layer)  
↓  
AWS Glue Crawler (Schema Detection)  
↓  
AWS Glue ETL Jobs (Data Cleaning & Transformation)  
↓  
Amazon S3 (Processed Layer)  
↓  
AWS Glue Crawler (Updated Schema)  
↓  
Amazon Athena (SQL Queries)  
↓  
Exported CSV  
↓  
Tableau Dashboard  

---

## ⚙️ Tech Stack

- Amazon S3 – Data lake storage (raw and processed data)  
- AWS Glue – ETL processing and transformation  
- AWS Glue Crawler – Automatic schema detection  
- Amazon Athena – SQL-based querying  
- Tableau – Data visualization and dashboards  

---

## 📂 Project Structure

DEA_Event_Analytics/  
│  
├── data/  
│   ├── raw/  
│   └── processed/  
│  
├── queries/  
│   ├── revenue_queries.sql  
│   ├── sponsorship_queries.sql  
│  
├── dashboards/  
│   ├── dashboard.png  
│  
├── architecture/  
│   ├── architecture_diagram.png  
│  
├── screenshots/  
│   ├── s3.png  
│   ├── glue.png  
│   ├── athena.png  
│  
├── docs/  
│   ├── project_report.pdf  
│  
└── README.md  

---

## 📊 Datasets Used

### attendance.csv
Tracks student attendance for events with timestamps and event mapping.

### events.csv
Contains event details such as event name, date, location, and type.

### registrations.csv
Links students to events and tracks registration status.

### sponsors.csv
Contains sponsor details including contribution amounts.

---

## 🔄 Data Transformation Steps

- Removed extra headers and inconsistencies  
- Standardized column names  
- Handled missing/null values  
- Converted data types  
- Performed aggregations and joins  
- Prepared datasets for analytics  

---

## 📈 Sample SQL Queries

### Revenue per Event
SELECT event_name, SUM(payment_amount) AS total_revenue  
FROM processed_registrations  
GROUP BY event_name  
ORDER BY total_revenue DESC;  

### Sponsor Contribution
SELECT sponsor_name, SUM(sponsorship_amount) AS total_contribution  
FROM sponsors_clean  
GROUP BY sponsor_name;  

### Participation Analysis
SELECT event_name, COUNT(*) AS participants  
FROM attendance_clean  
GROUP BY event_name;  

---

## 📊 Dashboard Features

- Revenue per Event Analysis  
- Sponsorship Contribution Breakdown  
- Event Performance (Participants vs Revenue)  
- Financial Summary Insights  

---

## 🔍 Key Insights

- High participation events generate higher revenue  
- Sponsorship contributes significantly to total revenue  
- Some events have high revenue per participant  
- Data-driven insights improve decision-making  

---

## ⚡ Results

- Clean and structured dataset created  
- Faster querying using Athena  
- Multiple datasets optimized for visualization  
- Improved analytics and reporting capabilities  

---

## 🚀 Future Enhancements

- Real-time data ingestion using AWS Kinesis  
- Machine learning for predictive analytics  
- Fully automated pipeline using triggers  
- Live dashboards with streaming data  

---

## 🔐 Security (IAM Usage)

IAM roles were used to provide secure access:
- AWS Glue → Access to S3 data  
- Athena → Query execution permissions  

---

## 🧠 Key Concepts Demonstrated

- Data Lake Architecture  
- ETL Pipeline Design  
- Serverless Computing  
- SQL-based Analytics  
- Data Visualization  

---

## 📸 Screenshots

Add screenshots of:
- S3 Buckets  
- Glue Jobs  
- Athena Queries  
- Tableau Dashboard  

---

## 🏁 Conclusion

This project demonstrates a scalable, cost-effective, and automated data engineering pipeline using AWS, enabling efficient data processing and actionable insights for event analytics.

---

## ⭐ Acknowledgement

This project was developed as part of academic coursework in Data Engineering and Analytics.
