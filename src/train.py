import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

from preprocess import clean_text

# Load dataset
df = pd.read_csv("data/spam.csv", encoding="latin-1")

# Rename columns
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# Clean text
df['message'] = df['message'].apply(clean_text)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['message'],
    df['label'],
    test_size=0.2,
    random_state=42
)

# Model
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

# Train
model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

# Save model
joblib.dump(model, "models/spam_classifier.pkl")

print("Model Saved Successfully!")