# Education Continuity Risk Mapping in Conflict-Affected WAEMU/UEMOA Regions

**ICT for Civic Data Crash Course 2026 – Exam Project**

## Project Overview
This project explores how open geospatial data, conflict-event monitoring, and lightweight civic-data tools can support education continuity planning in conflict-affected WAEMU/UEMOA countries [cite: 11, 14].

The project focuses primarily on **Burkina Faso**, with regional references to **Niger** and **Mali**, to identify areas where insecurity, displacement, and infrastructure vulnerability may disrupt access to education [cite: 4, 16]. Using open datasets and simple geospatial analysis, the project demonstrates how humanitarian organizations can complement field expertise with data-driven prioritization and visualization tools [cite: 11, 69, 96].

The work was developed as part of the **ICT for Civic Data Crash Course 2026** exam assignment, which required:
- A visual artifact
- A proposal strategy section
- Transparent access to the underlying data pipeline

---

## Research Question
**How can open geospatial data and conflict-event monitoring help humanitarian organizations identify schools and communities at elevated risk of education disruption in conflict-affected WAEMU/UEMOA regions?** [cite: 11, 27]

### Secondary Questions:
- Which schools are located near conflict-event clusters? [cite: 28]
- Which regions combine high child population vulnerability with low education access? [cite: 30]
- How can lightweight maps and dashboards improve operational prioritization for non-technical humanitarian staff? [cite: 51, 69, 94]
- How can open data complement existing field knowledge rather than replace it? [cite: 96]

---

## Project Angle
This project argues that education continuity monitoring systems can serve as a foundational resilience layer for humanitarian education programming [cite: 12, 14, 92].

Rather than relying solely on fragmented field reporting, organizations can combine:
- Conflict-event datasets [cite: 66]
- School infrastructure data [cite: 67]
- Population and displacement estimates [cite: 68]
- Geospatial analysis [cite: 11, 27]

...to improve prevention, preparedness, and response planning for vulnerable communities [cite: 25, 85]. The approach emphasizes open datasets, low-cost tooling, reproducible workflows, and accessible outputs for non-technical users [cite: 65, 69].

---

## Countries Covered
- **Primary focus:** Burkina Faso [cite: 4, 61]
- **Secondary regional context:** Niger and Mali [cite: 4, 62, 63]
- **Optional spillover analysis:** Northern Benin border regions [cite: 4, 64]

---

## Data Pipeline
The project followed the civic-data pipeline framework:

1.  **Define:** Defined the operational humanitarian question and proposal angle [cite: 1].
2.  **Find:** Identified open datasets related to conflict events, schools, population distribution, and administrative boundaries.
3.  **Get:** Downloaded and organized raw datasets into a structured repository.
4.  **Verify:** Checked geographic validity, duplicate records, coordinate consistency, and dataset completeness.
5.  **Clean:** Used spreadsheet workflows and OpenRefine to standardize names and normalize geographic fields.
6.  **Analyse:** Combined datasets to identify schools near conflict concentrations and regional vulnerability patterns [cite: 27, 37].
7.  **Present:** Published maps, dashboards, and documentation using GitHub Pages [cite: 69].

---

## Tools and Platforms Used
| Tool | Purpose |
| :--- | :--- |
| GitHub Codespaces | Development environment |
| GeminiCLI | AI-assisted coding and workflow support |
| OpenRefine | Data cleaning and normalization |
| Google Sheets | Manual verification and spreadsheet analysis |
| Leaflet | Interactive mapping |
| Chart.js | Dashboard visualizations |
| GitHub Pages | Project publishing |
| v0 by Vercel | UI prototyping and layout support |
| DataViz Catalogue | Visualization planning reference |

---

## Datasets Used
| Dataset | Source | Format | Purpose |
| :--- | :--- | :--- | :--- |
| **ACLED Conflict Events** | [acleddata.com](https://acleddata.com) | CSV | Conflict-event locations and severity [cite: 66] |
| **OpenStreetMap Schools** | [openstreetmap.org](https://www.openstreetmap.org) | GeoJSON | School locations [cite: 67] |
| **Admin Boundaries** | [HDX](https://data.humdata.org/) | GeoJSON | Regional mapping layers |
| **Population Estimates** | [WorldPop](https://www.worldpop.org/) | CSV | Population vulnerability context [cite: 68] |
| **Displacement Data** | UNHCR / IOM | CSV | Displacement and vulnerability overlays [cite: 68] |

---

## Repository Structure
```text
.
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── processed/
├── maps/
├── dashboard/
├── scripts/
├── docs/
├── index.html
└── README.md
```
