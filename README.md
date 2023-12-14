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

### How CountVectorizer Works?
The CountVectorizer is a technique used in natural language processing (NLP) for converting a collection of text documents into a matrix of token counts. It's a fundamental tool for text preprocessing before applying machine learning algorithms. 

**Here's how it generally works:**

*1. Breaking Text into Tokens:* The CountVectorizer breaks down the text into individual words or tokens. This process is known as tokenization. It also handles n-grams, which are sequences of words (bi-grams for two words, tri-grams for three words, etc.) as specified by the user.

*2. Building the Vocabulary:* It creates a vocabulary of unique words present in the entire corpus (collection of documents). Each unique word becomes a feature.

*3. Counting Occurrences:* For each document in the corpus, CountVectorizer counts the frequency of each word (or n-gram) in the vocabulary within that document. This results in a matrix where each row corresponds to a document, and each column corresponds to a unique word in the vocabulary. The matrix represents the count of each word's occurrence in each document.

*Example:*

Suppose you have three documents:

Document 1: "I love coding."

Document 2: "Coding is fun."

Document 3: "Python is for coding."

*The CountVectorizer will:*

Create a vocabulary of unique words: ["I", "love", "coding", "is", "fun", "Python", "for"]

*Generate a matrix representation:*

| Document | I | love | Coding | is | fun | Python | for|
| ------ | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Document 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| Document 2 | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| Document 3 | 0 | 0 | 1 | 1 | 0 | 1 | 1 |

## Model Training
Random Forest Classifier algorithm is used for trainining.
### How Random Forest Classifier Works?
Random forest is an ensemble bagging learning method. A decision tree is like a structured algorithm that divides the whole dataset into branches, which again split into branches and finally get a leaf node that can't be divided. Random forests creates multiple numbers of decision trees and these trees are called a forest. It means in decision tree we create one tree but in a random forest we create multiple trees and because there are too many trees so it is called a forest. To build a machine learning model the whole dataset is divided into train and test. Random forest takes data points from the training dataset and data points are taken randomly that's why it is called random forest.

![Random Forest Classifier](https://github.com/Rafsun001/strock_market_sentiment_classification/blob/main/Random%20Forest%20Classifier.png?raw=true )

Suppose there are 100 records in a dataset. Randomly take 25 records from that dataset and create a new small dataset or one bag, then again randomly take 25 data from the main dataset and create a 2nd bag or new dataset. Bags or new datasets will be created like this according to needs. Remember one thing, this selection is called replacement selection. It means that after creating one bag or one dataset from a random selection of data from the original dataset, the data you selected will go back in the main dataset again, and then again a new bag or new dataset will be created. It means bags can have duplicate records. It means the number one bag and number two bag can have the same records. Same records means all the data can't be the same, some data can be the same like number 1 record of the main dataset is present in all the bags or some bags and it also can be possible that number 1 record is present in only one bag. After creating the bags or small datasets the number of decision trees will be used equally to the number of bags or datasets. If 5 bags or mini datasets are created then 5 decision tree models will be used. After completing the training each model will give an output. Then combine all those model outputs and then do vote. which output is mostly predicted is the final output.
