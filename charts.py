import plotly.express as px

def sentiment_distribution(df):
    d=df.groupby(['Platform','Sentiment']).size().reset_index(name='Reviews')
    return px.bar(d,x='Platform',y='Reviews',color='Sentiment',barmode='group',title='Sentiment Distribution')

def aspect_distribution(df):
    d=df.assign(Aspect=df['Aspect'].str.split(', ')).explode('Aspect').groupby(['Platform','Aspect']).size().reset_index(name='Reviews')
    return px.bar(d,x='Aspect',y='Reviews',color='Platform',barmode='group',title='Aspect Distribution')

def aspect_sentiment(df):
    d=df.assign(Aspect=df['Aspect'].str.split(', ')).explode('Aspect').groupby(['Platform','Aspect','Sentiment']).size().reset_index(name='Reviews')
    return px.bar(d,x='Aspect',y='Reviews',color='Sentiment',facet_col='Platform',barmode='group',title='Aspect-Based Sentiment')

def delivery(df):
    d=df.groupby('Platform')['Delivery Time (min)'].mean().reset_index()
    return px.bar(d,x='Platform',y='Delivery Time (min)',text_auto='.1f',title='Average Delivery Time')

def rating(df):
    return px.box(df,x='Platform',y='Rating',color='Platform',title='Rating Distribution')
