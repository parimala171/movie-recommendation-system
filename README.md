# 🎬 Movie Recommendation System

## 📌 Project Overview

This project is an end-to-end **Movie Recommendation System** that suggests similar movies based on user input using Natural Language Processing (NLP) and Machine Learning.

The system uses **content-based filtering** to recommend movies by analyzing movie descriptions (overview).

---

## 🚀 Features

* 🎯 Content-based recommendation system
* 🔤 NLP using CountVectorizer
* 📊 Cosine similarity for matching movies
* 🌐 Flask API for real-time recommendations
* 📡 Simulated real-time requests
* 📈 Basic Exploratory Data Analysis (EDA)

---

## 📂 Project Structure

```
MOVIE_RECOMMENDATION_SYSTEM/
│
├── movies.csv              # Raw dataset (not included in repo)
├── cleaned_data.csv        # Processed dataset
├── retrain.py              # Model training script
├── model.pkl               # Movie data
├── similarity.pkl          # Similarity matrix
├── stream_data.py          # Simulated requests
├── app.py                  # Flask API
├── movie_analysis.ipynb    # EDA & NLP notebook
├── Dockerfile
└── requirements.txt
```

---

## 📥 Dataset

Dataset is not uploaded due to GitHub size limits.

👉 Download from:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

👉 After downloading, rename and place as:

```
movies.csv
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## 🧠 Model Training

```bash
python retrain.py
```

---

## 🌐 Run Flask API

```bash
python app.py
```

👉 Open in browser:

```
http://127.0.0.1:5007
```

---

## 📡 Real-time Simulation

```bash
python stream_data.py
```

---

## 🧪 Sample API Request

```json
POST /recommend
{
  "movie": "Avatar"
}
```

👉 Response:

```json
{
  "Recommendations": [
    "Titanic",
    "Guardians of the Galaxy",
    "Interstellar",
    "Inception",
    "The Avengers"
  ]
}
```

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* NLP (CountVectorizer)
* Flask
* Machine Learning

---

## 🔥 Key Learnings

* NLP preprocessing techniques
* Feature extraction using CountVectorizer
* Similarity computation using cosine similarity
* Building recommendation systems
* Deploying ML models using Flask API
* Handling real-time requests

---

## ⚠️ Notes

* Large dataset files are excluded using `.gitignore`
* Only essential project files are uploaded

---

## 👨‍💻 Author

**Parimala.S**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
