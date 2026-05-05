from __future__ import annotations

import os

import requests
import streamlit as st

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8008")

st.set_page_config(page_title="DSW Spam Demo", page_icon="📧")
st.title("DSW Spam Detection Demo")
st.write("A tiny example for showing a spam classifier workflow. Uses deterministic random predictions to simulate a model.")


def fetch_random_email() -> dict[str, str]:
    response = requests.get(f"{BACKEND_URL}/sample", timeout=5)
    response.raise_for_status()
    return response.json()

if "email" not in st.session_state:
    try:
        st.session_state.email = fetch_random_email()
    except requests.RequestException as exc:
        st.error(f"Backend request failed: {exc}")
        st.stop()

if st.button("Generate random email"):
    try:
        st.session_state.email = fetch_random_email()
    except requests.RequestException as exc:
        st.error(f"Backend request failed: {exc}")
    st.rerun()

st.subheader("Message")
title = st.text_input("Title", value=st.session_state.email["subject"])
body = st.text_area("Body", value=st.session_state.email["body"])
spam_probability = st.slider("Spam probability", 0.0, 1.0, 0.5, 0.05)

if st.button("Predict"):
    st.session_state.email = {"subject": title, "body": body}
    try:
        response = requests.post(
            f"{BACKEND_URL}/predict",
            json={"subject": title, "body": body, "spam_probability": spam_probability},
            timeout=5,
        )
        response.raise_for_status()
        result = response.json()
        prediction = result["prediction"]

        if prediction == "Spam":
            st.error(f"Prediction: {prediction}")
        else:
            st.success(f"Prediction: {prediction}")
    except requests.RequestException as exc:
        st.error(f"Backend request failed: {exc}")
