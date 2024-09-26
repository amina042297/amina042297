<h1 align="center">Amina Bauyrzhan - Data Analyst Portfolio</h1>

## About

Hi, I'm Amina! With an analytical background in Economics and a recent graduate of Boston University's Applied Data Analytics Program, I have developed a robust foundation in data science and advanced analytical techniques.

I’m passionate about exploring innovative tools and methodologies in data analysis, continuously seeking opportunities to enhance my skills. Whether collaborating with a team or working independently, I thrive on uncovering meaningful insights and applying data-driven solutions to tackle complex problems.

This repository is a space where I showcase my skills, share projects, and document my journey in the fields of Data Analytics and Data Science.

## Table of Contents
- [About](#about)
- [Portfolio Projects](#portfolio-projects)
  #### Python
  - [Predicting Dota 2 Match Outcomes: A Machine Learning Approach](https://github.com/amina042297/amina042297/blob/main/README.md#predicting-dota-2-match-outcomes)
  - [AI Statement Correctness Checker app with NLP and GPT](https://github.com/amina042297/amina042297/blob/main/README.md#ai-statement-correctness-checker)
  - [Classification models to differentiate between two rice varieties, Cammeo and Osmancik](#classification-models-to-differentiate-between-two-rice-varieties-cammeo-and-osmancik)
  #### R
  - [Billionaires Statistics Dataset Analysis](#billionaires-statistics-dataset-analysis)
  - [Analysis of Direct Marketing Campaign Effectiveness](#analysis-of-direct-marketing-campaign-effectiveness)


# Portfolio Projects
In this section, I list my data analytics projects, briefly describing the technology stack used to solve each case.

---

### Predicting Dota 2 Match Outcomes
**Code:** [Dota 2 Winner Prediction (Binary Classification Problem)](https://github.com/amina042297/amina042297/blob/main/Dota_2_Binary_Classification_Kaggle.ipynb)

**Goal:**
To predict the winner (Radiant or Dire) in a Dota 2 game based on in-game statistics from the first few minutes of gameplay using machine learning models.

**Description:**
This project is based on the Dota 2 Kaggle competition, involving binary classification to predict the winner using structured data. It includes key steps like data preprocessing, feature engineering, applying logistic regression and XGBoost models, and evaluating performance with ROC AUC metrics. An ensemble model using Logistic Regression and XGBoost was implemented to further improve prediction accuracy.

**Skills:** 
- Data Engineering: Feature creation (gold difference, XP difference).
- Machine Learning: Logistic regression, XGBoost, Ensemble modeling.
- Model Evaluation: ROC AUC metric assessment.
- Python Programming: pandas, scikit-learn for data manipulation and modeling.
- Feature Scaling: Standardization for model training.

**Technology:**
- pandas, scikit-learn (LogisticRegressionCV, StratifiedKFold, StandardScaler), XGBoost, Matplotlib.

**Results:**
- Best ROC AUC score of **0.8327** using XGBoost.
- Ensemble model achieved ROC AUC score of **0.8262**.
- 2nd place in the [competition](https://www.kaggle.com/competitions/dota-2-simplified/overview).

---

### AI Statement Correctness Checker
**App:** [Streamlit App](https://ai-statement-correctness-checker-jxy5j4ehhghdxaxrvwbafb.streamlit.app/)

**Code:** [AI Statement Correctness Checker app with NLP and GPT](https://github.com/amina042297/AI-Statement-correctness-checker/blob/main/README.md)

**Goal:**
To automate the process of identifying and validating correct statements from lecture materials (PDF/PPT) using advanced NLP techniques, including MPNet and GPT models.

**Description:**
The project helps students quickly identify correct statements in tests based on lecture materials. The solution extracts text from PDFs/PPTs, preprocesses it, and applies MPNet for semantic analysis. GPT is used to refine ambiguous cases. The Streamlit app provides a user interface for uploading documents, inputting statements, and displaying results.

**Skills:** 
- Natural Language Processing (NLP), GPT integration.
- Streamlit app development.
- Python programming.

**Technology:** 
- MPNet (paraphrase-mpnet-base-v2), GPT-4, pdfminer, python-pptx, Streamlit.

**Results:**
- Successfully automated the identification of correct statements with color-coded feedback and detailed explanations.
- [App](https://ai-statement-correctness-checker-jxy5j4ehhghdxaxrvwbafb.streamlit.app/) deployed.

---

### Rice Varieties Classification: Cammeo and Osmancik
**Code:** [Classification models for Cammeo and Osmancik](https://github.com/amina042297/Cammeo-and-Osmancik-Varieties/tree/main)

**Goal:**
To classify two rice varieties—Cammeo and Osmancik—using machine learning models based on their morphological features.

**Description:**
The project uses a dataset of 3,810 rice grain images to classify two rice varieties. The dataset includes features such as Area, Perimeter, Major Axis Length, Minor Axis Length, Eccentricity, Convex Area, and Extent. The performance of several machine learning models was evaluated, and the dataset was split into training and testing sets.

**Skills:** 
- Exploratory Data Analysis (EDA), Feature Engineering.
- Supervised machine learning.
- Model evaluation and tuning.

**Technology:** 
- KNN, Logistic Regression, SVM, Naive Bayes, Decision Tree, Random Forest.
- Python: pandas, scikit-learn, Matplotlib, Seaborn.

**Results:**
- **Random Forest** achieved the highest accuracy of **93%**.
- **SVM** performed slightly lower with **92.9%** accuracy.
- **Logistic Regression** achieved **92.7%** accuracy.

---

### Billionaires Statistics Dataset Analysis
**Summary:** [Published in RPubs](https://rpubs.com/amina0422/1223987)


**Code:** [Billionaires Statistics Dataset Analysis](https://github.com/amina042297/Billionaires-Statistics-Dataset-Analysis)
  
**Goal:**
Analyze the wealth distribution, business sectors, and demographics of the world's billionaires based on a dataset from Kaggle.

**Description:**
This project provides insights into income sources, self-made versus inherited wealth, age demographics, and wealth distribution of billionaires. Additionally, various sampling methods were applied to further explore the dataset, with visualizations summarizing the data.

**Skills:**
- Data wrangling, visualization, EDA.
- Statistical analysis, sampling techniques.

**Technology:**
- R: `plotly`, `ggplot2`, `tm`, `wordcloud`.
- Sampling Methods: Simple Random Sampling, Systematic Sampling, Stratified Sampling.

**Results:**
- **Wealth Distribution**: Most billionaires are from Finance, Technology, and Manufacturing.
- **Self-made Billionaires**: 68% self-made, prevalent in Sports and Energy sectors.

---

### Analysis of Direct Marketing Campaign Effectiveness for Term Deposit Subscriptions

**Code:** [Analysis of Direct Marketing Campaign Effectiveness](https://github.com/amina042297/Analysis-of-Direct-Marketing-Campaign-Effectiveness/blob/main/README.md)
**Goal:**
Identify key predictors of client subscription to term deposits based on a direct marketing campaign dataset and assess the effectiveness of logistic regression with ridge regularization.

**Description:**
This project analyzes the direct marketing campaigns of a Portuguese bank to promote term deposit subscriptions. The dataset consists of 45,211 observations with 17 variables. Logistic regression with ridge regularization was applied to manage multicollinearity, and the dataset was preprocessed through outlier removal and downsampling.

**Skills:**
- Data Preprocessing, EDA, Logistic Regression with Ridge Regularization.
- Model Performance Evaluation (AUC, Accuracy, Sensitivity).

**Technology:**
- R Libraries: `dplyr`, `psych`, `ggplot2`, `tidyr`, `caret`, `glmnet`, `pROC`.

**Results:**
- **AUC** of **0.913** with high sensitivity and specificity.
- Key predictors: being a student, single marital status, previous campaign outcome.

📫 Email: **amina.bauyrzhan@gmail.com**

📋 [CV](https://github.com/amina042297/amina042297/blob/main/CV_Amina.pdf)

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/www.linkedin.com/in/amina-bauyrzhan" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="www.linkedin.com/in/amina-bauyrzhan" height="30" width="40" /></a>
<a href="https://kaggle.com/https://www.kaggle.com/aminabauyrzhan" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="https://www.kaggle.com/aminabauyrzhan" height="30" width="40" /></a>
<a href="https://www.leetcode.com/https://leetcode.com/u/amina0422/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/leet-code.svg" alt="https://leetcode.com/u/amina0422/" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://aws.amazon.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="40" height="40"/> </a> <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a> <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="40" height="40"/> </a> </p>
