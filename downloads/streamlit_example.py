import numpy as np
import streamlit as st

def random_email():
	return {
		"subject": str(np.random.choice(["Urgent invoice update", "Meeting reminder", "Free gift card inside", "Account verification needed"])),
		"body": str(np.random.choice(["Please review the attached note.", "Click now to claim your prize.", "Open attachment for details.", "See details at your convenience."]))
	}

def model_predict(email, spam_probability):
    np.random.seed(hash(email.__str__()) % (2**8)) # Seed based on email content
    return np.random.choice(["Spam", "Not spam"], p=[spam_probability, 1 - spam_probability])

st.set_page_config(page_title="DSW Spam Demo", page_icon="📧")
st.title("DSW Spam Detection Demo")
st.write("A tiny example for showing a spam classifier workflow. Uses deterministic random predictions to simulate a model.")

if "email" not in st.session_state:
	st.session_state.email = random_email()

if st.button("Generate random email"):
	st.session_state.email = random_email()
	st.rerun()

st.subheader("Message")
title = st.text_input("Title", value=st.session_state.email["subject"])
body = st.text_area("Body", value=st.session_state.email["body"])
spam_probability = st.slider("Spam probability", 0.0, 1.0, 0.5, 0.05)

if st.button("Predict"):
    st.session_state.email = {"subject": title, "body": body}
    prediction = model_predict(st.session_state.email, spam_probability)
    
    if prediction == "Spam":
        st.error(f"Prediction: {prediction}")
    else:
        st.success(f"Prediction: {prediction}")