```markdown
# Data Mining Course Assignments

Welcome to my repository for **Data Mining course assignments**.  
This repository includes practical tasks and projects completed during the course, covering fundamental data mining concepts, algorithms, and real-world data analysis.

---

## 📚 Contents

- [Repository Structure](#-repository-structure)
- [Assignments Overview](#-assignments-overview)
  - [Assignment 1: Shopping Basket Analysis](#assignment-1-shopping-basket-analysis)
  - [Assignment 2: Abalone Age Prediction (KNN)](#assignment-2-abalone-age-prediction-knn)
- [Tools and Technologies](#️-tools-and-technologies)
- [Author](#-author)
- [License](#-license)

---

## 📁 Repository Structure

```text
├── Assignment1/          # Shopping Basket Analysis (Association Rules)
├── Assignment2/          # Abalone Age Prediction (KNN)
├── data/                 # Dataset files (if applicable)
├── reports/              # Generated reports, notebooks, and outputs
└── README.md
```

---

## 📝 Assignments Overview

### Assignment 1: Shopping Basket Analysis

**Goal:**  
Analyze customer purchasing behavior using association rule mining.

**Tasks:**
- Find frequently co-purchased product pairs
- Find frequently co-purchased department pairs
- Generate per-department product association rules

**Metrics:**
- **Support:** `min_support = 0.003`
- **Confidence:** `min_confidence = 0.25`

**Output:**  
Lists of product pairs and department pairs with support/confidence values, including descriptive product names.

---

### Assignment 2: Abalone Age Prediction (KNN)

**Goal:**  
Predict abalone age using the **K-Nearest Neighbors (KNN)** algorithm.

**Dataset:**  
[Abalone Dataset (UCI Machine Learning Repository)](https://archive.ics.uci.edu/dataset/1/abalone)

**Features Used:**
- Length
- Diameter
- Height
- Whole weight
- Shucked weight
- Viscera weight
- Shell weight

> **Note:** The sex/gender feature is excluded from the model.

**Target:**  
Number of rings (used as an indicator of age)

**Approach:**
- Split the dataset into **70% training** and **30% testing**
- Evaluate KNN for values of `k` from `1` to `10`
- Use **RMSE (Root Mean Squared Error)** as the evaluation metric

**Output:**
- RMSE vs. k plot
- Performance analysis and discussion

---

## 🛠️ Tools and Technologies

- **Python**
  - pandas
  - numpy
  - scikit-learn
  - matplotlib
  - seaborn
- **Git**
- **GitHub**

---

## 👤 Author

**Armin Servati**  
Data Mining Course Student  
**Instructor:** Prof. Alireza Sokhandan  
**University:** University of Tabriz

---

## 📄 License

This repository is intended for **educational purposes only**.
```
