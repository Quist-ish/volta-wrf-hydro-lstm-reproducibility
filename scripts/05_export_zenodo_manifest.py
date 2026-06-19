from pathlib import Path
import hashlib, pandas as pd
ROOT = Path(__file__).resolve().parents[1]
records=[]
for p in sorted(ROOT.rglob('*')):
    if p.is_file() and '.git' not in p.parts:
        h=hashlib.sha256()
        with open(p,'rb') as f:
            for chunk in iter(lambda:f.read(8192), b''): h.update(chunk)
        records.append({'relative_path':str(p.relative_to(ROOT)).replace('\','/'), 'size_bytes':p.stat().st_size, 'sha256':h.hexdigest()})
out=ROOT/'docs/ZENODO_FILE_MANIFEST.csv'
pd.DataFrame(records).to_csv(out, index=False)
print('Saved', out)
