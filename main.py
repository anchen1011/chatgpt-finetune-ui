import streamlit as st
import string
import os
import json
import re
import webbrowser
import openai

st.set_page_config(page_title="Pathway Explorer", page_icon=":smiley:", layout="wide")

# Render the api key input and enter button
api_key = st.text_input('Enter your API key:', '')

# If api_key is entered, read the contents and process the data
if api_key.startswith('sk-'):
    openai.api_key = api_key
    st.title("OpenAI Fine Tuning Service")

    # File Operations
    st.subheader("File Operations")

    st.subheader("Upload a File")
    file_path = st.text_input("Enter a file path to upload")
    purpose = st.text_input("Enter a purpose for the file")
    if st.button("Upload File"):
        with open(file_path, "rb") as file:
            uploaded_file = openai.File.create(file=file, purpose=purpose)
            st.write("File Uploaded", uploaded_file)

    st.subheader("Delete a File")
    file_id = st.text_input("Enter a file ID to delete")
    if st.button("Delete File"):
        deleted_file = openai.File.delete(file_id)
        st.write("File Deleted:", deleted_file)

    # List Files
    st.subheader("List Files")
    if st.button("List Files"):
        files = openai.File.list()
        for file in files.data:
            st.write("File:", file)

    # Fine Tuning Job Operations
    st.subheader("Fine-tuning Job Operations")

    st.subheader("Create a Fine-Tuning Job")
    job_file = st.text_input("Enter a file id for job creation")
    model = st.text_input("Enter a model for job creation")
    if st.button("Create Fine-Tuning Job"):
        job = openai.FineTuningJob.create(training_file=job_file, model=model)
        st.write("Job:", job)

    st.subheader("Get Fine-Tuning Job Details")
    job_id = st.text_input("Enter a job ID to retrieve details")
    if st.button("Get Fine-Tuning Job"):
        job = openai.FineTuningJob.retrieve(job_id)
        st.write("Job Retrieved: ", job)

    st.subheader("List Job Events")
    fine_tune_id = st.text_input("Enter a Fine-tuning job ID to list events")
    if st.button("List Events"):
        events = openai.FineTuningJob.list_events(id=fine_tune_id, limit=10)
        for event in events.data:
            st.write("Event:", event)

    st.subheader("Cancel a Fine-Tuning Job")
    cancel_job_id = st.text_input("Enter a job ID to cancel")
    if st.button("Cancel Job"):
        cancelled_job = openai.FineTuningJob.cancel(cancel_job_id)
        st.write("Job Cancelled:", cancelled_job)

    st.subheader("Delete a Fine-Tuned Model")
    model_id = st.text_input("Enter a model ID to delete")
    if st.button("Delete Model"):
        deleted_model = openai.Model.delete(model_id)
        st.write("Model Deleted:", deleted_model)

    # List Fine Tuning Jobs
    st.subheader("List Fine-Tuning Jobs")
    if st.button("List Jobs"):
        jobs = openai.FineTuningJob.list(limit=10)
        for job in jobs.data:
            st.write("Job:", job)


# Display the footer at the bottom of the page
st.markdown(
    """
    <style>
    body {
    font-size: 16px;
    }        
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f6f6f6;
        text-align: center;
        padding: 5px;
        font-size: 20px;
        font-weight: bold;
        border-top: 1px solid #cccccc;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="footer">RUIPING AI - For Internal Evaluation Only</div>
    """,
    unsafe_allow_html=True,
)