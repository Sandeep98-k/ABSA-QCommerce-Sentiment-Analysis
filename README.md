# Quick Commerce ABSA Project

## Dataset
Processed Excel dataset with Blinkit and Zepto sheets and a combined sheet. The supplied dataset contains 6,000 Blinkit + 6,000 Zepto records.

## Stack
- Excel / Pandas: data processing
- Python + NLP: preprocessing and aspect mapping
- Transformer/BERT-family model: sentiment modeling (use the trained checkpoint for genuine model evaluation)
- PyTorch + Hugging Face Transformers: deep-learning layer
- Plotly: interactive charts
- Streamlit: dashboard
- VS Code: development
- Google Colab: preprocessing/training workflow

## Run in VS Code
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python check_data.py
python prepare_dashboard_data.py
streamlit run app.py
```

## Dashboard behavior
- Combined Dataset: Blinkit vs Zepto comparison
- Blinkit: Blinkit-only title, KPIs, aspects, sentiment, delivery, ratings, complete data
- Zepto: Zepto-only title, KPIs, aspects, sentiment, delivery, ratings, complete data
- Filters immediately update every KPI/chart/table
- No `Predicted Sentiment` dependency: the existing `Customer Feedback Type` is normalized to `Sentiment`

## Accuracy
Do not report dashboard percentages as model accuracy. Genuine accuracy requires a held-out labelled test set and predictions from the trained model.
