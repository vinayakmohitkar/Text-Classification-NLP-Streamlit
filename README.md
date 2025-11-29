# Text Classification NLP Streamlit App

## Overview
This project is a simple web app that classifies text (like tweets or reviews) into sentiment categories: positive, negative, or neutral. It uses machine learning models trained on real Twitter data and provides an easy-to-use interface built with Streamlit.

## Features
- Classifies text sentiment using Naive Bayes and Logistic Regression models
- User-friendly web interface
- Instant predictions and confidence scores


### Prerequisites
- Python 3.x

### Installation
1. Clone this repository or download the files.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the App
Start the Streamlit app with:
```
streamlit run app.py
```

## Usage
- Select a model from the sidebar.
- Enter your text in the input box.
- Click “Predict” to see the sentiment and confidence scores.

## Project Structure
- `app.py` – The main Streamlit app.
- `twittersentimentanalysis_nlp_project.py` – Script for training the models.
- `requirements.txt` – List of required Python packages.

## Data
The models were trained on a public Twitter sentiment dataset from Kaggle.


## Link to Streamlit APP 
https://text-classification-nlp-app-5wsrnhueuxnmwgbfh4kg53.streamlit.app/