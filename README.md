# E-Commerce-Order-Data-Pipeline-
<!-- README: Data Pipeline Architecture -->
<div align="center">

```mermaid
flowchart TD
    classDef python fill:#306998,stroke:#fff,color:#fff
    classDef csv fill:#f0f0f0,stroke:#999,color:#333
    classDef snowflake fill:#29B5E8,stroke:#fff,color:#fff
    classDef dbt fill:#FF694B,stroke:#fff,color:#fff
    classDef airflow fill:#017CEE,stroke:#fff,color:#fff

    A[🐍 Dummy Data Creation<br/><small>Python script</small>]:::python
    B1[customers.csv]:::csv
    B2[orders.csv]:::csv
    B3[shipments.csv]:::csv
    C[Snowflake: RAW Schema<br/><small>orders, customers, shipments tables</small>]:::snowflake
    D[dbt<br/><small>Transformation using dbt</small>]:::dbt
    E[Snowflake: ANALYTICS Schema<br/><small>via dbt: order_status view,<br/>transformed models</small>]:::snowflake
    F[Apache Airflow DAG<br/><small>• Runs dbt hourly<br/>• Sends Email Alert if shipped > 48 hrs</small>]:::airflow

    A --> B1 & B2 & B3
    B1 & B2 & B3 --> C
    C --> D
    D --> E
    E --> F
    F -->|triggers| D

    click A href "https://github.com/your-repo/blob/main/scripts/create_dummy.py"
    click F href "https://github.com/your-repo/blob/main/dags/shipments_alert_dag.py"
