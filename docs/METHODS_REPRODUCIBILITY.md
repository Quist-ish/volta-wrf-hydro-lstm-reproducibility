# Methods Reproducibility

This repository supports the reproducibility package for the study:

**A modular environmental modelling framework for coupling WRF-Hydro, LSTM residual correction, and multi-source flood diagnostics in data-scarce regulated basins**

Zenodo release: **v1.0.1**  
DOI: **10.5281/zenodo.20762197**

## Harmonization

All datasets were harmonized to a common 0.05° modelling grid. CHIRPS precipitation was used as rainfall forcing, while ERA5 atmospheric variables were aggregated from hourly to daily resolution. HydroSHEDS/SRTM elevation data, Landsat-derived land cover, and HWSD soil properties supported drainage construction, routing representation, and land-surface parameterization.

## WRF-Hydro simulation

WRF-Hydro was run in standalone uncoupled mode with Noah-MP and diffusive-wave routing. The model generated daily discharge and hydrological state variables used as the process-based simulation backbone.

## Residual learning

Residual learning was formulated as benchmark-relative correction, not direct discharge replacement. Residuals were defined as:

```text
e(t) = Q_B(t) - Q_WRF(t)

where Q_B(t) is the mapped G-RUN runoff/reanalysis benchmark and Q_WRF(t) is standalone WRF-Hydro discharge.

A 30-day input sequence was used to train a single-layer LSTM with 64 hidden units, dropout of 0.2, Adam optimizer, learning rate of 0.001, batch size of 64, and early stopping. Corrected discharge was computed as:

Q_corr(t) = Q_WRF(t) + e_hat(t)

where e_hat(t) is the predicted residual correction.

Baseline models

Two lower-complexity residual baselines were retained:

Persistence residual correction
Linear autoregressive residual correction with WRF-Hydro discharge as a covariate

ARIMA is not included in the revised baseline comparison.

Evaluation

Evaluation was conducted for the AMJJASO wet season. Discharge metrics included RMSE, MAE, R², NSE, KGE, residual variance, and lag-1 residual autocorrelation.

Q90 was used as the primary AMJJASO high-flow target. Q95 was retained as an extreme-flow sensitivity test.

Spatial flood diagnostics were interpreted as benchmark-relative and satellite-supported indicators after permanent-water masking with JRC Global Surface Water. These outputs should not be interpreted as independent discharge validation or full hydraulic inundation validation.

Data and licensing

Third-party raw datasets are not redistributed unless permitted by the original providers. Users should download CHIRPS, ERA5, G-RUN ENSEMBLE, GRDC, GloFAS, Global Flood Database, JRC Global Surface Water, Sentinel-1 SAR, HydroSHEDS/SRTM, Landsat-derived products, and HWSD soil data from their official repositories and comply with their licensing and citation requirements
