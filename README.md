🧬 Multiple Disease Prediction System

A Machine Learning-powered web application built using Streamlit that predicts the likelihood of multiple diseases — Kidney Disease, Liver Disease, and Parkinson’s Disease — based on user input.

This project integrates trained ML models, a clean UI, and real-time inference to help users understand potential risks and take timely action.

🚀 Features

✔️ Predict Kidney Disease
✔️ Predict Liver Disease
✔️ Predict Parkinson’s Disease
✔️ Clean Streamlit UI with sidebar navigation
✔️ Fast and accurate predictions using trained machine learning models
✔️ Fully containerizable and deployable on platforms like Streamlit Cloud

🖼️ Tech Stack

Frontend / UI: Streamlit
Backend: Python
Models: Pickle (.pkl files)
Libraries:

NumPy

Pandas

Scikit-learn

Streamlit

streamlit-option-menu


⚙️ How It Works

User selects a disease from the sidebar.

Inputs medical measurements.

The trained model processes the input.

Streamlit displays prediction:

>“Positive – Disease Detected”

>“Negative – No Disease Detected”
How to Run the Project:
1. Clone the repository
git clone https://github.com/Thariga-yuvi/DS_Multiple-Disease-prediction.git
cd multiple-disease-prediction
2. Install the dependencies
 pip install -r requirements.txt
3. Run the Streamlit app
   streamlit run prediction.py

<img width="1557" height="798" alt="image" src="https://github.com/user-attachments/assets/ed52f3ec-c6c8-4243-825f-3d4ab0903716" />
<img width="1457" height="673" alt="image" src="https://github.com/user-attachments/assets/f455d575-7c90-4111-b5f6-68590e8046cb" />
<img width="1807" height="760" alt="image" src="https://github.com/user-attachments/assets/e5c8aec1-d788-449a-985d-295a79c27e08" />
<img width="1818" height="672" alt="image" src="https://github.com/user-attachments/assets/5880e963-adeb-4386-8417-f606ea1e14a8" />

📊 Models Used
Kidney Disease Model

Algorithm: Random Forest/ KNN/Logistic Regression/DecisionTree

Metrics: High accuracy with balanced feature distribution

Liver Disease Model

Algorithm: Random Forest

Handles missing values and imbalance

Parkinson’s Disease Model

Algorithm: GradientBoosting, SVM

🤝 Contribution

Pull requests are welcome!
If you'd like to contribute, feel free to fork the repo and submit PRs.

📜 License

This project is licensed under the MIT License.

📧 Contact

Developer: Thariga Charles
📩 Email: tharigayuvaraj@gmail.com
🌍 Location: Chennai, India




