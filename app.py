import streamlit as st
import whisper
from gtts import gTTS
import os

st.title("AI IVR System")
st.write("Upload an audio file and interact with the AI IVR.")

uploaded_file = st.file_uploader(
    "Upload audio",
    type=["mp3", "wav", "m4a"]
)

if uploaded_file is not None:

    st.success("Audio uploaded successfully!")

    # Save uploaded audio
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.read())

    # Load Whisper model
    model = whisper.load_model("base")

    # Speech-to-Text
    result = model.transcribe("temp_audio.wav")

    text = result["text"]

    st.subheader("Transcribed Text")
    st.write(text)

    # Convert to lowercase for intent matching
    query = text.lower()

    # Rule-based IVR responses
    if "balance" in query:
        response = (
            "Your account balance information is currently unavailable. "
            "Please contact customer support."
        )

    elif "loan" in query:
        response = (
            "For loan related queries, please contact our loan department "
            "at 1800-123-4567."
        )

    elif "credit card" in query:
        response = (
            "Your credit card request has been forwarded to our support team."
        )

    elif "hello" in query or "hi" in query:
        response = (
            "Hello! Welcome to our AI IVR system. "
            "How may I help you today?"
        )

    elif "support" in query or "customer care" in query:
        response = (
            "Our customer support team is available 24 hours a day. "
            "Please call 1800-111-2222."
        )

    else:
        response = (
            "I'm sorry, I couldn't understand your request. "
            "Please try again."
        )

    st.subheader("AI Response")
    st.write(response)

    # Text-to-Speech
    tts = gTTS(response)
    tts.save("response.mp3")

    # Play audio response
    audio_file = open("response.mp3", "rb")
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/mp3")