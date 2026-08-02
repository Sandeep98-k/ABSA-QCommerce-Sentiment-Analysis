from analytics import load_data

df=load_data()
print('ROWS:',len(df))
print('COLUMNS:',df.columns.tolist())
print('\nPLATFORM:')
print(df['Platform'].value_counts())
print('\nSENTIMENT:')
print(df['Sentiment'].value_counts())
print('\nASPECT:')
print(df['Aspect'].value_counts())
print('\nMISSING:')
print(df.isna().sum())
