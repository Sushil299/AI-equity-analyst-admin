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

# Function to upload documents
def upload_document(doc_type, uploaded_file):
    if uploaded_file:
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
        data = {
            "company_name": company_name,
            "analysis_quarter": analysis_quarter,
            "document_type": doc_type,
        }
        response = requests.post(f"{BACKEND_URL}/upload/", files=files, data=data)
        return response

# Quarterly Report Upload
st.markdown("#### 🏢 Quarterly Report")
quarterly_file = st.file_uploader("Upload Quarterly Report", type=["pdf"], key="quarterly")

# Earnings Call Transcript Upload
st.markdown("#### 🎙 Earnings Call Transcript")
earning_file = st.file_uploader("Upload Earnings Call Transcript", type=["pdf"], key="earnings")

# Investor Presentation Upload
st.markdown("#### 📊 Investor Presentation")
presentation_file = st.file_uploader("Upload Investor Presentation", type=["pdf"], key="presentation")

# Submit Button
if st.button("Submit"):
    if not company_name or not analysis_quarter:
        st.warning("⚠️ Please enter both Company Name and Analysis Quarter before uploading.")
    else:
        upload_status = []

        # Process each document type individually
        for doc_type, file in [
            ("Quarterly Report", quarterly_file),
            ("Earnings Call Transcript", earning_file),
            ("Investor Presentation", presentation_file)
        ]:
            if file:
                response = upload_document(doc_type, file)
                if response.status_code == 200:
                    upload_status.append(f"{doc_type}: ✅ Uploaded successfully!")
                else:
                    upload_status.append(f"{doc_type}: ❌ Upload failed! ({response.text})")

        if upload_status:
            st.success("\n".join(upload_status))
        else:
            st.warning("⚠️ No files were uploaded. Please select at least one document.")

# Divider
st.markdown("---")