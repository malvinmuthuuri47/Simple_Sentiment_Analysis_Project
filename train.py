from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

# Create a Custom Dataset
train_data = [
    ("I love this product!", "positive"),
    ("This product is terrible", "negative"),
    ("I'm not sure how I feel about this product.", "neutral")
]

# Train the classifier
c1 = NaiveBayesClassifier(train_data)

# Create a TextBlob Object with the custom classifier
text = "I'm not sure how I feel about this product."
blob = TextBlob(text, classifier=c1)

# get the sentiment
sentiment = blob.classify()
print("Sentiment: ", sentiment)