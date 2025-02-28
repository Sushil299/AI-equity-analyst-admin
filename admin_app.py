# -*- coding: utf-8 -*-
"""admin_app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-kL48zJMZD2sqabS-FeKumgjGmbYXeYY
"""

import streamlit as st
import requests
import pandas as pd

# Backend URL
BACKEND_URL = "https://ai-equity-analyst.onrender.com"

st.title("📤 Admin Panel - Upload Documents")
st.markdown("### Enter Company Name and Analysis Quarter")

# Company Info
company_name = st.text_input("Company Name")
analysis_quarter = st.selectbox("Analysis Quarter", ["Q1FY25", "Q2FY25", "Q3FY25", "Q4FY25"])

# Quarterly Report Upload
st.markdown("#### 🏢 Quarterly Report")
quarterly_file = st.file_uploader("Upload Quarterly Report", type=["pdf"], key="quarterly")

# Earnings Call Transcript Upload
st.markdown("#### 🎙 Earnings Call Transcript")
earning_file = st.file_uploader("Upload Earnings Call Transcript", type=["pdf"], key="earnings")

# Investor Presentation Upload
st.markdown("#### 📊 Investor Presentation")
presentation_file = st.file_uploader("Upload Investor Presentation", type=["pdf"], key="presentation")

# Function to upload all documents in a single request
def upload_documents():
    files = {}

    if quarterly_file:
        files["quarterly_report"] = (quarterly_file.name, quarterly_file.getvalue(), "application/pdf")
    else:
        files["quarterly_report"] = ('', b'')

    if earning_file:
        files["earnings_call_transcript"] = (earning_file.name, earning_file.getvalue(), "application/pdf")
    else:
        files["earnings_call_transcript"] = ('', b'')

    if presentation_file:
        files["investor_presentation"] = (presentation_file.name, presentation_file.getvalue(), "application/pdf")
    else:
        files["investor_presentation"] = ('', b'')

    data = {
        "company_name": company_name,
        "analysis_quarter": analysis_quarter
    }

    response = requests.post(f"{BACKEND_URL}/upload/", files=files, data=data)
    return response

# Submit Button
if st.button("Submit"):
    if not company_name or not analysis_quarter:
        st.warning("⚠️ Please enter both Company Name and Analysis Quarter before uploading.")
    else:
        response = upload_documents()
        if response.status_code == 200:
            st.success("✅ Files uploaded & AI analysis updated successfully!")
        else:
            st.error(f"❌ Upload failed! ({response.text})")