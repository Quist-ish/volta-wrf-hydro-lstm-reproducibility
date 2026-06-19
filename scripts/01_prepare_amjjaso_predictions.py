from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
infile = ROOT/'data/processed/amjjaso_predictions.csv'
outfile = ROOT/'data/processed/amjjaso_predictions_clean.csv'

def clean_numeric(s):
    return pd.to_numeric(s.astype(str).str.replace(',', '', regex=False), errors='coerce')

def normalize(df):
    rename={}
    for c in df.columns:
        lc=c.lower().strip()
        if lc in ['benchmark','grun','g_run','g-run','q_grun','q_g_run','q_benchmark']: rename[c]='benchmark'
        elif lc in ['wrf','wrf_hydro','wrf-hydro','q_wrf','standalone','wrfhydro']: rename[c]='wrf_hydro'
        elif lc in ['hybrid','lstm_hybrid','wrf_lstm','wrf-hydro-lstm','q_hybrid']: rename[c]='hybrid'
        elif lc in ['date','time','datetime']: rename[c]='date'
        elif lc == 'month': rename[c]='month'
    return df.rename(columns=rename)

df = normalize(pd.read_csv(infile))
for c in ['benchmark','wrf_hydro','hybrid']:
    if c in df: df[c]=clean_numeric(df[c])
if 'date' in df:
    df['date']=pd.to_datetime(df['date'], errors='coerce'); df['month']=df['date'].dt.month
if 'month' in df:
    df['month']=pd.to_numeric(df['month'], errors='coerce')
    df=df[df['month'].isin([4,5,6,7,8,9,10])].copy()
df=df.dropna(subset=['benchmark','wrf_hydro']).reset_index(drop=True)
df.to_csv(outfile, index=False)
print('Saved', outfile, len(df), 'rows')
