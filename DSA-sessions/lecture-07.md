# Lecture 7: Content-Based Methods

- Feature matrices: items and users as attribute vectors
- From data to vectors: text (TF-IDF / BoW), images, tabular data
- Comparing vectors: cosine similarity, euclidean distance, dot product — geometric intuition
- Building a content-based recommender: match user profile vector with item vectors
- Cold start: works for new items (they have features), fails for new users (no profile)
- Limitations: curse of dimensionality, feature engineering bottleneck, no serendipity

**Practice:** Build item-feature matrix from MovieLens genres, pairwise cosine similarity, "Because you liked The Matrix" top-5, user profile vector
