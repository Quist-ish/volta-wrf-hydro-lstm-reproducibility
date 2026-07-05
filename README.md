# Volta WRF-Hydro–LSTM Reproducibility Package

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20762197.svg)](https://doi.org/10.5281/zenodo.20762197)

This repository supports the manuscript:

**A modular environmental modelling framework for coupling WRF-Hydro, LSTM residual correction, and multi-source flood diagnostics in data-scarce regulated basins**

## Core interpretation

This repository documents a reproducible environmental modelling workflow for AMJJASO wet-season high-flow reconstruction and benchmark-relative flood diagnostics in the Volta River Basin.

The interpretation follows the manuscript evidence hierarchy:

- WRF-Hydro is the process-based hydrological backbone.
- LSTM is an additive residual-correction post-processor, not a replacement hydrological model.
- G-RUN ENSEMBLE is used only as a runoff/reanalysis benchmark for residual construction and benchmark-relative comparison.
- GRDC station records, GloFAS discharge, Global Flood Database maps, JRC Global Surface Water, and Sentinel-1 SAR provide separate discharge or spatial diagnostic evidence.
- Spatial flood diagnostics are benchmark-relative and satellite-supported. They are not full hydraulic inundation validation.

## Study domain and time window

- Hydrological context: Volta River Basin.
- Assessment focus: Ghanaian Volta focus domain.
- Season: AMJJASO wet season, April to October.
- Model grid: 0.05 degrees, approximately 5 km.
- Simulation period: 1974 to 2024.

## Research objectives

1. Develop a modular environmental modelling workflow that couples WRF-Hydro simulation, LSTM residual correction, and multi-source diagnostic evaluation.
2. Test whether additive LSTM residual correction improves AMJJASO benchmark-relative streamflow reconstruction relative to standalone WRF-Hydro.
3. Evaluate recurrent high-flow performance using $Q_{90}$ as the primary AMJJASO high-flow target and $Q_{95}$ as an extreme-flow sensitivity test.
4. Assess whether corrected discharge behaviour is consistent with benchmark-relative, satellite-supported spatial flood diagnostics after permanent-water masking.

## Corrected benchmark-relative results used in the revised manuscript

| Metric | Standalone WRF-Hydro | Hybrid WRF-Hydro–LSTM | Interpretation |
|---|---:|---:|---|
| AMJJASO RMSE | 1.411 | 0.844 | 40.22% reduction |
| AMJJASO MAE | 1.091 | 0.606 | Lower benchmark-relative error |
| $R^2$ | 0.610 | 0.851 | Higher benchmark-relative agreement |
| NSE | 0.574 | 0.848 | Higher hydrograph skill |
| KGE | 0.776 | 0.845 | Higher distributional agreement |
| $Q_{90}$ RMSE | 2.284 | 1.693 | 25.88% reduction, primary high-flow target achieved |
| $Q_{95}$ RMSE | 2.486 | 2.102 | 15.47% reduction, sensitivity improvement only |
| Flood-area RMSE | 1,670.86 km² | 1,431.82 km² | 14.31% reduction |
| Full-period spatial disagreement | 0.117 | 0.057 | 50.90% reduction |

## Repository structure

```text
config/         YAML configuration files for study setup, WRF-Hydro, LSTM, and evaluation
scripts/        Python scripts for environment check, preprocessing, training, metrics, figures, and manifest export
data/           processed data, templates, and raw-data placeholders
outputs/        generated tables, figures, and packaged outputs
docs/           dataset inventory, data availability statement, methods notes, checklist, and Zenodo text
notebooks/      workflow outline notebook
Reproduction sequence
conda env create -f environment.yml
conda activate volta-wrf-lstm-repro

python scripts/00_check_environment.py
python scripts/01_prepare_amjjaso_predictions.py
python scripts/02_train_lstm_residual_model.py
python scripts/03_compute_metrics_and_baselines.py
python scripts/04_generate_supplementary_figures.py
python scripts/05_export_zenodo_manifest.py
Minimum processed files included or expected
data/processed/amjjaso_predictions.csv
data/processed/GFD_Ghana_Volta_Flood_Event_Stats_2000_2018.csv
data/processed/JRC_Ghana_Volta_Water_Area_Stats.csv
outputs/tables/Table_S3_domain_based_AMJJASO_residual_baseline_populated.csv
Data and licensing

The reproducibility package is archived on Zenodo as release v1.0.1:

DOI: https://doi.org/10.5281/zenodo.20762197

Third-party raw source datasets are not redistributed unless permitted by the original providers. Users should download CHIRPS, ERA5, G-RUN ENSEMBLE, GRDC, GloFAS, Global Flood Database, JRC Global Surface Water, Sentinel-1 SAR, HydroSHEDS/SRTM, land-cover, and HWSD products from their official repositories and comply with their licensing, citation, and access conditions.

Processed files, scripts, configuration files, derived tables, and supplementary figure-generation materials are provided for transparency and reproducibility. Users should consult the repository license file and Zenodo record for reuse conditions.

Citation

If you use this reproducibility package, please cite:

Quist, I., Bi, S., Yeboah, E., Sarfo, I., Owusu, A. B., Mensah, A. O. K. N., Evi, M., & Quist, B. N. Y. (2026). 
Reproducibility package for a hybrid WRF-Hydro-LSTM residual-correction framework in the Volta River Basin (Version v1.0.1). Zenodo. https://doi.org/10.5281/zenodo.20762197

## Data and licensing note

This repository provides scripts, configuration files, processed derivative outputs, evaluation tables, and documentation needed to reproduce the analysis. Third-party raw datasets are not redistributed unless permitted by the original data providers. Users should download CHIRPS, ERA5, G-RUN ENSEMBLE, GRDC, GloFAS, Global Flood Database, JRC Global Surface Water, Sentinel-1 GRD, HydroSHEDS/SRTM, land-cover products, and HWSD soil data from their official repositories and comply with their licenses, citation requirements, and access conditions.

G-RUN ENSEMBLE is used only as a runoff/reanalysis benchmark for residual construction and benchmark-relative comparison. It is not observed discharge, ground truth, or independent validation. GRDC, GloFAS, Global Flood Database, JRC Global Surface Water, and Sentinel-1 products are used as separate discharge or spatial diagnostic evidence streams.
