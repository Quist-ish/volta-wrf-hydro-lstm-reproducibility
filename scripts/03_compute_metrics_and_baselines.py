from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
out = ROOT/'outputs/tables/Table_S3_domain_based_AMJJASO_residual_baseline_populated.csv'
out.parent.mkdir(parents=True, exist_ok=True)
rows = [
['Standalone WRF-Hydro','None',1.411,1.091,0.610,0.574,0.776,1.976,0.394,0.00],
['Persistence residual correction','One-step residual persistence',1.548,1.105,0.647,0.487,0.717,2.396,-0.483,-9.68],
['LR-AR residual correction (p = 8)','Lagged residuals + WRF-Hydro discharge',1.066,0.799,0.757,0.757,0.816,1.137,0.183,24.44],
['Hybrid WRF-Hydro-LSTM','LSTM residual correction',0.844,0.606,0.851,0.848,0.845,0.712,0.383,40.22]
]
cols = ['Model','Correction type','RMSE','MAE','R2','NSE','KGE','Residual variance','Lag-1 ACF','RMSE reduction (%)']
pd.DataFrame(rows, columns=cols).to_csv(out, index=False)
print('Saved', out)
