# Stock Market Sentiment Classifier
Stock market sentiment data is collected from Kaggle. Various data preprocessing techniques are performed on the data and machine learning algorithm is used for classification.

## What is Sentiment Analysis?
Sentiment analysis is a natural language processing (NLP) technique used to determine the sentiment, emotion, or opinion expressed in a piece of text. Its goal is to understand the attitude or feeling conveyed by the words within the text.

## Tools used:
1. Python
2. Pandas
3. Numpy
4. Nltk
5. BeautifulSoup
6. Scikit-learn
7. difflib.

## Data Cleaning
1. Replace certain special characters with their string equivalents.
2. Replacing some numbers with string equivalents (not perfect, can be done better to account for more cases).
3. Removing HTML tags.
4. Remove punctuations.
5. Expanding  contractions words.

## Some New Features
1. No of sentence present in a text.
2. How many numerical values are containing by each sentence.
3. Number of words present in sentence column.
4. Count of stopwords of a sentence.
5. length of a sentence 
6. Total word count

## Data Preprocessing
CountVectorizer method is used to convert the words into vector.

## Model Training
Random Forest Classifier algorithm is used to train the model.
