from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag

nltk.download('punkt')
nltk.download('stopwords')

model = pickle.load(open('stock_mdl2.pkl', 'rb'))

vectorizer = CountVectorizer()

app = Flask(__name__)

@app.route('/')
def verifier_ui():
    return render_template('index.html')

df = pd.read_excel("myData.xlsx")
df = df.dropna(subset=['Sentences'])
X_train = df['Sentences']
vectorizer.fit(X_train)


@app.route('/usa_info_vari', methods=['POST'])
def recommend():
    try:
        input_dt = request.form.get('user_input')

        def preprocess(q):
            q = str(q).lower().strip()
            q = q.replace('%', ' percent')
            q = q.replace('$', ' dollar ')
            q = q.replace('₹', ' rupee ')
            q = q.replace('€', ' euro ')
            q = q.replace('@', ' at ')
            q = q.replace('(', '')
            q = q.replace(')', '')
            q = q.replace('-', ' ')
            
            contractions = {
                # ... your contractions dictionary
            }

            q_decontracted = []

            for word in q.split():
                if word in contractions:
                    word = contractions[word]

                q_decontracted.append(word)

            q = ' '.join(q_decontracted)
            q = q.replace("'ve", " have")
            q = q.replace("n't", " not")
            q = q.replace("'re", " are")
            q = q.replace("'ll", " will")
            
            # Use 'html.parser' and decode HTML entities
            q = BeautifulSoup(q, 'html.parser').get_text()

            return q

        sentence = preprocess(input_dt)

        # Tokenize the sentence into words
        words = word_tokenize(sentence)

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word.lower() not in stop_words]

        # Perform Part-of-Speech tagging
        tagged_words = pos_tag(filtered_words)

        # Extract words based on their POS tags
        verbs = [word for word, tag in tagged_words if tag.startswith('VB')]
        adverbs = [word for word, tag in tagged_words if tag.startswith('RB')]
        nouns = [word for word, tag in tagged_words if tag.startswith('NN')]
        adjectives = [word for word, tag in tagged_words if tag.startswith('JJ')]

        tmp_li = ""
        for j in sentence.split():
            if j in verbs or j in adverbs or j in nouns or j in adjectives:
                tmp_li = tmp_li + " " + str(j)
            else:
                pass

        X_input = vectorizer.transform([tmp_li])

        prediction = model.predict(X_input)

        if prediction == 1:
            return render_template('index.html', prediction_text="Positive sentiment")
        else:
            return render_template('index.html', prediction_text="Negative sentiment")

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run()
