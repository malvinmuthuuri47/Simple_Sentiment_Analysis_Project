from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from textblob import TextBlob
import time
from collections import OrderedDict

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse', methods=['POST'])
def analyse():
    start=time.time()
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        blob = TextBlob(rawtext)
        received_text = blob
        blob_sentiment, blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
        no_of_tokens = len(blob.words)

        # Extract unique nouns and adjectives using an OrderedDict to maintain Order
        unique_words = OrderedDict()
        for word, tag in blob.tags:
            if tag in ['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'] :
                unique_words[word.lemmatize()] = None
        
        # Convert the OrderedDict back to a list
        final_words = list(unique_words.keys())
        
        len_of_words = len(final_words)
        summary = final_words

        end = time.time()
        elapsed_time = "{:.2f}".format(end - start)

    return render_template(
        'index.html', received_text=received_text, number_of_tokens=no_of_tokens, blob_sentiment=blob_sentiment, blob_subjectivity=blob_subjectivity, summary=summary, elapsed_time=elapsed_time, raw_text=rawtext, len_of_words=len_of_words
    )

if __name__ == "__main__":
    app.run(debug=True)