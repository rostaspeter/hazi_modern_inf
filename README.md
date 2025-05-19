# AI Training & Monitoring Pipeline (Flask + MLflow + Airflow + Evidently)

Ez a projekt egy **konténerizált gépi tanulási pipeline-t** valósít meg, amely különböző komponenseket integrál:  
- **Flask API** a modell tanításához és a fájlok feltöltéséhez  
- **MLflow** a kísérletek nyomon követéséhez és modellek verziókezeléséhez  
- **Apache Airflow** az automatizált ütemezéshez  
- **Evidently + Streamlit** az adatdrift vizualizálásához

---

## 🔧 Technológiák

| Szolgáltatás | Leírás |
|--------------|--------|
| **Flask** | REST API tanító pipeline elindítására |
| **MLflow** | Modellnaplózás, metrikák és artifact kezelés |
| **Airflow** | DAG-ok segítségével ütemezett futtatások |
| **Streamlit (Evidently)** | Adatdrift elemzés és vizualizáció |

---

## 🗂 Mappa Struktúra

```
.
├── DockerfileAirflow
├── DockerfileEvidently
├── DockerfileFlask
├── docker-compose.yml
├── dags/              # Airflow DAG-ok
├── data/              # Input adatok
├── evidently/         # Streamlit alkalmazás Evidently-vel
├── mlruns/            # MLflow backend store és artifact root
├── requirements.txt
```

---

## 🚀 Indítás

A konténerek elindításához használd az alábbi parancsot:

```bash
docker-compose up --build
```

Ez elindítja a következő szolgáltatásokat:
- `http://localhost:8081` → Flask API
- `http://localhost:5102` → MLflow UI
- `http://localhost:8080` → Airflow UI (felhasználó: `admin`, jelszó: `admin`)
- `http://localhost:8501` → Evidently Streamlit Dashboard

---

## ⚙️ Airflow

- Az `airflow` konténer az `apache/airflow:2.9.1-python3.10` image-ből épül.
- A `dags/` mappából bemásolt DAG-okat futtatja standalone módban.
- Az adatbázis SQLite-alapú, és helyileg mountolva van.

---

## 📈 MLflow

- Az `mlflow` konténer a hivatalos MLflow szervert futtatja.
- A modellek és kísérletek a `./mlruns` könyvtárba kerülnek mentésre.
- Flask API ezen keresztül logolja az eredményeket.

---

## 📊 Evidently (Streamlit)

- A Streamlit alapú felület az Evidently-t használja adatdrift kimutatására.
- A `evidently_app.py` fájl felelős a dashboard futtatásáért.

---

## 🧪 Tesztelés

- Tölts fel egy CSV fájlt a Flask API-n keresztül a tanítás elindításához.
- Ellenőrizd az MLflow UI-n a metrikákat és modelleket.
- Vizsgáld meg az adatdriftet a Streamlit dashboardon.
- Automatizált pipeline futásokat az Airflow UI-n láthatsz.

---

## 📋 Előfeltételek

- Docker + Docker Compose telepítve
- Portok elérhetősége: `8080`, `8081`, `5102`, `8501`

---

## 📄 Licenc

Ez a projekt oktatási vagy fejlesztési célra készült.
