from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / 'data'

def load_data(path=None):
    path = Path(path) if path else DATA_DIR / 'Processed_ABSA.xlsx'
    if not path.exists():
        raise FileNotFoundError(f'Dataset not found: {path}')
    xls = pd.ExcelFile(path)
    frames=[]
    for sheet in xls.sheet_names:
        d=pd.read_excel(path,sheet_name=sheet)
        d.columns=d.columns.astype(str).str.strip()
        if 'Platform' not in d.columns and sheet!='Combined Dataset': d['Platform']=sheet
        frames.append(d)
    df=pd.concat(frames,ignore_index=True).drop_duplicates().reset_index(drop=True)
    return normalize(df)

def normalize(df):
    df=df.copy()
    df['Platform']=df['Platform'].astype(str).str.strip().str.title()
    df['Review Text']=df['Review Text'].fillna('').astype(str).str.strip()
    df['Rating']=pd.to_numeric(df['Rating'],errors='coerce')
    df['Delivery Time (min)']=pd.to_numeric(df['Delivery Time (min)'].astype(str).str.extract(r'(\d+(?:\.\d+)?)')[0],errors='coerce')
    df['Customer Feedback Type']=df['Customer Feedback Type'].fillna('Neutral').astype(str).str.strip().str.title()
    df['Sentiment']=df['Customer Feedback Type']
    df['Aspect']=df.apply(infer_aspects,axis=1)
    score={'Positive':100,'Neutral':50,'Negative':0}
    df['Sentiment Score']=df['Sentiment'].map(score).fillna(50)
    return df

def infer_aspects(row):
    text=' '.join(str(row.get(c,'')) for c in ['Review Text','Customer Feedback Type','Product Availability','Price Range']).lower()
    aspects=[]
    delivery=['delivery','delayed','delay','late','on time','fast','quick','slow']
    pricing=['price','pricing','discount','offer','affordable','cheap','expensive','cost','fee','charge']
    product=['product','quality','fresh','freshness','damaged','packaging','available','availability','out of stock','stock']
    app=['app','application','login','checkout','payment','tracking','crash','interface','notification']
    if any(x in text for x in delivery): aspects.append('Delivery Speed')
    if any(x in text for x in pricing): aspects.append('Pricing')
    if any(x in text for x in product): aspects.append('Product Quality')
    if any(x in text for x in app): aspects.append('App Experience')
    return ', '.join(dict.fromkeys(aspects)) if aspects else 'Other'
