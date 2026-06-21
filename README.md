
---

# Development Setup

## Prerequisites

Install:

* Python 3.10+
* PostgreSQL 14+
* Git

Verify:

```bash
python3 --version
psql --version
git --version
```

---

# Clone Repository

```bash
git clone git@github.com:Prathmesh2931/Tiger-bachao.git

cd Tiger-bachao
```

---

# Create Virtual Environment

Linux:

```bash
python3 -m venv venv

source venv/bin/activate
```

Windows:

```powershell
python -m venv venv

venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Start PostgreSQL:

Ubuntu:

```bash
sudo systemctl start postgresql

sudo systemctl status postgresql
```

---

Create database:

```bash
sudo -u postgres psql
```

Inside psql:

```sql
CREATE USER tiger_admin WITH PASSWORD 'tiger123';

CREATE DATABASE tiger_db;

GRANT ALL PRIVILEGES ON DATABASE tiger_db TO tiger_admin;

\q
```

---

Verify:

```bash
psql -U tiger_admin -d tiger_db -h localhost
```

Password:

```text
tiger123
```

---

# Environment Configuration

Create local environment file:

```bash
cp .env.example .env
```

Contents:

```env
DATABASE_URL=postgresql://tiger_admin:tiger123@localhost:5432/tiger_db

SECRET_KEY=tiger_secret_key

API_V1_PREFIX=/api/v1

PROJECT_NAME=Tiger Protection System

YOLO_MODEL_PATH=models/tiger_detector_v1.pt
```

---

# Create Database Tables

```bash
PYTHONPATH=. python scripts/create_tables.py
```

Expected output:

```text
Tables Created
```

---

# Verify Database

```bash
psql -U tiger_admin -d tiger_db -h localhost
```

Check tables:

```sql
\dt
```

Expected:

```text
alerts
cameras
detections
```

---

# Run Detection Test

```bash
PYTHONPATH=. python test_pipeline.py
```

Expected:

```text
person detected
truck detected
alert generated
```

---

# Verify Detection Storage

```sql
SELECT *
FROM detections
ORDER BY detection_id DESC;
```

---

# Verify Alerts

```sql
SELECT *
FROM alerts
ORDER BY alert_id DESC;
```

---

# Project Workflow

```text
Image / Video
       │
       ▼
YOLO Detection
       │
       ▼
Threat Scoring
       │
       ▼
PostgreSQL Storage
       │
       ▼
Alert Generation
       │
       ▼
Dashboard Visualization
```

---

# Models Included

Currently:

| Model                | Purpose                   |
| -------------------- | ------------------------- |
| tiger_detector_v1.pt | Tiger Detection           |
| yolov8n.pt           | Human / Vehicle Detection |

---

# Current Features

### Wildlife Monitoring

* Tiger Detection
* Bounding Box Generation
* Confidence Estimation

### Human Intrusion Detection

* Person Detection
* Threat Assessment

### Vehicle Detection

* Car
* Truck
* Bus
* Motorcycle

### Threat Scoring

Current rule-based scoring:

```text
Tiger      → 0.95
Person     → 0.85
Vehicle    → 0.75
Other      → 0.20
```

### Alert Generation

```text
LOW
HIGH
CRITICAL
```

generated automatically.

---

# Development Roadmap

### Completed

* Tiger Detection
* Human Detection
* Vehicle Detection
* PostgreSQL Integration
* Alert Pipeline
* FastAPI Structure
* Dashboard Structure

### In Progress

* Video Processing Pipeline
* Dashboard Integration
* Geofencing

### Future

* Weapon Detection
* Tiger Re-Identification
* Live CCTV Monitoring
* Heatmaps
* Notification Service

---

For your project specifically, this README is enough for another developer to:

```text
git clone
↓
create venv
↓
install requirements
↓
create local PostgreSQL
↓
run create_tables.py
↓
run test_pipeline.py
```

without ever asking you a single question.

After this, the next thing I'd do is create a proper `docker-compose.yml` so that the README eventually becomes:

```bash
git clone ...
docker compose up --build
```

which is the cleanest setup for collaborators.
