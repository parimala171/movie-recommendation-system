import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("movies.csv", low_memory=False)

# Select important columns
df = df[['title', 'overview']].dropna()

# Text vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(df['overview']).toarray()

# Similarity matrix
similarity = cosine_similarity(vectors)

# Save data
df.to_csv("cleaned_data.csv", index=False)

# Save model
pickle.dump(similarity, open("similarity.pkl", "wb"))
pickle.dump(df, open("model.pkl", "wb"))

print("Movie Recommendation Model Ready!")