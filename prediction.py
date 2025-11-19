import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# Page Config

st.set_page_config(
    page_title="Multiple Disease Prediction",
    layout="wide",
    page_icon="🧬"
)
# Load Models

kidney_model = pickle.load(open("kidney_disease_prediction.pkl", 'rb'))
liver_model = pickle.load(open("liver_disease_prediction.pkl", 'rb'))
parkinson_model = pickle.load(open("parkinsons_model.pkl", 'rb'))

st.markdown("""
<style>

/* remve top space */
section.main > div {
    padding-top: 0rem !important;
}
.block-container {
    padding-top: 0rem !important;
    margin-top: -2rem !important;
}

/* Remove header space */
header[data-testid="stHeader"] {
    height: 0px !important;
    padding: 0px !important;
    background: none !important;
}

/* Dark theme */
body, .stApp {
    background-color: #0d0d0d;
    color: white;
}

/* Card */
.card {
    background-color: #1a1a1a;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 0px 12px rgba(255,255,255,0.05);
    margin-bottom: 25px;
}

/* Title */
.title {
    text-align: center;
    color: #00e6e6;
    font-size: 32px;
    font-weight: bold;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #cccccc;
    font-size: 18px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)


# SIDEBAR NAVIGATION

with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Home', 'Kidney Disease Prediction', 'Liver Disease Prediction', 'Parkinsons Prediction'],
        icons=['house', 'activity', 'heart', 'person'],
        default_index=0
    )


# HOME PAGE

if selected == 'Home':

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>🧬 Multiple Disease Prediction System</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>A Machine Learning Powered Health Screening Tool</p>", unsafe_allow_html=True)

    st.write("""
    ### Project Overview  
    This system uses machine learning models to predict the likelihood of:  
    - 🩸 **Chronic Kidney Disease (CKD)**  
    - 🍷 **Liver Disease**  
    - 🧠 **Parkinson’s Disease**  

    ### Purpose of the Project  
    Early detection of diseases is crucial.  
    This ML application provides a **fast, easy, and reliable preliminary assessment** based on patient data.

    ### 🛠 Models Used  
    - Kidney Disease → Random Forest  
    - Liver Disease → Logistic Regression or Random Forest  
    - Parkinson’s Disease → SVM / Random Forest  

    Navigate using the sidebar → Select a disease → Enter patient details → Get prediction instantly.
    """)
    st.markdown("</div>", unsafe_allow_html=True)


# KIDNEY DISEASE PREDICTION

if selected == 'Kidney Disease Prediction':

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>🩸 Kidney Disease Prediction</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    kidney_features_names = [
        "Age","BP","SG","AL","SU","RBC","PC","PCC","BA","BGR",
        "BU","SC","POT","WC","RC","HTN","DM","CAD","Appetite","PE","ANE"
    ]

    kidney_features = []
    for name in kidney_features_names:
        kidney_features.append(st.number_input(name))

    input_data = np.array([kidney_features])

    if st.button("🔍 Predict Kidney", use_container_width=True):
        prediction = kidney_model.predict(input_data)
        if prediction[0] == 1:
            st.error("⚠ The model predicts that the patient HAS Kidney Disease.")
        else:
            st.success("The model predicts that the patient does NOT have Kidney Disease.")


# LIVER DISEASE PREDICTION
if selected == 'Liver Disease Prediction':

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>🍷 Liver Disease Prediction</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    liver_features_names = [
        "Age","Gender","Total_Bilirubin","Direct_Bilirubin","Alkaline_Phosphotase",
        "Alamine_Aminotransferase","Aspartate_Aminotransferase",
        "Total_Protiens","Albumin","Albumin_and_Globulin_Ratio"
    ]

    liver_features = []
    for name in liver_features_names:
        liver_features.append(st.number_input(name))

    input_data = np.array([liver_features])

    if st.button("🔍 Predict Liver", use_container_width=True):
        prediction = liver_model.predict(input_data)
        if prediction[0] == 1:
            st.error("⚠ The model predicts that the patient HAS Liver Disease.")
        else:
            st.success("The model predicts that the patient does NOT have Liver Disease.")

# -----------------------------
# PARKINSON'S DISEASE PREDICTION
# -----------------------------
if selected == 'Parkinsons Prediction':

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>🧠 Parkinson's Disease Prediction</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    parkinson_features_names = [
        "MDVP:Fo(Hz)","MDVP:Fhi(Hz)","MDVP:Flo(Hz)","MDVP:Jitter(%)",
        "MDVP:Jitter(Abs)","MDVP:RAP","MDVP:PPQ","Jitter:DDP",
        "MDVP:Shimmer","MDVP:Shimmer(dB)","Shimmer:APQ3","Shimmer:APQ5",
        "MDVP:APQ","Shimmer:DDA","NHR","HNR","RPDE","DFA","spread1",
        "spread2","D2","PPE"
    ]

    parkinson_features = []
    for name in parkinson_features_names:
        parkinson_features.append(st.number_input(name))

    input_data = np.array([parkinson_features])

    if st.button("🔍 Predict Parkinson", use_container_width=True):
        prediction = parkinson_model.predict(input_data)
        if prediction[0] == 1:
            st.error("⚠ The model predicts that the patient HAS Parkinson's Disease.")
        else:
            st.success("The model predicts that the patient does NOT have Parkinson's Disease.")

# FOOTER
st.markdown("""
<hr>
<p style='text-align: center; color: gray; font-size: 14px;'>
    Developed by <b>Thariga Charles</b> | © 2025
</p>
""", unsafe_allow_html=True)
