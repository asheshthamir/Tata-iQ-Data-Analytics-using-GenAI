# 🚀 Predictive Analytics & Agentic AI Strategy for Credit Risk (Tata iQ Simulation)

### **Project Overview**
This project simulates a real-world engagement with **Geldium**, a financial services client facing rising loan defaults. Acting as a Data Consultant, I conducted an end-to-end analysis—from diagnosing data integrity issues to architecting an autonomous AI-driven collections system.

**Key Achievement:** Discovered a critical **"Credit Score Inversion"** anomaly (high credit score customers defaulting more often), debunking the reliance on traditional metrics and pivoting the strategy towards behavioral indicators like Credit Utilization.

---

### **📂 Project Structure & Deliverables**

#### **Task 1: Exploratory Data Analysis (EDA) & Data Integrity**
* **Objective:** Assess dataset quality for predictive modeling.
* **Method:** Utilized Python & GenAI for automated insight generation.
* **💡 Critical Insight:** Identified that **Credit Utilization (>50%)** is a 3x stronger predictor of default than Credit Score. Discovered that the dataset contained an anomaly where delinquent customers had higher average credit scores (591) than non-delinquents (575).

#### **Task 2: Predictive Modeling Framework**
* **Objective:** Build a model to forecast customer delinquency.
* **Approach:** * Rejected **Logistic Regression** due to the non-linear relationship found in the "Credit Score Inversion."
    * Selected **Random Forest Classifier** to handle data anomalies and maximize **Recall** (catching the most defaulters).
* **Outcome:** A robust model framework focusing on behavioral features (Utilization, DTI) rather than just demographics.

#### **Task 3: Business Strategy & Intervention**
* **Objective:** Translate model insights into actionable business recommendations.
* **Strategy:** Shifted from "Reactive Collections" to "Proactive Nudges."
* **Recommendation:** Launch a **6-week SMS Pilot** targeting customers with >50% utilization spikes, aiming for a **10% reduction** in early-stage delinquency.

#### **Task 4: Autonomous Agentic AI System Design**
* **Objective:** Design a scalable, automated system to execute the strategy.
* **Solution:** Architected an **Agentic AI Framework** that:
    * **Monitors:** Real-time utilization spikes.
    * **Acts:** Autonomously sends personalized "Soft Nudges."
    * **Protects:** Includes "Fairness Guardrails" to prevent bias against low-income segments and ensures regulatory compliance (ECOA/GDPR).

---

### **🛠️ Tools & Technologies Used**
* **Analysis & Modeling:** Python (Pandas, Scikit-learn), GenAI (for code scaffolding).
* **Visualization:** Matplotlib, Seaborn.
* **Strategy & Reporting:** Microsoft PowerPoint, Word.
* **Concepts:** Random Forest, Median Imputation, Agentic AI, Socioeconomic Bias Mitigation.

---

### **📊 The "Credit Score Inversion" Anomaly**
One of the defining moments of this analysis was the discovery that **Credit Score was a misleading metric** for this specific dataset. 

| Customer Segment | Average Credit Score | Default Rate |
| :--- | :--- | :--- |
| **Non-Delinquent** | 575 | Low |
| **Delinquent** | **591** (Higher!) | **High** |

* **Implication:** A standard linear model would have failed. This finding drove the decision to use **Random Forest** (which handles non-linearity) and focus on **Credit Utilization** as the primary risk trigger.

---

### **📜 Certificate**
* **Issued by:** Tata iQ (via Forage)
* **Date:** Jan 2026
* **Focus:** Data Analytics, Predictive Modeling, Business Strategy.

---

### **👤 Author**
**Ashesh Thamir** *IIT Kanpur Graduate | Aspiring Data Analyst* [LinkedIn Profile](Your_LinkedIn_URL_Here)
