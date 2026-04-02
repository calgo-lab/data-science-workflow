# Lecture 10: Two-Tower, Evaluation & Retrieval

## Part 1 — Two-Tower Architecture
- Two-Tower architecture: separate user and item encoders, dot-product scoring
- **Collaborative baseline (RecBole):** Train DSSM on MovieLens ratings via RecBole — ratings-only, no multimodal
- **Multimodal two-tower (custom PyTorch):** Image tower (pre-trained ResNet/ViT on TMDB posters) + text/interaction tower (user or plot embeddings), contrastive/dot-product loss to align both towers into a shared embedding space
- Why not RecBole for multimodal? RecBole consumes pre-extracted features — cannot train encoders end-to-end
- Extract learned embeddings → load into ChromaDB
- Key insight: the vector DB doesn't care where embeddings come from (text vs. collaborative vs. multimodal) — it just indexes and retrieves

## Part 2 — Evaluation & Method Comparison
- Metrics: Precision@k, Recall@k
- Compare all methods on the same test set: content-based (L7) vs. SVD/AutoRec (L8) vs. neural embeddings (L9) vs. collaborative two-tower (RecBole) vs. multimodal two-tower (custom PyTorch)
- Cold-start evaluation: held-out items — which method still works?

## Cluster demo
- kubectl, GPU access, batch embedding on MovieLens 25M

**Practice:** Mini final project — embed dataset, generate recommendations with 2+ methods, compare P@k/R@k, interpret results
