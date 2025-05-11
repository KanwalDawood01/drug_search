import streamlit as st
import pandas as pd

st.set_page_config(page_title="Drug Categorizer", layout="wide")

st.title("💊 Drug Categorization App")

# Step 1: Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file with drug names and details", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📋 Preview of Uploaded Data")
    st.dataframe(df.head())

    # Step 2: Validate structure
    if 'DRUG NAME' not in df.columns:
        st.error("CSV must contain a 'DRUG NAME' column.")
    else:
        drug_list = df['DRUG NAME'].dropna().unique().tolist()

        st.subheader("🔍 Drug Categories")
        
        # Category 1: User-selected drugs
        selected_drugs = st.multiselect("Select drugs for Control Sustances:", options=drug_list)

        # Category 2: Remaining drugs
        remaining_drugs = [drug for drug in drug_list if drug not in selected_drugs]

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 📂 Control Substance Drugs")
            for drug in selected_drugs:
                st.write(drug)

        with col2:
            st.markdown("### 📂 Non Control Substance Drugs")
            for drug in remaining_drugs:
                st.write(drug)

        st.subheader("🔎 Search or Click Drug for Details")

        # Combine both lists for search
        search_drug = st.selectbox("Search for a drug name:", drug_list)

        # Filter for exact and similar drug names
        matched_drugs = df[df['DRUG NAME'].str.contains(search_drug, case=False, na=False)]

        st.markdown(f"### 🧾 Details for '{search_drug}' and similar drugs:")
        st.dataframe(matched_drugs.reset_index(drop=True))
