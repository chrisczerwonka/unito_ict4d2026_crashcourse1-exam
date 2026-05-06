# Open Datasets for Education and Conflict in the WAEMU Region

This document outlines key open data sources for mapping conflict events, school locations, displacement, and population vulnerability in Burkina Faso, Mali, Niger, and northern Benin. These resources are selected to support humanitarian education continuity projects.

## 1. Conflict Events: ACLED
**The Armed Conflict Location & Event Data Project**

* **What it covers:** Reported political violence (battles, explosions, violence against civilians) and non-violent protests.
* **Information contained:** Event dates, types of violence, actors involved (e.g., insurgent groups), and reported fatalities.
* **Geographic level:** **Point locations** (Latitude/Longitude) and administrative levels (District/Region).
* **Format:** CSV, Excel, and API.
* **How to access:** Register for a free account at [acleddata.com](https://acleddata.com). Use the "Data Export Tool" to filter for specific countries and date ranges.
* **Beginner-friendly?** **Yes.** CSV files with coordinates are easily imported into most mapping tools.

## 2. School Infrastructure: UNICEF / Giga
**Global School Mapping (via HDX or Giga)**

* **What it covers:** Precise locations of primary and secondary educational facilities.
* **Information contained:** School names, education levels, and sometimes connectivity or facility status.
* **Geographic level:** **Point locations**.
* **Format:** CSV, GeoJSON, or Shapefile.
* **How to access:** Search for "[Country Name] - Education Facilities" on the [Humanitarian Data Exchange (HDX)](https://data.humdata.org/).
* **Beginner-friendly?** **Yes.** These provide a clear "baseline" map of where schools exist (or existed).

## 3. Population & Vulnerability: WorldPop
**High-Resolution Gridded Population Data**

* **What it covers:** Estimated population density based on census data and satellite imagery.
* **Information contained:** People per pixel (100m x 100m). Specific datasets also estimate school-aged child populations.
* **Geographic level:** **Gridded (Raster)** data or **District-level summaries**.
* **Format:** GeoTIFF (for GIS) or CSV (for tabular summaries).
* **How to access:** Available at [worldpop.org](https://www.worldpop.org/) or via HDX.
* **Beginner-friendly?** **Medium.** Raster files (GeoTIFF) require GIS software (like QGIS), but the CSV district summaries are easy to use in Excel.

## 4. Displacement Patterns: IOM DTM
**IOM Displacement Tracking Matrix**

* **What it covers:** Internally Displaced Persons (IDP) and returnee movements.
* **Information contained:** Number of IDPs, host community locations, reasons for displacement, and sectoral needs.
* **Geographic level:** **Point locations** (camps) and **Administrative levels** (host districts).
* **Format:** CSV and PDF summary reports.
* **How to access:** [DTM West and Central Africa](https://dtm.iom.int/regions/west-and-central-africa) portal.
* **Beginner-friendly?** **Yes.** Baseline assessment CSVs are excellent for understanding where the demand for education has shifted.

---

## Integration Strategy for Beginners

To support an **Education Continuity Project**, these datasets should be layered using tools like **QGIS** or **Felt.com**:

1.  **Risk Analysis:** Overlay **ACLED (Conflict)** points on **UNICEF (Schools)** to identify facilities in active conflict zones.
2.  **Gap Analysis:** Compare **IOM DTM (Displacement)** numbers with existing **UNICEF (Schools)** locations to see if the available infrastructure can handle the influx of displaced students.
3.  **Prioritization:** Use **WorldPop** to identify densely populated rural areas that are underserved by physical school buildings but may benefit from remote or mobile learning interventions.
