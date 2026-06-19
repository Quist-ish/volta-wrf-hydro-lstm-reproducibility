# Volta WRF-Hydro–LSTM Reproducibility Package

This repository supports the manuscript **Multi-source assessment of a hybrid WRF-Hydro–LSTM residual-correction framework for AMJJASO high-flow reconstruction in the regulated Volta River Basin**.

## Core interpretation

- WRF-Hydro is the process-based hydrological backbone.
- LSTM is an additive residual-correction post-processor, not a replacement hydrological model.
- G-RUN ENSEMBLE is used only as a runoff/reanalysis benchmark for residual construction and benchmark-relative comparison.
- GRDC, GloFAS, Global Flood Database, JRC Global Surface Water, and Sentinel-1 SAR provide separate discharge or spatial flood evidence.
- Spatial flood diagnostics are benchmark-relative and satellite-supported; they are not full hydraulic inundation validation.

## Study domain and time window

- Hydrological context: Volta River Basin.
- Assessment focus: Ghanaian Volta focus domain.
- Season: AMJJASO wet season, April–October.
- Model grid: 0.05 degrees, approximately 5 km.
- Stated simulation period: 1974–2024.

## Research objectives

1. Assess standalone WRF-Hydro performance using benchmark-relative comparison and separate independent/external evidence sources.
2. Determine whether additive LSTM residual correction reduces AMJJASO and Q90 high-flow RMSE by at least 20% relative to standalone WRF-Hydro.
3. Evaluate whether corrected discharge behaviour is consistent with satellite-supported spatial flood diagnostics after permanent-water exclusion.

## Corrected benchmark-relative results used in the revised manuscript

| Metric | Standalone WRF-Hydro | Hybrid WRF-Hydro–LSTM | Interpretation |
|---|---:|---:|---|
| AMJJASO RMSE | 1.411 | 0.844 | 40.22% reduction |
| AMJJASO MAE | 1.091 | 0.606 | Lower error |
| R² | 0.610 | 0.851 | Higher agreement |
| NSE | 0.574 | 0.848 | Higher hydrograph skill |
| KGE | 0.776 | 0.845 | Higher distributional agreement |
| Q90 RMSE | 2.284 | 1.693 | 25.88% reduction; primary target achieved |
| Q95 RMSE | 2.486 | 2.102 | 15.47% reduction; sensitivity only |
| Flood-area RMSE | ~1,680 km² | ~1,420 km² | ~15% reduction |
| Spatial disagreement | 0.34 | 0.27 | Reduced mismatch |

## Repository structure

```text
config/         YAML configuration files for study, WRF-Hydro, LSTM, and evaluation
scripts/        Python scripts for environment check, preprocessing, training, metrics, figures, and manifest
data/           processed data, templates, and raw-data placeholders
outputs/        generated tables, figures, and packaged outputs
docs/           dataset inventory, data availability, methods, checklist, Zenodo text
notebooks/      workflow outline notebook
```

## Reproduction sequence

```bash
conda env create -f environment.yml
conda activate volta-wrf-lstm-repro
python scripts/00_check_environment.py
python scripts/01_prepare_amjjaso_predictions.py
python scripts/02_train_lstm_residual_model.py
python scripts/03_compute_metrics_and_baselines.py
python scripts/04_generate_supplementary_figures.py
python scripts/05_export_zenodo_manifest.py
```

## Minimum processed files included or expected

- `data/processed/amjjaso_predictions.csv`
- `data/processed/GFD_Ghana_Volta_Flood_Event_Stats_2000_2018.csv`
- `data/processed/JRC_Ghana_Volta_Water_Area_Stats.csv`
- `outputs/tables/Table_S3_domain_based_AMJJASO_residual_baseline_populated.csv`

Third-party raw source data should be downloaded from the official providers according to their licensing terms unless redistribution is permitted.
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20762197.svg)](https://doi.org/10.5281/zenodo.20762197)
