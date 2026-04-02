# Lectures 6–10: Recommender Systems, Embeddings & Retrieval

**Dozent:** Leo | **Format:** 3h pro Session (1.5h Vorlesung + 1.5h Practice)

## Roter Faden

```
L6 Problem  →  L7 Vektoren  →  L8 Gelernte Embeddings  →  L9 Neural Embeddings  →  L10 Evaluation
```

Durchgängiges Thema **Cold Start:** eingeführt (L6) → teilweise gelöst (L7) → scheitert bei MF (L8) → gelöst durch Neural Embeddings (L9) → quantitativ evaluiert (L10)

**Datensatz:** MovieLens durchgehend — Ratings + Genres (L6–L8), + TMDB Plot-Summaries (L9), + Scale 25M + Poster auf Cluster (L10)

---

### L6 — The Recommendation Problem
Problemstellung: Rating-Matrizen, explizites vs. implizites Feedback, Sparsity, Cold Start, Long Tail.
**Practice:** MovieLens erkunden und Kernprobleme identifizieren.

### L7 — Content-Based Methods
Items als Vektoren darstellen (Genre-One-Hot, TF-IDF), Cosine Similarity, Content-based Recommender bauen.
**Practice:** Similarity berechnen, "Because you liked X" Recommender bauen.

### L8 — Matrix Factorization & Learned Embeddings
Rating-Matrix zerlegen (SVD, SGD), latente Embeddings lernen. Kurze Autoencoder-Demo als nicht-linearer Nachfolger.
**Practice:** SVD/SGD anwenden, aus gelernten Embeddings Empfehlungen generieren.

### L9 — Neural Embeddings & Semantische Suche
Sentence Transformers, ChromaDB als einfaches Tool, semantischen Recommender bauen. Cold Start gelöst.
**Practice:** Text-Embeddings erzeugen, Recommender bauen, Cold-Start testen.

### L10 — Evaluation & Methodenvergleich
Precision@k, Recall@k. Content-based vs. MF vs. Neural auf demselben Test-Set vergleichen. Cluster-Einführung (kubectl, GPU). Bonus: Contrastive Training Demo.
**Practice:** Mini-Finalprojekt — 2 Methoden vergleichen, Ergebnisse diskutieren.

---

### Abschlussprojekt
Eigener Datensatz, Recommendation-Anwendung bauen, mind. 2 Methoden quantitativ vergleichen. Details: `requirements.md`
