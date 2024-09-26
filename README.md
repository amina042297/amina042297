<h1 align="center">Amina Bauyrzhan - Data Analyst Portfolio</h1>

## About

Hi, I'm Amina! With an analytical background in Economics and a recent graduate of Boston University's Applied Data Analytics Program, I have developed a robust foundation in data science and advanced analytical techniques.

I’m passionate about exploring innovative tools and methodologies in data analysis, continuously seeking opportunities to enhance my skills. Whether collaborating with a team or working independently, I thrive on uncovering meaningful insights and applying data-driven solutions to tackle complex problems.

This repository is a space where I showcase my skills, share projects, and document my journey in the fields of Data Analytics and Data Science.

Portfolio projects
  #### Python
  - [Dota 2 Winner Prediction (Binary Classification Problem)](https://github.com/amina042297/amina042297/blob/main/Dota_2_Binary_Classification_Kaggle.ipynb)
  - [AI Statement Correctness Checker app with NLP and GPT](https://github.com/amina042297/AI-Statement-correctness-checker/blob/main/README.md)
  - [Classification models to differentiate between two rice varieties, Cammeo and Osmancik](https://github.com/amina042297/Cammeo-and-Osmancik-Varieties/tree/main)
  #### R
  - [Billionaires Statistics Dataset Analysis](https://github.com/amina042297/Billionaires-Statistics-Dataset-Analysis)
  - [Analysis of Direct Marketing Campaign Effectiveness](https://github.com/amina042297/Analysis-of-Direct-Marketing-Campaign-Effectiveness/blob/main/README.md)
## Portfolio Projects
In this section I will list data analytics projects briefly describing the technology stack used to solve cases.

### Predicting Dota 2 Match Outcomes: A Machine Learning Approach
**Code:** [Dota 2 Winner Prediction (Binary Classification Problem)](https://github.com/amina042297/amina042297/blob/main/Dota_2_Binary_Classification_Kaggle.ipynb) 

**Goal:**
To predict the winner (Radiant or Dire) in a Dota 2 game based on in-game statistics from the first few minutes of gameplay using machine learning models.

**Description:**
This project is based on the Dota 2 Kaggle competition, which involves binary classification to predict the winner of a game using structured data. The dataset contains numerous game features such as player stats, hero selections, and game events. Key steps include data preprocessing (feature engineering and encoding), applying logistic regression and XGBoost models, and evaluating their performance using ROC AUC metrics. Additionally, an ensemble model using both Logistic Regression and XGBoost was implemented to further improve prediction accuracy.

**Skills:** 

- Data Engineering: Creating new features (gold difference, XP difference, etc.) from raw game data.
- Machine Learning: Implementing logistic regression with cross-validation, XGBoost, Ensemble modeling (VotingClassifier)
- Model Evaluation: Using performance metrics such as ROC AUC to assess model accuracy.
- Python Programming: Using libraries like pandas for data manipulation and scikit-learn for machine learning and model evaluation.
- Feature Scaling: Applying standardization techniques for preparing data for model training.

**Technology:** 

- pandas for data manipulation
- scikit-learn for machine learning models, scaling, and evaluation (LogisticRegressionCV, StratifiedKFold, StandardScaler)
- XGBoost
- Matplotlib (for ROC curve visualization)

**Results:**

- The best model achieved a ROC AUC score of 0.8327 using XGBoost.
- The ensemble model (Voting Classifier) achieved a ROC AUC score of 0.8262.
- Submission results were prepared for the Kaggle competition, predicting the probability of the Radiant team winning.
- I was 2nd in this [competition.](https://www.kaggle.com/competitions/dota-2-simplified/overview)


### AI Statement Correctness Checker [App.](https://ai-statement-correctness-checker-jxy5j4ehhghdxaxrvwbafb.streamlit.app/)

**Code:** [AI Statement Correctness Checker app with NLP and GPT](https://github.com/amina042297/AI-Statement-correctness-checker/blob/main/README.md)

**Goal:**
To automate the process of identifying and validating correct statements from lecture materials (PDF/PPT) using advanced Natural Language Processing (NLP) techniques, such as MPNet (from the BERT family) and GPT models.

**Description:**
This project addresses the challenge faced by students in the CS688 course of quickly and accurately identifying correct statements during tests based on extensive lecture materials. The solution extracts text from PDFs and PPTs, preprocesses it, and applies semantic analysis using the MPNet model to check the correctness of user-inputted statements. In cases where the semantic similarity is ambiguous, GPT is used to refine the classification. The application provides a user-friendly Streamlit interface for uploading documents, inputting statements, setting thresholds, and visualizing results.

**Skills:** 

- Natural Language Processing (NLP)
- Text extraction and preprocessing
- Semantic analysis using sentence embeddings
- GPT integration for advanced contextual analysis
- Streamlit app development
- Python programming

**Technology:** 

- MPNet (paraphrase-mpnet-base-v2): For semantic similarity and sentence embedding generation.
- GPT-4: Used for deeper context analysis when MPNet results are ambiguous.
- Python libraries: pdfminer (for PDF extraction), python-pptx (for PPT extraction), sentence-transformers, Streamlit.
- Streamlit: Provides the user interface for file uploads, analysis, and results display.

**Results:**

- The application successfully automates the identification of correct statements from lecture materials, offering a streamlined process to help students perform better in tests. It allows users to upload lecture slides, input statements, and receive a True/False classification based on predefined similarity thresholds, with color-coded feedback and detailed explanations (e.g., similarity scores, relevant slide/page references).
- Here is the [app.](https://ai-statement-correctness-checker-jxy5j4ehhghdxaxrvwbafb.streamlit.app/)

### Rice Varieties Classification: Cammeo and Osmancik

**Code:** [Classification models to differentiate between two rice varieties, Cammeo and Osmancik](https://github.com/amina042297/Cammeo-and-Osmancik-Varieties/tree/main)

**Goal:**
To classify two rice varieties—Cammeo and Osmancik—using machine learning models based on their morphological features.

**Description:**
This project uses a dataset of 3,810 rice grain images to classify the rice varieties grown in Turkey (Osmancik and Cammeo). The dataset contains seven key morphological features for each rice grain, such as Area, Perimeter, Major Axis Length, Minor Axis Length, Eccentricity, Convex Area, and Extent. These features were analyzed using exploratory data analysis and machine learning models to differentiate between the two rice varieties. The dataset was split into training and testing sets to evaluate the performance of various models.

**Skills:** 

- Exploratory Data Analysis (EDA)
- Feature engineering and selection
- Supervised machine learning classification
- Model evaluation and tuning
- Feature scaling and model interpretation

**Technology:** 

- **Machine Learning Models**:
  - K-Nearest Neighbors (KNN)
  - Logistic Regression
  - Support Vector Machine (SVM)
  - Gaussian Naive Bayes
  - Decision Tree
  - Random Forest
- **Python Libraries**:
  - Pandas
  - Scikit-learn
  - Matplotlib
  - Seaborn
- **StandardScaler**: For standardizing features 

**Results:**

- **Random Forest** achieved the highest accuracy of **93%**, with excellent performance in classifying both rice varieties.
- **Linear SVM** showed a slightly lower accuracy of **92.9%**, with the best ability to distinguish non-Cammeo varieties.
- **Logistic Regression** also performed well, achieving an accuracy of **92.7%**.
- **KNN** and **Naive Bayes** models performed similarly, with accuracies slightly above **91%**.
- **Decision Tree** had the lowest accuracy of **89.5%**.

The **Random Forest** and **Linear SVM** models were the top performers, indicating that more sophisticated models are better suited for this classification task.



 
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
