# TD Bank Loan Prediction Project

This project predicts loan approval outcomes for TD Bank customers using machine learning.
It includes data preprocessing, model training, and a web application for making real-time predictions.

---

## Features

* Data cleaning and encoding (see `TD.ipynb`)
* Machine Learning model (stored in `td_loan_model.pkl`)
* Interactive web app built with Flask (`app.py`)
* Cleaned dataset included (`td_loan_data_encoded_clean.xltx`)

---

## Model Overview

The model analyzes customer financial and demographic features to predict whether a loan should be approved or denied.
It is trained using scikit-learn algorithms on encoded and scaled features from the prepared dataset.

---

## How to Run the App

1. Install dependencies:

   ```bash
   pip install flask pandas scikit-learn
   ```
2. Run the web app:

   ```bash
   python app.py
   ```
3. Open your browser at:

   ```
   http://127.0.0.1:5000
   ```

---

## Files Included

| File                            | Description                                           |
| ------------------------------- | ----------------------------------------------------- |
| TD.ipynb                        | Jupyter Notebook for data analysis and model training |
| app.py                          | Flask web application for model deployment            |
| td_loan_data_encoded_clean.xltx | Cleaned dataset used for training                     |
| td_loan_model.pkl               | Serialized trained ML model                           |
| .ipynb_checkpoints/             | Auto-generated Jupyter backup folder                  |

---

## Future Improvements

* Add Streamlit UI for easier access
* Include model accuracy visualization
* Integrate with cloud database (e.g., AWS RDS)

---


