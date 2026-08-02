import streamlit as st
import pandas as pd
from pathlib import Path
from analytics import load_data
from charts import sentiment_distribution,aspect_distribution,aspect_sentiment,delivery,rating

st.set_page_config(page_title='Quick Commerce ABSA Intelligence',page_icon='⚡',layout='wide')
st.markdown('''<style>.block-container{padding-top:1.5rem}.title{font-size:34px;font-weight:800}.subtitle{font-size:17px;color:#888}.card{padding:16px;border:1px solid #333;border-radius:14px}</style>''',unsafe_allow_html=True)

@st.cache_data
def get_data(): return load_data()

df=get_data()

st.sidebar.title('📌 Dashboard Controls')
dataset=st.sidebar.selectbox('Choose Dataset',['Combined Dataset','Blinkit','Zepto'])

work=df if dataset=='Combined Dataset' else df[df.Platform.eq(dataset)].copy()

# filters
if not work.empty:
    rmin=int(work.Rating.min()); rmax=int(work.Rating.max())
    rr=st.sidebar.slider('⭐ Rating',rmin,rmax,(rmin,rmax))
    work=work[work.Rating.between(rr[0],rr[1])]
for col,label in [('Order Type','📦 Order Type'),('Customer Feedback Type','😊 Sentiment'),('Product Availability','📦 Availability')]:
    if col in work.columns:
        vals=sorted(work[col].dropna().astype(str).unique().tolist())
        sel=st.sidebar.multiselect(label,vals,default=vals)
        work=work[work[col].astype(str).isin(sel)]

if dataset=='Zepto': title='⚡ Zepto Expert-Based Sentiment Analysis'; subtitle='Deep Learning + NLP | Complete Zepto Customer Intelligence'
elif dataset=='Blinkit': title='🛒 Blinkit Expert-Based Sentiment Analysis'; subtitle='Deep Learning + NLP | Complete Blinkit Customer Intelligence'
else: title='📊 Blinkit vs Zepto Expert-Based Sentiment Analysis'; subtitle='Comparative Quick-Commerce Customer Intelligence'
st.markdown(f'<div class="title">{title}</div>',unsafe_allow_html=True)
st.markdown(f'<div class="subtitle">{subtitle}</div>',unsafe_allow_html=True)
st.divider()

if work.empty: st.warning('No records match the selected filters.'); st.stop()

pos=(work.Sentiment=='Positive').sum(); neu=(work.Sentiment=='Neutral').sum(); neg=(work.Sentiment=='Negative').sum()
c1,c2,c3,c4=st.columns(4)
c1.metric('Total Reviews',f'{len(work):,}')
c2.metric('Average Rating',f'{work.Rating.mean():.2f} ⭐')
c3.metric('Positive',f'{pos/len(work)*100:.1f}%')
c4.metric('Negative',f'{neg/len(work)*100:.1f}%')

st.plotly_chart(sentiment_distribution(work),use_container_width=True)
a,b=st.columns(2)
with a: st.plotly_chart(aspect_distribution(work),use_container_width=True)
with b: st.plotly_chart(delivery(work),use_container_width=True)
st.plotly_chart(aspect_sentiment(work),use_container_width=True)
st.plotly_chart(rating(work),use_container_width=True)

st.header(f'🔍 {dataset} Complete Analysis')

# aspect table
aspect_rows=[]
for _,row in work.iterrows():
    for aspect in str(row.Aspect).split(', '): aspect_rows.append((row.Platform,aspect,row.Sentiment))
ad=pd.DataFrame(aspect_rows,columns=['Platform','Aspect','Sentiment'])
if not ad.empty:
    summary=pd.crosstab([ad.Platform,ad.Aspect],ad.Sentiment).reset_index()
    for c in ['Positive','Neutral','Negative']:
        if c not in summary: summary[c]=0
    summary['Total']=summary[['Positive','Neutral','Negative']].sum(axis=1)
    summary['Positive %']=(summary.Positive/summary.Total*100).round(1)
    summary['Negative %']=(summary.Negative/summary.Total*100).round(1)
    st.dataframe(summary,use_container_width=True,hide_index=True)

st.header('📋 Complete Selected Dataset')
st.caption('When Zepto is selected, this table contains only Zepto records and all available analysis fields.')
st.dataframe(work,use_container_width=True,height=480,hide_index=True)
st.download_button(f'⬇ Download {dataset} Analysis CSV',work.to_csv(index=False).encode('utf-8'),f'{dataset.replace(" ","_")}_ABSA.csv','text/csv')

st.divider()
st.caption('Project: Expert-Based Aspect-Based Sentiment Analysis of Quick-Commerce Customer Reviews | Data: Excel/Pandas | NLP: Python | Visualization: Plotly | Dashboard: Streamlit')
st.markdown("""
<style>
 ==============================
   MAIN BACKGROUND
   ============================== */

.stApp {
    background: #ffffff;
    color: #111827;
}


/* Main content */

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ==============================
   SIDEBAR
   ============================== */

section[data-testid="stSidebar"] {
    background: #f8fafc;
    border-right: 1px solid #e5e7eb;
}


/* ==============================
   HEADINGS
   ============================== */

h1, h2, h3 {
    color: #111827 !important;
    font-weight: 700;
}


/* ==============================
   NORMAL TEXT
   ============================== */

p, label, span {
    color: #374151;
}


/* ==============================
   METRIC CARDS
   ============================== */

div[data-testid="stMetric"] {

    background: #ffffff;

    border: 1px solid #e5e7eb;

    border-radius: 14px;

    padding: 18px;

    box-shadow:
        0 2px 8px rgba(0,0,0,0.05);
}


/* ==============================
   BUTTON
   ============================== */

.stButton > button {

    border-radius: 10px;

    border: 1px solid #d1d5db;

    background: #ffffff;

    color: #111827;

    font-weight: 600;
}


.stButton > button:hover {

    border-color: #2563eb;

    color: #2563eb;
}


/* ==============================
   DATAFRAME
   ============================== */

div[data-testid="stDataFrame"] {

    border-radius: 12px;

    border: 1px solid #e5e7eb;

}


/* ==============================
   SELECT BOX
   ============================== */

div[data-baseweb="select"] > div {

    background: #ffffff;

    border-radius: 8px;

    border: 1px solid #d1d5db;
}


/* ==============================
   DIVIDERS
   ============================== */

hr {

    border-color: #e5e7eb;
}


/* ==============================
   INFO / SUCCESS
   ============================== */

div[data-testid="stAlert"] {

    border-radius: 10px;
}


/* ==============================
   ZE​​PTO BRAND
   ============================== */

.zepto-title {

    color: #2563eb;

    font-weight: 800;

}


==============================
   BLINKIT BRAND
   ============================== 

.blinkit-title {

    color: #f5b700;

    font-weight: 800;

}

</style>
""", unsafe_allow_html=True)