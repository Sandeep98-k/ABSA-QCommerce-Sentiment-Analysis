"""Optional model evaluation template.
Run only after you have a TRAINED sentiment classifier and a ground-truth label.
This file deliberately does not invent accuracy from the existing labels.
"""
from analytics import load_data

df=load_data()
print('Dataset loaded:',len(df),'rows')
print('Ground-truth label currently available:', 'Customer Feedback Type' in df.columns)
print('To calculate genuine model accuracy, evaluate held-out predictions against labels that were not used for training.')
