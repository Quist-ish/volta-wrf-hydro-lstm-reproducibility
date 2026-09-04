# Volta WRF-Hydro–LSTM Reproducibility Package

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22285366.svg)](https://doi.org/10.5281/zenodo.22285366)

This repository supports the submitted manuscript:

**Benchmark-relative WRF-Hydro–LSTM residual correction for wet-season high-flow reconstruction in the regulated Volta River Basin, Ghana**

## Current archival record

The editor-ready reproducibility package is archived on Zenodo:

- Zenodo record: https://zenodo.org/records/22285366
- DOI: https://doi.org/10.5281/zenodo.22285366
- Version: v1.2 editor-ready update
- Publication date: 2026-09-04

Zenodo is the citable, persistent archive. This GitHub repository is maintained as the working code/documentation mirror.

## Purpose

This repository documents a benchmark-relative hydrological modelling and flood-diagnostic workflow for AMJJASO wet-season high-flow reconstruction in the Volta River Basin. It supports scrutiny of the manuscript workflow, data hierarchy, residual-learning design, benchmark-relative metrics, and spatial flood diagnostics.

## Evidence hierarchy and interpretation

The study uses source-specific evidence roles. These sources should not be treated as interchangeable validation datasets.

- WRF-Hydro is retained as the process-based hydrological backbone.
- LSTM is used as an additive residual-correction post-processor, not as a replacement hydrological model.
- G-RUN ENSEMBLE is used only as a runoff/reanalysis benchmark for residual construction and benchmark-relative comparison.
- Native G-RUN is monthly at 0.5° resolution and extends to 2019; harmonization does not create independent daily observed discharge.
- GRDC station records and GloFAS discharge provide separate discharge context where available.
- Global Flood Database, JRC Global Surface Water, and Sentinel-1 SAR provide satellite-supported spatial evidence and permanent-water separation.
- Spatial flood diagnostics are benchmark-relative and satellite-supported. They are not full hydraulic inundation validation.

## Study domain and time window

- Hydrological context: Volta River Basin.
- Assessment focus: Ghanaian Volta focus domain.
- Season: AMJJASO wet season, April to October.
- Model grid: 0.05 degrees, approximately 5 km.
- Simulation period: 1974–2024.
- G-RUN benchmark support: native product extends to 2019; post-2019 analyses require separate external context.

## Main reproducible outputs

| Manuscript item | Repository/Zenodo support |
|---|---|
| Table 1 | Dataset inventory and source-specific evidence roles |
| Table 2 | WRF-Hydro–LSTM configuration and benchmark-specific evaluation design |
| Table 3 | AMJJASO benchmark-relative streamflow performance |
| Table 4 | Q90 and Q95 high-flow diagnostics |
| Table 5 | Flood-area and spatial diagnostics |
| Table 6 | Integrated temporal-spatial synthesis |
| Figs. 1–11 | Figure-support materials and extracted manuscript figure copies |
| Supplementary Tables S1–S5 | Locked supplementary result tables and configuration summaries |
| Supplementary Figs. S1–S7 | Supplementary figure-support materials |

## Corrected benchmark-relative results used in the submitted manuscript

| Metric | Standalone WRF-Hydro | Hybrid WRF-Hydro–LSTM | Interpretation |
|---|---:|---:|---|
| AMJJASO RMSE | 1.411 | 0.844 | 40.22% reduction |
| AMJJASO MAE | 1.091 | 0.606 | Lower benchmark-relative error |
| R² | 0.610 | 0.851 | Higher benchmark-relative agreement |
| NSE | 0.574 | 0.848 | Higher hydrograph skill |
| KGE | 0.776 | 0.845 | Higher distributional agreement |
| Q90 RMSE | 2.284 | 1.693 | 25.88% reduction; primary high-flow target achieved |
| Q95 RMSE | 2.486 | 2.102 | 15.47% reduction; sensitivity improvement only |
| Flood-area RMSE | 1,670.86 km² | 1,431.82 km² | 14.31% reduction |
| Full-period spatial disagreement | 0.117 | 0.057 | 50.90% reduction |

## Repository structure

```text
config/         YAML configuration files for study setup, WRF-Hydro, LSTM, and evaluation
scripts/        Python scripts for environment check, preprocessing, training, metrics, figures, and manifest export
data/           processed data templates and raw-data placeholders
outputs/        generated tables, figures, and packaged outputs
docs/           dataset inventory, crosswalks, methods notes, audit notes, and data-availability text
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

The full editor-ready reproducibility archive contains locked tables, figure-support files, audit crosswalks, and checksums. Use the Zenodo archive for the citable version of record.

## Data and licensing

Third-party raw datasets are not redistributed unless permitted by the original providers. Users should obtain CHIRPS, ERA5, G-RUN ENSEMBLE, GRDC, GloFAS, Global Flood Database, JRC Global Surface Water, Sentinel-1 SAR, HydroSHEDS/SRTM, land-cover, and HWSD products from their official repositories and comply with their licensing, citation, and access conditions.

Scripts, configuration files, documentation, and derivative reproducibility materials are released under the MIT License unless otherwise stated. Third-party data remain subject to their original provider licences.

## Citation

If you use this reproducibility package, please cite the Zenodo archive:

Quist, I., Bi, S., Yeboah, E., Sarfo, I., Owusu, A. B., Mensah, A. O. K. N., Evi, M., Shwe, M. M., Darko, G., Oduro, C., & Quist, B. N. Y. (2026). *Reproducibility package for the benchmark-relative WRF-Hydro–LSTM residual-correction framework in the Volta River Basin* (Version v1.2 editor-ready update). Zenodo. https://doi.org/10.5281/zenodo.22285366
