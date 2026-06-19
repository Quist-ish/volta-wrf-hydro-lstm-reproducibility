# Methods Reproducibility

## Harmonization
All datasets were harmonized to a 0.05-degree modelling grid. CHIRPS precipitation was used as rainfall forcing; ERA5 variables were aggregated from hourly to daily; HydroSHEDS/SRTM, Landsat-derived land cover, and HWSD soil properties supported routing and land-surface representation.

## WRF-Hydro
WRF-Hydro was run in standalone uncoupled mode with Noah-MP and diffusive-wave routing. The model produced daily discharge and hydrological state variables.

## Residual learning
Residuals were defined as `r_t = Q_G-RUN(t) - Q_WRF(t)`. A 30-day sequence was used to train a single-layer LSTM with 64 hidden units, dropout 0.2, Adam optimizer, learning rate 0.001, batch size 64, and early stopping. Corrected discharge was computed as `Q_corr(t) = Q_WRF(t) + r_hat(t)`.

## Baselines
Persistence residual correction and LR-AR residual correction are retained. ARIMA is not included in the revised baseline comparison.

## Evaluation
AMJJASO metrics include RMSE, MAE, R2, NSE, KGE, residual variance, and lag-1 ACF. Q90 is the primary high-flow target; Q95 is an extreme-flow sensitivity test. Spatial metrics are benchmark-relative, satellite-supported diagnostics after permanent-water masking.
