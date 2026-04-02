#dsa

## Überblick

Leos Teil: Von der Recommendation-Problemstellung über Vektorrepräsentationen und Matrix-Faktorisierung hin zu modernen Embeddings und Vektor-Datenbanken. Fokus liegt auf dem roten Faden: **Daten → Vektoren → Latent Space → Retrieval at Scale**.

**Cold Start als roter Faden:** eingeführt (L6) → teilweise gelöst durch Content-based (L7) → scheitert bei MF (L8) → gelöst durch Neural Embeddings (L9) → quantitativ evaluiert (L10)

**Format:** Jede Lecture = 3 Stunden (1.5h Vorlesung + 1.5h Hands-on Practice)

**Slides:** [[lecture-06-the-recommendation-problem|Lecture 6]] · [[lecture-07-content-based-methods|Lecture 7]] · [[lecture-08-matrix-factorization|Lecture 8]] · [[lecture-09-neural-embeddings|Lecture 9]] · [[lecture-10-vector-databases-and-retrieval|Lecture 10]]

**Datensatz:** MovieLens durchgehend, schrittweise angereichert:
- L6–L8: ml-latest-small (Ratings + Genres) — Studenten lernen den Datensatz kennen
- L9: + TMDB Plot-Summaries (per API) — zeigt den Mehrwert von Text-Embeddings gegenüber Genre-Vektoren
- L10: ml-25m auf dem Cluster (Scale) + TMDB Poster für multimodale Demo

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

## Lecture 8: Matrix Factorization & Learned Embeddings

**Ziel:** Von handgemachten Features zu gelernten Features — lineare und nicht-lineare Dimensionsreduktion

- **Motivation:** Rohe Vektoren sind sparse und verrauscht — wir wollen latente Struktur entdecken
- **Collaborative Filtering Idee:** User, die in der Vergangenheit übereinstimmten, werden es wieder tun (kurz)
- **Matrix-Faktorisierung:** User-Item-Matrix in zwei niedrig-rangige Matrizen zerlegen (U × V^T)
- **SVD:** A = UΣV^T, Low-Rank-Approximation, Truncated SVD
- **Optimierung:** SGD mit Regularisierung (from scratch)
- **Kernaussage:** Die Zeilen von U und V sind Embeddings von Usern und Items im selben latenten Raum
- **Autoencoder (kurze Demo, ~20 min):** Nicht-linearer Nachfolger von SVD — Encoder-Decoder auf die Rating-Matrix, vergleich mit SVD-Rekonstruktion
- **Transduktiv vs. Induktiv:** MF/Autoencoder = Lookup-Tabelle für bekannte IDs → neue User/Items haben keinen Vektor (Cold Start scheitert). Motiviert den Sprung zu Neural Embeddings in L9

**Practice (1.5h):** Kleine Matrix von Hand faktorisieren (M=XY), SVD auf echten Daten mit Varianzanalyse, SGD-Training from scratch, Empfehlungen aus gelernten Embeddings generieren

**Material:** [[singular value decomposition SVD]], [[matrix factorization and embeddings]], [[dsa legacy slides]] Part IV & V

---

## Lecture 9: Neural Embeddings & Semantische Suche

**Ziel:** Von SVD-Embeddings zu modernen Neural-Embeddings — Cold Start lösen und einen funktionierenden Recommender bauen

- **Brücke:** SVD/Autoencoder gaben uns Embeddings — neuronale Netze liefern bessere (Word2Vec → Sentence Transformers)
- **Induktive Embeddings:** Jeder Text kann embedded werden, auch für ungesehene Items → Cold Start gelöst
- **Hands-on:** Text-Embeddings mit Sentence Transformers erzeugen, semantische Suche bauen
- **ChromaDB als Tool:** Embeddings speichern und abfragen in 5 Zeilen (Client, Collection, Add, Query) — kein Deep-Dive in DB-Interna
- **Contrastive Training (Ausblick):** Wie werden Embedding-Modelle trainiert? Kurze Erklärung des Prinzips (similar pairs close, dissimilar pairs far)

**Practice (1.5h):** (A) Text-Embeddings generieren, semantische Ähnlichkeit testen; (B) Recommender bauen: alle Movies embedden, ChromaDB befüllen, Empfehlungen für User generieren; (C) Cold-Start-Test: neuen Film erfinden, ähnliche finden

**Material:** [[Sentence Transformers]], [[CLIP multimodal embeddings]]

---

## Lecture 10: Evaluation, Methodenvergleich & Cluster

**Ziel:** Alle Ansätze quantitativ vergleichen, den Cluster nutzen, und das Gesamtbild für das Finalprojekt schließen

- **Cluster-Einführung:** kubectl, GPU-Zugang, Batch-Embedding auf dem vollständigen MovieLens 25M Datensatz
- **Evaluation:** Precision@k, Recall@k — wie gut sind unsere Empfehlungen wirklich?
- **Methodenvergleich:** Content-based (L7) vs. MF/Autoencoder (L8) vs. Neural Embeddings (L9) auf demselben Test-Set
- **Cold-Start-Evaluation:** Held-out Items — welche Methode funktioniert trotzdem?
- **Bonus: Contrastive Training Demo** — Paar-Konstruktion, Cosine Similarity Loss, Before/After Visualisierung

**Cluster-Demo (`lecture-10-cluster-demo.ipynb`):** Live-Demonstration auf GPU — multimodales Two-Tower Training in PyTorch: Image-Tower (ResNet/ViT auf TMDB Postern) + Text-Tower, contrastive Loss, Embeddings im selben Raum (CLIP-Prinzip). RecBole dient als Collaborative-Baseline (DSSM, nur Ratings), kann aber kein End-to-End Encoder-Training

**Practice (1.5h):** Mini-Version des Finalprojekts — eigenen Datensatz (oder MovieLens) embedden, Empfehlungen generieren, 2 Methoden vergleichen (P@k/R@k), Ergebnisse interpretieren

### Abschlussprojekt

Studierende wählen einen eigenen Datensatz (oder nutzen den aus Felix' Teil) und bauen darauf eine Anwendung, die Empfehlungen generieren kann. Viel Gestaltungsfreiheit — bewertet werden klare Dimensionen, nicht spezifische Methoden.

**Pflichtbausteine:**

| Baustein | Was | Bezug |
|---|---|---|
| Datensatz | Eigener oder Felix' Datensatz, sauber aufbereitet | L6 (Sparsity/Cold Start analysieren) |
| Vektorisierung | Items als Embeddings darstellen (mind. 1 Methode) | L7–L9 |
| Empfehlung | System das für einen Input relevante Items zurückgibt | L9–L10 |
| Evaluation | Quantitativer Vergleich (P@k/R@k) von mind. 2 Methoden | L10 |

**Frei wählbar:** Datensatz-Quelle (Scraping, API, Kaggle, eigene Idee), Embedding-Methode (TF-IDF, SVD, Sentence Transformers, Autoencoder, AutoML …), Anwendungsform (Notebook, API, Dashboard), Use Case / "Startup-Pitch".

**Bewertungsdimensionen (Leo):**
1. Datenvorbereitung — sinnvoll gewählt und aufbereitet?
2. Methodik — Embedding-/Recommendation-Methoden korrekt angewandt?
3. Evaluation — quantitativer Vergleich, nicht nur "es funktioniert"?
4. Reflexion — warum ist Methode A besser/schlechter als B?

**Optional mit Felix (gemeinsame Bewertung):**
5. End-to-End Pipeline — von Datenakquise bis Empfehlung

```
Felix (Sessions 1–5)                    Leo (Lectures 6–10)
─────────────────────                   ─────────────────────
Data Acquisition (Scraping/API)    →
Data Quality & Cleaning            →
Data Exploration                   →
ML Pipeline / AutoML               →    Vektorisierung & Embeddings
                                        Speicherung in Vector DB
                                        Retrieval & Evaluation auf Cluster
```

Details: siehe `requirements.md`

