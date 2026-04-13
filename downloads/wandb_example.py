from __future__ import annotations

import os

import numpy as np
import wandb
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def main() -> None:
    # OpenML dataset (as in Session 1)
    X, y = fetch_openml("iris", version=1, as_frame=False, return_X_y=True)

    # Data split
    x_train, x_val, y_train, y_val = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    # Standardize features
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_val = scaler.transform(x_val)

    # Parameters
    loss_fn = "log_loss"
    learning_rate = 0.05
    alpha = 1e-4
    seed = 42
    epochs = 15

    # Simple model
    classifier = SGDClassifier(
        loss=loss_fn,
        learning_rate="constant",
        eta0=learning_rate,
        alpha=alpha,
        random_state=seed,
    )
    classes = np.unique(y_train)

    # W&B run metadata shows what this script is doing.
    run = wandb.init(
        project="openml-mini-demo",
        name="iris-sgd",
        mode=os.getenv("WANDB_MODE", "online"),
        config={
            "dataset": "iris",
            "loss_fn": loss_fn,
            "learning_rate": learning_rate,
            "alpha": alpha,
            "seed": seed,
            "epochs": epochs          
        }
    )

    # Train for a few epochs and log metrics after each pass
    for epoch in range(1, epochs + 1):
        classifier.partial_fit(x_train, y_train, classes=classes)

        # Compute metrics so W&B can plot them over time
        train_proba = classifier.predict_proba(x_train)
        val_proba = classifier.predict_proba(x_val)

        train_loss = log_loss(y_train, train_proba)
        val_loss = log_loss(y_val, val_proba)
        train_accuracy = accuracy_score(y_train, classifier.predict(x_train))
        val_accuracy = accuracy_score(y_val, classifier.predict(x_val))

        # Log metrics to W&B
        wandb.log(
            {
                "epoch": epoch,
                "train/loss": train_loss,
                "val/loss": val_loss,
                "train/accuracy": train_accuracy,
                "val/accuracy": val_accuracy,
            },
            step=epoch,
        )

        print(
            f"epoch={epoch:02d} train_loss={train_loss:.4f} "
            f"val_loss={val_loss:.4f} val_accuracy={val_accuracy:.3f}"
        )

    run.finish()


if __name__ == "__main__":
    main()