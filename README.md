# Question-Generator-Application

A lightweight resume classification tool built with Streamlit and scikit-learn, designed to help recruiters or job portals automatically categorize resumes into job sectors using a machine learning model.

---

## 🚀 Features

- 📤 Resume Upload – Upload resumes in .txt or .pdf format
- 🧹 Resume Cleaner – Preprocesses resume text (removes noise like URLs, symbols, etc.)
- 🤖 Job Role Classifier – Predicts job categories using a pre-trained ML model
- ✅ Answer Generator – Automatically generate accurate answers
- 🎯 Instant Output – View predicted category within seconds
- 🔍 Simple & Fast – Minimal interface with direct results

---

## 🛠️ Technology Stack

- **Framework**: Streamlit 
- **Machine Learning**: scikit-learn (for model and TF-IDF vectorizer)
- **Preprocessing**: re, nltk
- **Model Files**: clf.pkl, tfidf.pkl
- **Text Extraction**:  UTF-8 and fallback to latin-1 encoding for resume decoding

---

## 📋 Prerequisites

- Python 3.8+  
- Trained ML model saved as clf.pkl
- Trained TF-IDF vectorizer saved as tfidf.pkl

---

## ⚙️ Installation

1. Clone the Repository

```bash
git clone https://github.com/airakibul/Resume_Screening.git

```

2. Create an environment

```bash
python -m venv venv
```

```bash
venv\Scripts\activate

```

3. install requirements

```bash

pip install -r requirements.txt

```

## ▶️ Usage

1. Start the application

```bash

streamlit run app.py


```

2. Upload a PDF file
3. It will show you the catagory


---

## Project Structure

```text
├── app.py
├── clf.pkl
├── tfidf.pkl
├── requirements.txt
└── README.md
```
---

## 🧠 How It Works

- File Upload: Resume file is uploaded and decoded.

- Preprocessing: The text is cleaned using regex and NLTK.

- Feature Extraction: The cleaned text is converted into TF-IDF features.

- Prediction: The ML model predicts a job category.

- Result: The category is shown instantly on the screen.

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## Screenshots

![App Screenshot]( https://github.com/airakibul/Resume_Screening/blob/main/screenshots/Screenshot1.png)
