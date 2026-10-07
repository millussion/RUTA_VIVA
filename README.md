# RutaViva Mobility

Data platform for dynamic pricing and fleet operations (taxis and ride-hailing services).

> **Project 02 of 10 — Data Engineering / Cloud / Backend / Analytics**

---

## Project Description

**RutaViva Mobility** is a data engineering project focused on analyzing and processing data related to the operation of a fleet of approximately **8,000 vehicles**.

The goal is to build an **end-to-end** solution capable of integrating diverse data sources, processing large volumes of historical data, and ingesting operational data in near real-time.

The platform must enable the analysis of the relationship between **vehicle supply and demand**, the calculation of a **dynamic fare multiplier based on zone and time slot**, the identification of underserved areas, and the automatic generation of required regulatory reports.

The project has an estimated duration of **6 weeks** and is to be deployed on **AWS**, aiming for a solution that is both technically sound and cost-optimized.

---

## Problem

RutaViva currently uses a fixed fare structure based on zones that does not adequately respond to changes in:

- Passenger demand.
- Vehicle availability.
- Weather conditions.
- Special events.
- Operating hours.

This leads to several operational issues:

- Wait times can increase significantly during rainy days.
- Drivers remain idle during periods of low demand.
- Analysts require several hours to process large volumes of trip data.
- Erroneous data can skew key metrics.
- Regulatory reports may suffer from delays or errors.
- There is insufficient traceability regarding fare calculations.

The proposed system must primarily address the lack of visibility into the **demand vs. supply** relationship across different zones and time periods. ---

## Objectives

### Business objectives

The project aims to:

- Reduce average wait times during peak hours by **25%**.
- Increase vehicle utilization during off-peak hours by **15%**.
- Automatically generate the monthly regulatory report.
- Ensure that every fare can be audited and reconstructed.

These objectives require the system to retain sufficient information to identify the multiplier used and the conditions that led to that calculation.

---

## System actors

| Actor | Need |
|---|---|
| Operations Manager | Check supply, demand, and underserved zones |
| Passenger App | Check the current multiplier |
| Driver | Receive recommendations for zones with unmet demand |
| Transit Authority | Receive monthly reports |
| Internal Auditor | Reconstruct the fare calculation |



---

# Data sources

The system integrates various information sources.

| ID | Source | Type | Frequency |
|---|---|---|---|
| F1 | NYC Yellow Taxi Trip Data | CSV | Historical |
| F2 | TLC Taxi Zone Lookup | Public CSV | One-time |
| F3 | Historical weather and forecast | API | Hourly |
| F4 | GPS telemetry | Simulated stream | Every 15 seconds |
| F5 | Trip requests | Simulated API | Continuous |
| F6 | Driver registry | Simulated PostgreSQL | Daily |
| F7 | Special events | CSV | Weekly |

F1 must be processed over a minimum of **6 consecutive months** and presents schema changes across different years; therefore, one of the main challenges is data unification and standardization.

---

# Required technologies and topics

The project must demonstrate the use of the key topics covered during the program. ### Backend

- FastAPI
- REST API
- OpenAPI / Swagger
- ORM
- Data validation
- Error handling

### Containers

- Docker
- Docker Compose / multi-container ecosystem
- Reproducible images
- Environment variables

### AWS

- IAM
- VPC
- Subnets
- Security Groups
- EC2
- S3
- RDS
- ECR
- ECS
- Fargate
- ALB

### Messaging

- RabbitMQ

### Data Processing

- Apache Airflow
- Celery
- Apache Spark
- ETL
- Partitioning
- Columnar formats
- Distributed processing

### DevOps

- Git
- Pull Requests
- CI/CD
- Automated testing
- Image building
- Automated deployment

---

## Created by

**RutaViva Team**

- Camila Marrugo
- Daniel Barrera
- Daniel Arciniegas

**2026 · Project under development**
