# Final Project: Recommendation Application

## Overview

Build an application that generates recommendations for a domain of your choice. You choose the dataset, the methods, and the form of the application. The goal is to demonstrate that you can take raw data, represent it as vectors, and build a system that returns relevant items — and that you can evaluate how well it works.

## Required Components

### 1. Dataset
- Choose a dataset relevant to your use case (e.g., movies, articles, products, music, recipes, ...)
- Sources: web scraping, APIs, Kaggle, public datasets, or data from Felix's sessions
- Document where the data comes from and how it was collected
- Analyze the dataset: How many items? How sparse? Are there cold-start items?

### 2. Vectorization
- Represent your items as vectors using **at least one** embedding method:
  - Content-based features (TF-IDF, one-hot encoding, manual feature vectors)
  - Matrix factorization (SVD, SGD-based)
  - Neural embeddings (Sentence Transformers, autoencoders, or similar)
  - Any other method you can justify (AutoML, CLIP, fine-tuned models, ...)
- Explain your choice: why does this method fit your data?

### 3. Recommendation System
- Build a system that takes an input (user profile, item, or text query) and returns relevant recommendations
- The system must actually work — demonstrate it with concrete examples
- Store and retrieve embeddings using a vector database (e.g., ChromaDB) or a simple similarity search

### 4. Evaluation
- Compare **at least 2 different methods** on the same dataset using quantitative metrics:
  - Precision@k, Recall@k (required)
  - Additional metrics welcome (MRR, nDCG, diversity, ...)
- Use a proper train/test split — do not evaluate on training data
- Show the results in a clear comparison (table, chart, or both)
- **Discuss:** Why does one method outperform the other? In which cases does it fail?

## Presentation Format

Present your project as a **pitch** (approx. 15 min + 5 min questions):
- What problem are you solving? Who would use this?
- How does your system work? (short technical walkthrough)
- How well does it work? (evaluation results)
- What would you improve with more time?

Deliverables: Jupyter notebook(s) + short presentation slides.

## Grading Criteria

| Dimension | Weight | What we look for |
|---|---|---|
| **Data Preparation** | 20% | Dataset is well-chosen, clean, and appropriately analyzed (sparsity, distributions, cold-start items identified) |
| **Methodology** | 30% | Embedding and recommendation methods are correctly implemented and appropriate for the data. Code is clear and reproducible. |
| **Evaluation** | 30% | At least 2 methods compared quantitatively. Proper test set. Results are presented clearly and discussed critically. |
| **Reflection & Presentation** | 20% | Student understands *why* results look the way they do. Strengths and limitations are discussed honestly. Presentation is clear and well-structured. |

### Joint grading with Felix (if applicable)

If your project uses data from Felix's sessions (scraping, APIs, data cleaning), Felix may co-evaluate:
- Data acquisition pipeline (scraping/API, data quality, cleaning)
- Cluster integration (deployment, scalability)
- Dashboard or API (if applicable)

In this case, Leo grades the recommendation and evaluation components, Felix grades the data pipeline components.

## Ideas for Datasets & Use Cases

These are suggestions — you are free to choose anything:

| Use Case | Data Source | Interesting Because |
|---|---|---|
| Movie recommender | MovieLens + TMDB API | Multimodal (text + poster images) |
| News recommender | Scraped articles (Felix's part) | Text embeddings + category-based evaluation |
| Music discovery | Spotify API / Last.fm | Audio features + collaborative signals |
| Recipe finder | Scraped recipe sites | Ingredient vectors + semantic search |
| Academic paper search | Semantic Scholar API | Citation-based vs. text-based similarity |
| Product recommendations | Amazon reviews / H&M dataset | Large-scale, real user interactions |
| Job matching | LinkedIn/Indeed scraping | Bidirectional: job ↔ candidate embeddings |

## Timeline

| Week | Milestone |
|---|---|
| After Lecture 8 | Dataset chosen, initial exploration done |
| After Lecture 9 | First embeddings generated, basic recommendation working |
| After Lecture 10 | Evaluation complete, at least 2 methods compared |
| Presentation week | Final notebook + slides + pitch |

## Rules

- Teams of 1–3 students
- All code must be in Jupyter notebooks and run reproducibly
- Do not commit API keys or credentials to your repository
- Using LLMs for code assistance is allowed — but you must understand and be able to explain every line
- Plagiarism or submitting another team's work will result in a failing grade
