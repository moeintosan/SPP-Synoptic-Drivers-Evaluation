# Linking SPP Skill to Synoptic Drivers of Extreme Events

[![DOI](https://img.shields.io/badge/DOI-10.1007%2Fs00704--026--06312--w-blue.svg)](https://doi.org/10.1007/s00704-026-06312-w)
[![Journal](https://img.shields.io/badge/Journal-Theoretical_and_Applied_Climatology-green.svg)](https://link.springer.com/journal/704)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the generalized analytical framework and visualization scripts associated with the research paper published in **Theoretical and Applied Climatology (2026)**.

## 📌 Overview
This project presents a dual assessment over a topographically complex mountain-desert transition zone in Isfahan province, Iran. It evaluates four leading multi-satellite precipitation products (SPPs) and diagnoses the large-scale atmospheric architecture of extreme wet months using ERA5 reanalysis data.

### Key Features of the Analysis:
* **Validation of SPPs:** Comprehensive evaluation of **IMERG, GSMaP, CHIRPS, and PERSIANN-CDR** against 85 ground-based rain gauges over a 20-year period (2004–2023).
* **Performance Metrics:** Implementation of continuous (CC, RMSE, NMB, MFB) and categorical (POD, FAR, CSI, BIAS Score) metrics.
* **Synoptic Climatology:** Identification of recurrent atmospheric patterns (200 hPa upper-level troughs and 850 hPa low-level moisture transport) driving extreme precipitation events.

## 📊 Conceptual Framework
The interaction between a deep upper-level trough over the Eastern Mediterranean and a surface low-pressure system induces a strong cyclonic circulation, establishing a moisture conveyor belt from the Red Sea and Persian Gulf.

<img width="3315" height="2209" alt="Figure_16_Conceptual_Schematic_PERFECT" src="https://github.com/user-attachments/assets/e55a9da5-a1fd-41f8-b98e-4f1effbf16fc" />

## 📂 Repository Structure
```text
SPP-Synoptic-Drivers-Evaluation/
├── data/               # Note: Raw rain gauge observations are restricted by institutional policy.
├── scripts/            # Generalized Python scripts for continuous and categorical metrics calculation.
├── notebooks/          # Jupyter notebooks for atmospheric state profile heatmaps.
├── figures/            # High-resolution outputs and synoptic anomaly maps.
├── requirements.txt    # Required Python dependencies (e.g., xarray, pandas, matplotlib, cartopy).
└── README.md
