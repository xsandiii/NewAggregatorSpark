# NewAggregatorSpark

## Project Overview
This project focuses on building a machine learning model to classify news headlines into four categories:

b - Business
t - Science & Technology
e - Entertainment
m - Health
The dataset used is from the UCI Machine Learning Repository:
News Aggregator Dataset

The goal is to automate the classification of news headlines to streamline document distribution in a business setting.

## Approach
### 1. Data Preprocessing
Loaded the dataset using Apache Spark for efficient large-scale processing.
Removed null values (only 9 instances in the category column).
Handled imbalanced data, where Entertainment had the highest number of samples, and Health the least.
Identified 778 rows with multiple category labels but treated it as a multiclass classification problem.
### 2. Model Selection
Follow models were tested:

* Naïve Bayes (Baseline Model)
* Random Forest (For better interpretability)
* should be tested XGBoost (More powerful but challenging to implement in Spark ML)
### 3. Evaluation Metrics
Due to class imbalance, traditional accuracy wasn't enough. Instead, we used:

* Precision
* Recall
* F1 Score
### Implementation Details
* Framework: Apache Spark (PySpark ML)
* Libraries Used:
  * pyspark.ml for model training
  * pandas for exploratory analysis
  * scikit-learn for additional metrics evaluation
* Training & Testing:
  * Data split into 80% training, 20% testing
