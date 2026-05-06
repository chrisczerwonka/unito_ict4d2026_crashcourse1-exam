# 🗺️ Sahel Edu-Continuity Hub (2026)

**ICT for Civic Data Crash Course – Exam Project | Response to Education Bridge Initiative (EBI) RFP**

This project provides a technical framework for mapping education continuity risk in the conflict-affected WAEMU/UEMOA regions, primarily focusing on **Burkina Faso**, **Mali**, and **Niger**. It demonstrates how open geospatial data and conflict-event monitoring can be transformed into actionable insights for humanitarian prioritization.

---

## 🚀 Live Visual Artifacts
*   **[Interactive Risk Map](https://chrisczerwonka.github.io/unito_ict4d2026_crashcourse1-exam/map/)** – Visualize school facilities and their proximity to conflict events.
*   **[Conflict Analysis Dashboard](https://chrisczerwonka.github.io/unito_ict4d2026_crashcourse1-exam/dashboard/)** – Explore regional trends, fatalities, and event types across the Central Sahel.

---

## 🌍 Project Overview & Strategic Intent
Conflict in the Sahel creates systemic disruptions to education. This project answers the call for **timely, localized, and operationally actionable information** to help EBI and local authorities prioritize interventions.

### Research Question
> **How can open geospatial data and conflict-event monitoring help humanitarian organizations identify schools and communities at elevated risk of education disruption in conflict-affected WAEMU/UEMOA regions?**

### Key Objectives:
- Identify schools within high-risk "proximity zones" (5km) of recent conflict events.
- Aggregate regional conflict trends to inform macro-level resource allocation.
- Provide a reproducible, lightweight data pipeline for non-technical humanitarian staff.

---

## 🛠️ Methodology & Risk Assessment
The project employs a **Proximity-Based Risk Model**:
1.  **Data Integration:** Merging ACLED conflict event data with school infrastructure points (HOT-OSM/UNICEF).
2.  **Geospatial Analysis:** A Python-based Haversine calculation determines the absolute nearest conflict event for every recorded school.
3.  **Classification:**
    *   🟣 **At-Risk:** Schools within **5.0 km** of a conflict event.
    *   🟢 **Safe:** Schools further than 5.0 km from recorded incidents.
4.  **Normalization:** Conflict severity is visualized through fatalities-weighted marker clustering.

---

## 📁 Repository Architecture
```text
.
├── 📊 data/
│   ├── raw/           # Unmodified source files (ACLED, OSM)
│   ├── cleaned/       # Standardized CSVs via OpenRefine/Python
│   └── processed/     # GeoJSON outputs for web visualization
├── 🗺️ map/             # Leaflet.js interactive mapping interface
├── 📈 dashboard/       # Chart.js conflict analytics dashboard
├── 🐍 scripts/         # Python automation for filtering and analysis
├── 📄 docs/            # Methodology, data sources, and strategy notes
└── index.html         # Project landing page
```

---

## ⚙️ Data Pipeline & Reproducibility
To reproduce the analysis or update the data:

1.  **Filter Data:** Run the country-level filter on raw ACLED data.
    ```bash
    python3 scripts/filter-sahel-data.py
    ```
2.  **Analyze Risk:** Run the geospatial proximity analysis.
    ```bash
    python3 scripts/analyze-school-risk.py
    ```
3.  **Deploy:** The outputs in `data/processed/` are automatically consumed by the Map and Dashboard.

---

## 📊 Data Attribution & Licenses
| Dataset | Source | License | Role |
| :--- | :--- | :--- | :--- |
| **Conflict Events** | [ACLED](https://acleddata.com) | [Creative Commons](https://acleddata.com/curated-data-files/) | Primary risk indicator |
| **School Locations** | [HOT-OSM](https://data.humdata.org/) | [ODbL](https://opendatacommons.org/licenses/odbl/) | Infrastructure baseline |
| **Admin Boundaries** | [OCHA/HDX](https://data.humdata.org/) | [CC-BY-IGO](https://creativecommons.org/licenses/by/3.0/igo/) | Geospatial containment |
| **Population** | [WorldPop](https://www.worldpop.org/) | [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Vulnerability context |

---

## 🧠 AI Disclosure & Ethics
This project was developed using **Gemini CLI** and **v0.dev** as high-level pair-programming assistants. 

*   **Role of AI:** Assisted in drafting Python geospatial logic (Haversine formula), boilerplate HTML/CSS for the dashboard, and repository standardization.
*   **Human Oversight:** Every line of code and data point was manually verified for geographic accuracy and humanitarian context. No "black-box" AI logic was used for the actual risk classification; the 5km threshold is a user-defined humanitarian parameter.

---

## 📄 License
This repository is licensed under the **MIT License**. The underlying datasets remain subject to the licenses provided by their respective authors (see Attribution section).
