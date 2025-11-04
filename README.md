# E-Commerce-Order-Data-Pipeline-with-Delayed-Orders-Alert
##  Data Pipeline System Design

This project demonstrates an end-to-end **data pipeline** using **Python**, **Snowflake**, **dbt**, and **Apache Airflow**.  
The system generates dummy data, loads it into Snowflake, transforms it using dbt, and automates execution and alerting using Airflow.

---

##  System Architecture

<p align="center">
  <img src="./assets/system_design.png" alt="System Design Flowchart" width="700"/>
</p>

---

##  Workflow Overview

1. **Data Generation (Python)**  
   - Python script creates dummy datasets:  
     - `customers.csv`  
     - `orders.csv`  
     - `shipments.csv`

2. **Data Loading (Snowflake RAW Schema)**  
   - These CSVs are loaded into Snowflake under the **RAW schema**.  
   - Tables: `customers`, `orders`, `shipments`.

3. **Data Transformation (dbt)**  
   - dbt transforms raw data into clean, analytical models.  
   - Output stored in **Snowflake ANALYTICS schema**.  
   - Includes transformed views like `order_status`.

4. **Automation (Apache Airflow)**  
   - Airflow DAG runs dbt transformations hourly.  
   - Sends email alerts if any shipment is delayed by more than **48 hours**.

---

##  Tech Stack

| Component        | Tool / Technology |
|------------------|------------------|
| Data Creation    | Python |
| Data Warehouse   | Snowflake |
| Data Transformation | dbt |
| Orchestration & Alerts | Apache Airflow |

---

##  How to Run

1. Generate dummy CSVs using the Python script.
2. Load data into Snowflake (RAW schema).
3. Run dbt models for transformation.
4. Trigger Airflow DAG to automate checks & alerts.

---

📌 *Designed for showcasing modern data engineering workflow integration.*
