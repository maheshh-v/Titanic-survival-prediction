#  Titanic Survival Prediction — End-to-End ML Project with Flask API

Hello! I'm **Mahesh**, a B.Tech Computer Science (AI) student.  
This project is part of my **internship and job readiness portfolio**, built to demonstrate my understanding of machine learning, data processing, model evaluation, and deployment.

---

##  Project Overview

This project predicts whether a passenger survived the Titanic disaster using a machine learning classification model.  
It includes everything from **EDA, feature engineering, model training**, and **API deployment** using **Flask** — all built from scratch.

> ✅ Goal: Show full ML lifecycle from raw CSV to deployed API  
> ✅ Dataset: [Kaggle Titanic Dataset](https://www.kaggle.com/competitions/titanic)

---

##  Skills Demonstrated

- Real-world data preprocessing (nulls, encoding, new features)
- Model building with **Scikit-learn** (Pipeline + Random Forest)
- **Saving & Loading models** using `joblib`
- Creating a **Flask API** for model inference
- **Postman testing** for JSON-based predictions
- Project structure and best practices for real-world code

---

## 📁 Project Structure
titanic\_ml\_project/  
│  
├── data/  
│ └── raw/ <- Original dataset (train.csv, test.csv)  
│  
├── models/  
│ └── titanic\_rf\_model.pkl <- Trained & saved model  
│  
├── notebooks/  
│ └── titanic\_model.ipynb <- Full EDA, modeling & final pipeline  
│  
├── src/  
│ └── app.py <- Flask API code  
│  
├── requirements.txt <- All required packages  
└── README.md <- This file



---

## 📊 Features Used in Model

- `Pclass` – Ticket class
- `Sex` – 0 (male), 1 (female)
- `Age`
- `SibSp` – Siblings/spouses aboard
- `Parch` – Parents/children aboard
- `Fare`
- `Embarked` – Encoded (0, 1, 2)
- `Title` – Extracted from Name
- `FamilySize` – SibSp + Parch + 1
- `isAlone` – Binary: 1 if no family, else 0

These were selected after EDA and feature engineering to improve model accuracy.

---

## 🔧 ML Pipeline & Model

```python
Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier())
])
```
*   Built using `Pipeline()` to combine preprocessing and training
    
*   Tuned with basic hyperparameters
    
*   Trained on cleaned dataset
    
*   Saved using `joblib`
    

* * *

## 🌐 API Deployment Using Flask

✔️ Flask Endpoints:

*   `/` → Health check (GET)
    
*   `/predict` → Predict survival using POST JSON input
    

### 🔁 Sample Input (JSON)


{
  "Pclass": 3,
  "Sex": 0,
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked": 0,
  "Title": 1,
  "FamilySize": 2,
  "isAlone": 0
}

### ✅ Sample Output

json


{
  "Survived": 0,
  "Survival Probability": 0.2676
}

Tested using Postman with proper headers (`Content-Type: application/json`)

* * *

## 🧪 Tools & Libraries Used

| Tool | Purpose |
| --- | --- |
| Python | Core programming language |
| Pandas, NumPy | Data manipulation |
| Scikit-learn | Model training, pipelines, metrics |
| Flask | API deployment |
| Joblib | Model saving/loading |
| Postman | API testing |

* * *

## 📸 Screenshots (Optional but Recommended)

*   Screenshot of Jupyter notebook model output
    
*   Screenshot of Postman response from `/predict`
    

* * *

## 📘 What I Learned

*   How to handle real-world messy data
    
*   Building Scikit-learn Pipelines
    
*   Saving & loading models using joblib
    
*   Building and testing Flask APIs
    
*   Structuring an ML project for clarity and reusability
    

* * *

## 🚀 Future Improvements

*   Add a simple web interface (Streamlit or HTML form)
    
*   Use Docker for containerized deployment
    
*   Add logging and exception handling to Flask API
    
*   Implement CI/CD for better development flow
    

* * *

## 🙏 Acknowledgements

*   Inspired by Kaggle Titanic Competition
    
*   Mentorship from AI tools and self-research
    
*   Project completed as part of my Internship Preparation Plan
    

* * *

## 💼 Connect with Me

If you're a recruiter or mentor looking for someone passionate, consistent, and self-driven in ML, feel free to connect:

📧 Email: \[[maheshvya.724@gmail.com](https://mailto:YourEmail@example.com/)\]  
🔗 LinkedIn: \[\]
