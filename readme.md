Email Spam Classifier
Project Overview
The Email Spam Classifier project applies machine learning and natural language processing concepts to automatically detect and classify email messages as spam or non-spam (ham). It demonstrates the entire workflow from data loading and preprocessing to model-ready dataset preparation.

Features
Loading and exploring the email dataset with dataset statistics

Text preprocessing including cleaning, tokenization, and stopword removal

Splitting dataset into training and testing for model evaluation

Modular Python implementation with logging and error handling

Technologies/Tools Used
Python 3

pandas, numpy for data manipulation

NLTK for text processing (tokenization, stopword removal)

scikit-learn for dataset splitting and model preparation

Logging module for debugging and progress tracking

Steps to Install and Run
Install Python 3.x and required libraries:

text
pip install pandas numpy nltk scikit-learn
Download NLTK datasets:

python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
Place your email dataset CSV file (or use the sample generator) in the project directory.

Run data_loader.py to load and explore the dataset.

Use preprocessor.py to preprocess the emails before model training.

Testing Instructions
Split the dataset using the provided function in data_loader.py

Use the processed data for training and testing classification models

Monitor logs for data loading, preprocessing, and splitting status

