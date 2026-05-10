**Due to github Storage limit We are not able to upload .pkl file and Raw dataset also**

#**Cognitive Load Detection from EEG & GSR Signals**
This project is an end-to-end machine learning pipeline designed to classify the cognitive load (task difficulty) experienced by students based on their physiological data, specifically Electroencephalography (EEG) and Galvanic Skin Response (GSR). The analysis uses a rich multimodal dataset to train, evaluate, and compare both classical machine learning and advanced deep learning models.

📋 Table of Contents
Project Objective
Methodology
Project Structure
How to Run
Results & Key Findings

#**🎯 Project Objective**
The primary goal is to build a reliable classifier that can distinguish between three levels of cognitive load (Low, Medium, High) that students experience while solving 3D mental rotation tasks. This is achieved by analyzing synchronized EEG (brainwave) and GSR (skin conductance) signals to identify predictive physiological patterns.

#**🔬 Methodology**
The project follows a structured data science workflow, from raw data processing to model interpretation:
Data Consolidation & Cleaning (00_consolidate_raw_data.ipynb):
Individual raw data files from 38 participants are combined into three master CSV files (EEG.csv, GSR.csv, PSY.csv).
The data is cleaned by handling errors, missing values, and selecting only the most relevant sensor columns for analysis.

#**Preprocessing & Windowing (01_preprocessing.ipynb):**
The cleaned, continuous sensor data is synchronized with task logs (PSY.csv).
The data is segmented into "windows," where each window contains the raw EEG and GSR signals recorded during a single task.

#**Feature Engineering (02_feature_engineering.ipynb):**
Statistical features are extracted from each data window to create a structured dataset. These include mean/variance of EEG frequency bands (Delta, Theta, Alpha, Beta, Gamma), classic cognitive load ratios (e.g., Theta/Alpha), and GSR signal statistics.

#**Baseline Modeling (03_modeling_baseline_classification.ipynb):**
A LightGBM classifier is trained on the engineered features.
Hyperparameter tuning with RandomizedSearchCV is used to find the optimal model configuration and maximize accuracy.

#**Deep Learning (04_modeling_deep_timeseries.ipynb):**
An advanced approach using Transfer Learning is implemented.
The time-series signals are converted into 2D spectrogram images.
A powerful, pre-trained EfficientNet model is fine-tuned on these images to perform classification.

#**Analysis & Inference (05_analysis.ipynb, 06_inference_example.ipynb):**
The performance of the LightGBM and Deep Learning models are compared side-by-side.
The feature importances from the best model are analyzed to understand the key physiological drivers of cognitive load.
An inference script demonstrates how to use the saved model to make predictions on new, hypothetical data.

📂 Project Structure

project/

├── data/

│   ├── raw/

│   │   ├── All_raw_data/

│   │   │   ├── EEG.csv

│   │   │   ├── GSR.csv

│   │   │   └── PSY.csv

│   │   ├── 1_EEG.csv

│   │   ├── 1_GSR.csv

│   │   └── ... (all 38 participant files)

│   └── processed/

│       ├── features_dataset.csv

│       └── task_windows.pkl

├── models/

│   ├── cnn_lstm_model.pt

│   └── lgbm_model.pkl

├── notebooks/

│   ├── 00_consolidate_raw_data.ipynb

│   ├── 01_preprocessing.ipyn

│   ├── 02_feature_engineering.ipynb

│   ├── 03_modeling_baseline_classification.ipynb

│   ├── 04_modeling_deep_timeseries.ipynb

│   ├── 05_analysis.ipynb

│   └── 06_inference_example.ipynb

├── requirements.txt

└── README.md

**🚀 How to Run**

Follow these steps to set up and run the project on your local machine.

Prerequisites:
Python 3.8+

Git
1. Clone the Repository
git clone <your-repository-url>
cd project

2. Create and Activate a Virtual Environment
Create the environment
python -m venv venv
Activate it (Windows)
venv\Scripts\activate
Activate it (macOS/Linux)
source venv/bin/activate

3. Install Dependencies
All required libraries are listed in the requirements.txt file.
pip install -r requirements.txt





