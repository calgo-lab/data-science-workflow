# Lecture 8: Matrix Factorization & AutoRec

## Part 1 — SVD (from scratch)
- Motivation: raw vectors are sparse and noisy — discover latent structure
- Matrix factorization: decompose R ≈ U · Sigma · V^T
- Truncated SVD: low-rank approximation
- SGD with regularization (from scratch)
- Key insight: rows of U and V are user/item embeddings in the same latent space

## Part 2 — AutoRec (with RecBole)
- AutoRec: the neural version of SVD — compress sparse rating vector through an autoencoder, reconstruct to fill missing entries
- Train loss only on observed ratings (mask out missing)
- RecBole introduction: train AutoRec on MovieLens with a few lines of config
- Compare SVD vs. AutoRec metrics — students see the linear-to-neural transition

**Practice:** SVD from scratch on MovieLens, then train AutoRec in RecBole, compare reconstruction quality and recommendation metrics
