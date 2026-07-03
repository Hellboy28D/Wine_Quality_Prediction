# Wine_Quality_Prediction

🍷 Wine Quality Prediction using Machine Learning

Overview

Wine quality assessment traditionally depends on human experts and sensory evaluation methods. However, machine learning provides an opportunity to predict wine quality efficiently using measurable chemical properties.

This project builds an end-to-end Machine Learning pipeline that predicts wine quality based on various physicochemical characteristics of red wine. The workflow includes data preprocessing, exploratory data analysis, visualization, feature preparation, model training, evaluation, and prediction.

The model is trained using a Random Forest Classifier to identify whether a wine belongs to a good-quality category or not.

⸻

Problem Statement

The quality of wine depends on several measurable factors such as acidity levels, alcohol percentage, sulfur dioxide content, pH level, and more. Understanding the relationship between these attributes can help automate quality prediction.

The objective of this project is to:

* Analyze wine data
* Discover patterns between features
* Build a machine learning model
* Predict wine quality based on input features
* Create a predictive system for real-world use

⸻

Dataset Information

The dataset contains physicochemical measurements of red wine samples.

Input Features

* Fixed Acidity
* Volatile Acidity
* Citric Acid
* Residual Sugar
* Chlorides
* Free Sulfur Dioxide
* Total Sulfur Dioxide
* Density
* pH
* Sulphates
* Alcohol

Target Variable

Quality score of wine

For binary classification:

* Quality ≥ 7 → Good Quality Wine (1)
* Quality < 7 → Bad Quality Wine (0)

⸻

Technologies Used

Programming Language

* Python

Libraries Used

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

Machine Learning Model

* Random Forest Classifier

⸻

Project Workflow

1. Data Collection

The dataset is loaded using Pandas and examined for:

* Shape of dataset
* Missing values
* Feature information
* Statistical summary

⸻

2. Exploratory Data Analysis (EDA)

Data visualization techniques were used to understand relationships and distributions within the dataset.

Visualizations include:

✔ Quality count distribution

✔ Volatile Acidity vs Quality

✔ Citric Acid vs Quality

✔ Correlation Heatmap

These visualizations help identify patterns and feature importance.

⸻

3. Data Preprocessing

Steps performed:

* Handling missing values
* Separating features and labels
* Converting quality values into binary labels

Binary conversion:

if quality >= 7:
    return 1
else:
    return 0

⸻

4. Train-Test Split

Dataset divided into:

* Training Data → 80%
* Testing Data → 20%

Using:

train_test_split()

⸻

5. Model Training

Random Forest Classifier was used for model training.

Why Random Forest?

* Handles non-linear relationships
* Reduces overfitting
* Works well with structured datasets
* Provides strong classification performance

⸻

6. Model Evaluation

Model performance measured using:

* Training Accuracy
* Testing Accuracy

⸻

7. Predictive System

A prediction pipeline was built that accepts new wine chemical measurements and predicts:

🍷 Good Quality Wine

or

🍷 Bad Quality Wine

⸻

Project Structure

Wine_Quality_Prediction/

├── winequality-red.csv

├── src/

│ ├── preprocess.py

│ ├── train.py

│ ├── predict.py

│ └── utils.py

├── README.md

└── .gitignore

⸻

Installation and Setup

Clone repository:

git clone https://github.com/Hellboy28D/Wine_Quality_Prediction.git

Move into project directory:

cd Wine_Quality_Prediction

Create virtual environment:

python3 -m venv venv
source venv/bin/activate

Install required packages:

pip install pandas numpy matplotlib seaborn scikit-learn

Run preprocessing:

python src/preprocess.py

Train model:

python src/train.py

Run prediction:

python src/predict.py

⸻

Future Improvements

🚀 Hyperparameter tuning

🚀 Compare multiple machine learning models

🚀 Feature selection techniques

🚀 Deploy using Flask or Streamlit

🚀 Build an interactive web application

🚀 Containerize using Docker

⸻

Learning Outcomes

Through this project I gained hands-on experience with:

* Data preprocessing
* Exploratory Data Analysis
* Data visualization
* Feature engineering
* Classification algorithms
* Model evaluation
* Building predictive systems

⸻

Author

Divakr Dayas

If you found this project useful, feel free to star the repository and provide feedback.
