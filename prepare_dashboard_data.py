from pathlib import Path
from analytics import load_data

BASE=Path(__file__).resolve().parent
OUT=BASE/'results'
OUT.mkdir(exist_ok=True)
df=load_data()
df.to_excel(OUT/'dashboard_data.xlsx',index=False)
df.to_csv(OUT/'dashboard_data.csv',index=False,encoding='utf-8-sig')
print('Rows:',len(df))
print('Platforms:',df['Platform'].value_counts().to_dict())
print('Sentiments:',df['Sentiment'].value_counts().to_dict())
print('Aspects:',df['Aspect'].value_counts().to_dict())
print('Saved:',OUT/'dashboard_data.xlsx')
