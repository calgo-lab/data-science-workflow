#dsa

## Überblick

Leos Teil: Von der Recommendation-Problemstellung über Vektorrepräsentationen und Matrix-Faktorisierung hin zu modernen Embeddings und Vektor-Datenbanken. Fokus liegt auf dem roten Faden: **Daten → Vektoren → Latent Space → Retrieval at Scale**.

**Cold Start als roter Faden:** eingeführt (L6) → teilweise gelöst durch Content-based (L7) → scheitert bei MF (L8) → gelöst durch Neural Embeddings (L9) → quantitativ evaluiert (L10)

**Format:** Jede Lecture = 3 Stunden (1.5h Vorlesung + 1.5h Hands-on Practice)

**Slides:** [[lecture-06-the-recommendation-problem|Lecture 6]] · [[lecture-07-content-based-methods|Lecture 7]] · [[lecture-08-matrix-factorization|Lecture 8]] · [[lecture-09-neural-embeddings|Lecture 9]] · [[lecture-10-vector-databases-and-retrieval|Lecture 10]]

**Quelle:** Gekürzt & modernisiert aus Prof. Dr. Erdelt, BHT RS Vorlesung SoSe 2024 (RecommenderSystems-1 bis -5.pdf)

Lectures 1-5 (Felix): siehe [[dsa course structure from Felix]]

---

## Lecture 6: The Recommendation Problem

**Ziel:** Problem-Framing — was lösen wir und warum ist es schwer?

- Was ist Recommendation? Systeme, die Interesse aus Daten ableiten
- **Datentypen:** ordinale Daten (Ratings, Likert-Skalen), Text (Reviews, Beschreibungen), Bilder (Produktfotos) — jeder Typ bringt eigene Repräsentations-Herausforderungen
- **Rating-Matrizen:** explizites vs. implizites Feedback
- **Kernprobleme:** Sparsity (meiste Einträge fehlen), Cold Start (neue User/Items), Long Tail (Popularitäts-Bias)
- **Evaluation:** Relevanz, Diversität, Serendipity, Explainability — werden in Lecture 10 quantitativ wieder aufgegriffen

**Practice (1.5h):** MovieLens 100K laden, Rating-Matrix bauen, Sparsity berechnen, Long-Tail-Plot, Cold-Start User/Items identifizieren, Heatmap der Rating-Matrix

**Material:** [[dsa legacy slides]] Part I & II

---

## Lecture 7: Content-Based Methods — Datenpunkte als Vektoren

**Ziel:** Die Vektor-Perspektive einführen — alles ist ein Punkt im Raum

- **Feature-Matrizen:** Items und User als Vektoren von Attributen
- **Von Daten zu Vektoren:** Text (TF-IDF/BoW), Bilder (einfache Features), tabellarische Daten → numerische Vektoren
- **Vektoren vergleichen:** Cosine Similarity (Winkel), Euklidische Distanz (Betrag), Dot Product (Projektion) — geometrische Intuition
- **Content-based Recommender bauen:** User-Profil-Vektor mit Item-Vektoren matchen
- **Cold Start:** Funktioniert für neue Items (haben Features), scheitert bei neuen Usern (kein Profil)
- **Limitierungen:** Curse of Dimensionality (kurz), Feature-Engineering-Bottleneck, keine Serendipity

**Practice (1.5h):** Item-Feature-Matrix aus MovieLens-Genres bauen, Pairwise Cosine Similarity, "Because you liked The Matrix" → Top-5, User-Profil-Vektor bauen, Cosine vs. Euclidean vergleichen

**Material:** [[recommenderSystems_content_based_methods]], [[vector similarity and distances (Dot - inner product)]], [[dsa legacy slides]] Part III

---

## Lecture 8: Matrix Factorization & Latent Factor Models

**Ziel:** Von handgemachten Features zu entdeckten Features durch Dimensionsreduktion

- **Motivation:** Warum nicht einfach rohe Vektoren vergleichen? Sparsity, Rauschen, und der Wunsch nach latenter Struktur
- **Collaborative Filtering Idee:** User, die in der Vergangenheit übereinstimmten, werden es wieder tun (kurz)
- **Matrix-Faktorisierung:** User-Item-Matrix in zwei niedrig-rangige Matrizen zerlegen (U × V^T)
- **SVD:** A = UΣV^T, Low-Rank-Approximation, Truncated SVD
- **Optimierung:** Gradient Descent und ALS mit Regularisierung
- **Kernaussage:** Die Zeilen von U und V sind Vektorrepräsentationen (Embeddings!) von Usern und Items in einem gemeinsamen latenten Raum
- **Transduktiv vs. Induktiv:** MF = Lookup-Tabelle für bekannte IDs → neue User/Items haben keinen Vektor (Cold Start scheitert). Das motiviert den Sprung zu Neural Embeddings in Lecture 9

**Practice (1.5h):** numpy SVD auf Rating-Matrix, Singular Values visualisieren, Rekonstruktion mit k=5/10/50, SGD-basierte Matrix-Faktorisierung from scratch, Training Loss plotten, User/Item-Embeddings in 2D visualisieren (PCA)

**Material:** [[singular value decomposition SVD]], [[matrix factorization and embeddings]], [[dsa legacy slides]] Part IV & V

---

## Lecture 9: Von Matrix-Faktorisierung zu Neural Embeddings

**Ziel:** Von SVD-Embeddings zu modernen Neural-Embeddings — und warum sie Cold Start lösen

- **Brücke:** SVD gab uns Embeddings — aber neuronale Netze liefern bessere (Word2Vec → Sentence Transformers, CNNs → CLIP für Bilder)
- **Induktive Embeddings:** Jeder Text / jedes Bild kann embedded werden, auch für ungesehene Items → Cold Start gelöst
- **Hands-on:** Text-Embeddings mit Sentence Transformers erzeugen, semantische Suche
- **Multimodal:** CLIP — Text und Bilder im selben Vektorraum
- **Two-Tower Architektur (Ausblick):** User-Tower + Item-Tower → Dot Product, vereint Content-based (L7) und Collaborative (L8). In L10: Collaborative Baseline via RecBole (DSSM), multimodales End-to-End Training (Image + Text Tower) in custom PyTorch — RecBole kann keine Encoder end-to-end trainieren
- **Visualisierung:** PCA/t-SNE des Embedding-Raums

**Practice (1.5h):** (A) Text-Embeddings mit sentence-transformers generieren, semantische Ähnlichkeit; (B) Alle Movies embedden, PCA/t-SNE Visualisierung; (C) Semantische Suche (brute-force Cosine), SVD vs. Neural Embeddings vergleichen

**Material:** [[Sentence Transformers]], [[CLIP multimodal embeddings]], [[Two-Tower architecture]]

---

## Lecture 10: Vector Databases & Retrieval at Scale

**Ziel:** Embeddings speichern, effizient durchsuchen, und alle Ansätze quantitativ vergleichen

- **Skalierungsproblem:** Brute-Force-Suche über Millionen Vektoren skaliert nicht
- **HNSW:** Hierarchische Graph-basierte Approximate Nearest Neighbor Suche
- **ChromaDB:** Embeddings + Metadaten speichern, Similarity Queries, Index-Konfiguration
- **Batch-Embedding auf GPU:** Vollständigen MovieLens 25M Datensatz auf dem Cluster embedden
- **Query-Benchmarking:** Brute-Force vs. HNSW-indexiert
- **Evaluation:** Precision@k, Recall@k, MRR
- **Vergleich:** Content-based (L7) vs. MF (L8) vs. Neural Embeddings (L9) auf demselben Test-Set
- **Cold-Start-Evaluation:** Held-out Items, die nicht im Training waren

**Practice (1.5h):** (A) Batch-Embedding auf GPU, ChromaDB aufsetzen und befüllen; (B) HNSW-Parameter tunen (M, ef_construction), Query-Benchmark; (C) Evaluation mit held-out Test-Set (P@k, R@k), Vergleich CB vs. MF vs. Neural, Cold-Start-Test

### Idee: Gemeinsames Abschlussprojekt mit Felix' Teil

Die beiden Kurshälften ergeben zusammen eine natürliche End-to-End Data Science Pipeline:

```
Felix (Lectures 1-5)                    Leo (Lectures 6-10)
─────────────────────                   ─────────────────────
Data Acquisition (Scraping/API)    →
Data Quality & Cleaning            →
Data Exploration                   →
                                        Vektorisierung & Embeddings
                                        Speicherung in Vector DB
ML Pipeline / AutoML               →    Retrieval & Evaluation auf Cluster
```

**Möglicher Projektrahmen:** Studierende bauen eine vollständige Pipeline — von der Datenakquise (Felix) über Qualitätssicherung und Exploration bis hin zur Embedding-Erzeugung, Speicherung in einer Vektor-Datenbank und skalierbarem Retrieval auf dem Cluster (Leo). Das Abschlussprojekt könnte beide Teile als eine zusammenhängende Aufgabe verbinden, z.B.:
- Einen domänenspezifischen Datensatz scrapen und bereinigen (Felix)
- Embeddings generieren, in ChromaDB indexieren, und ein Retrieval-System auf dem Cluster deployen (Leo)
- Evaluation der gesamten Pipeline end-to-end

