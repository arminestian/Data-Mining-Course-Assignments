```markdown
# Data Mining Course Assignments 

Welcome to my Data Mining course assignments repository. This repository contains the practical tasks and projects assigned during the course, focusing on key data mining concepts, algorithms, and real-world data analysis.

## 📁 Repository Structure

```
├── Assignment1/          # Shopping Basket Problem
├── Assignment2/          # Abalone Age Prediction (KNN)
├── data/                 # Dataset files (if applicable)
├── reports/              # Generated reports and outputs
└── README.md
```

## 📝 Assignments Overview

### Assignment 1: Shopping Basket Problem
- **Goal:** Analyze customer purchasing patterns using association rule mining.
- **Tasks:**
  - Identify frequently bought together product pairs.
  - Identify frequently bought together department pairs.
  - Generate per-department product association rules.
- **Metrics:** Support (`min_support = 0.003`), Confidence (`min_confidence = 0.25`)
- **Output:** Product pairs and department pairs with support/confidence values, including product names.

### Assignment 2: Abalone Age Prediction (KNN)
- **Goal:** Predict abalone age using the K-Nearest Neighbors algorithm.
- **Dataset:** [Abalone Dataset (UCI)](https://archive.ics.uci.edu/dataset/1/abalone)
- **Features:** Length, diameter, height, weight measurements (gender ignored).
- **Target:** Rings (age indicator)
- **Approach:**
  - Train-test split: 70% training, 30% testing
  - Evaluate KNN for `k = 1` to `10`
  - Performance metric: RMSE (Root Mean Squared Error)
- **Output:** RMSE vs. k plot + analysis of model performance.

## 🛠️ Tools & Technologies

- Python (pandas, numpy, scikit-learn, matplotlib, seaborn)
- Git & GitHub
   ```
## 👤 Author

Armin Servati – Data Mining Course Student  
Course Instructor: Prof. Alireza Sokhandan 
University: University of Tabriz

## 📄 License

This repository is for educational purposes only.
```
