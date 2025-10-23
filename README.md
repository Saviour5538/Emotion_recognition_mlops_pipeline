# Emotion Recognition MLOps Pipeline

## Project Overview
This project implements an **Emotion Recognition Machine Learning pipeline** with an MLOps approach. It includes data preprocessing, feature engineering (Bag of Words), model training (Gradient Boosting Classifier), and saving/loading trained models for deployment. The project demonstrates a clean ML workflow for reproducibility and maintainability.

## Features
- Data preprocessing: text normalization, stopword removal, lemmatization, punctuation removal, URL removal.  
- Feature engineering: Bag-of-Words representation.  
- Model training: Gradient Boosting Classifier.  
- Model saving and loading with `pickle`.  
- Structured project layout suitable for MLOps workflows.  

## Project Structure

motion_recognition_mlops_pipeline/
│
├── data/
│ ├── raw/Raw datasets
│ ├── processed/ Cleaned datasets
│ └── features/Features like BOW matrices
│
├── src/ # Source code
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ └── model_building.py
│
├── model.pkl # Trained model
├── README.md
└── requirements.txt # Python dependencies



## Installation
Make sure you have Python 3.9+ installed. Then clone the repo and install dependencies:

```bash
git clone https://github.com/Saviour5538/Emotion_recognition_mlops_pipeline.git
cd Emotion_recognition_mlops_pipeline
pip install -r requirements.txt


Usage

Preprocess your data
python src/data_preprocessing.py


Generate features
python src/feature_engineering.py


Train the model
python src/model_building.py


Load and predict

import pickle
import pandas as pd
# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))
# Load your features
X_test = pd.read_csv('./data/features/test_bow.csv').iloc[:, :-1].values

# Make predictions
predictions = model.predict(X_test)
print(predictions)

Dependencies

numpy
pandas
scikit-learn
nltk

Generate a requirements.txt file with:

pip freeze > requirements.txt

Future Work

Incorporate deep learning models like LSTM or Transformers for higher accuracy.

Build a REST API for real-time emotion prediction.

Implement automated model versioning and CI/CD deployment.
