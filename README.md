# 📊 Quick Commerce ABSA Project

Aspect-Based Sentiment Analysis (ABSA) and Comparative Customer Intelligence Dashboard for **Blinkit** and **Zepto** using Machine Learning, Deep Learning, and Interactive Data Visualization.

---

## 🚀 Project Overview

This project analyzes customer reviews from two leading Quick Commerce platforms:

- 🛒 Blinkit
- ⚡ Zepto

The system performs **Aspect-Based Sentiment Analysis (ABSA)** to identify customer opinions on different aspects such as Delivery, Product Quality, Pricing, Packaging, Discounts, and Availability.

The application provides an interactive Streamlit dashboard for comparative analytics and customer intelligence.

---

## 📂 Dataset

The project uses a processed Excel dataset containing:

| Dataset | Records |
|---------|---------:|
| Blinkit | 6,000 |
| Zepto | 6,000 |
| Combined | 12,000 |

The Excel workbook contains:

- Blinkit Sheet
- Zepto Sheet
- Combined Dataset Sheet

---

## 🛠 Technology Stack

| Component | Technology |
|-----------|------------|
| Data Processing | Excel, Pandas |
| NLP Preprocessing | Python, spaCy |
| Sentiment Analysis | Transformer / BERT |
| Deep Learning | PyTorch |
| Transformers | Hugging Face |
| Machine Learning | Scikit-learn |
| Visualization | Plotly |
| Dashboard | Streamlit |
| Development | VS Code |
| Training Workflow | Google Colab |

---

## 📋 Project Features

- ✅ Comparative Blinkit vs Zepto Analysis
- ✅ Aspect-Based Sentiment Analysis (ABSA)
- ✅ Interactive Dashboard
- ✅ Dynamic KPI Cards
- ✅ Rating Analysis
- ✅ Sentiment Distribution
- ✅ Delivery Performance Analysis
- ✅ Order Type Analysis
- ✅ Product Availability Analysis
- ✅ Interactive Filters
- ✅ Real-Time Dashboard Updates

---

## 📁 Project Structure

```text
ABSA_PROJECT/
│
├── data/
├── models/
├── results/
├── images/
│   └── dashboard.png
│
├── app.py
├── analytics.py
├── charts.py
├── check_data.py
├── prepare_dashboard_data.py
├── evaluate_model.py
│
├── requirements.txt
└── README.md
```

---

## ▶️ Run the Project

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Environment

Windows

```bash
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Dataset

```bash
python check_data.py
```

### 5. Prepare Dashboard Data

```bash
python prepare_dashboard_data.py
```

### 6. Launch Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 📊 Dashboard Behavior

### Combined Dataset

- Blinkit vs Zepto comparison
- Combined KPIs
- Comparative charts
- Comparative sentiment analysis

### Blinkit Dataset

- Blinkit-specific dashboard title
- Blinkit KPIs
- Blinkit sentiment analysis
- Blinkit delivery analysis
- Blinkit rating analysis
- Blinkit aspect analysis

### Zepto Dataset

- Zepto-specific dashboard title
- Zepto KPIs
- Zepto sentiment analysis
- Zepto delivery analysis
- Zepto rating analysis
- Zepto aspect analysis

---

## 🎛 Interactive Filters

The dashboard supports dynamic filtering by:

- Dataset
- Rating
- Order Type
- Sentiment
- Availability

All KPI cards, charts, and tables update instantly based on the selected filters.

---

## 🤖 Aspect-Based Sentiment Analysis

The project identifies sentiments for multiple business aspects, including:

- 🚚 Delivery
- 📦 Product Quality
- 💰 Pricing
- 🎁 Discounts
- 📦 Packaging
- 🛍 Availability

---

## 📈 Dashboard Metrics

- Total Reviews
- Average Rating
- Positive Sentiment
- Neutral Sentiment
- Negative Sentiment
- Sentiment Distribution
- Delivery Analysis
- Order Type Distribution
- Aspect Analysis

---

## 📚 Accuracy Note

**Dashboard percentages are NOT model accuracy.**

Model accuracy should always be evaluated using:

- Held-out Test Dataset
- Predictions from the trained Transformer/BERT model
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Dashboard sentiment percentages represent customer review distributions and should not be interpreted as machine learning accuracy.

---

## 👨‍💻 Developed Using

- Python
- Pandas
- NumPy
- spaCy
- Hugging Face Transformers
- BERT
- PyTorch
- Scikit-learn
- Plotly
- Streamlit
- VS Code
- Google Colab

---

## 📜 License

This project is developed for academic and research purposes.
