# E-Commerce-Order-Data-Pipeline-
<!-- E-Commerce Order Pipeline with Delayed Orders Alerting -->
<div align="center">

```mermaid
flowchart TD
    %% === Colours & Icons ===
    classDef python   fill:#306998,stroke:#fff,color:#fff
    classDef csv      fill:#fff,stroke:#666,color:#333
    classDef snow     fill:#29B5E8,stroke:#fff,color:#fff
    classDef dbt      fill:#FF694B,stroke:#fff,color:#fff
    classDef airflow  fill:#017CEE,stroke:#fff,color:#fff

    %% === Nodes ===
    A[ Dummy Data Creation<br/><small>Python script</small>]:::python

    B1[customers.csv]:::csv
    B2[orders.csv]:::csv
    B3[shipments.csv]:::csv

    C[Snowflake: RAW Schema<br/><small>orders, customers, shipments tables</small>]:::snow

    D[dbt<br/><small>Transformation using dbt</small>]:::dbt

    E[Snowflake: ANALYTICS Schema<br/><small>via dbt: order_status view,<br/>transformed models</small>]:::snow

    F[Apache Airflow DAG<br/><small>• Runs dbt hourly<br/>• Sends Email Alert if<br/> shipped > 48 hrs</small>]:::airflow

    %% === Flow ===
    A --> B1 & B2 & B3
    B1 & B2 & B3 --> C
    C --> D
    D --> E
    E --> F
    F -->|triggers hourly| D

    %% === Clickable Links (auto-point to your repo) ===
    click A   href "https://github.com/nyasa10/E-Commerce-Order-Data-Pipeline-with-Delayed-Orders-Alerting/blob/main/scripts/create_dummy.py"   "View dummy data script"
    click F   href "https://github.com/nyasa10/E-Commerce-Order-Data-Pipeline-with-Delayed-Orders-Alerting/blob/main/dags/shipment_alert_dag.py" "View Airflow DAG"

