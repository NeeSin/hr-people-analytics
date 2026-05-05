# ============================================
# HR People Analytics: Python Analysis
# Dataset: IBM HR Attrition
# Author: Your Name
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load Data ---
df = pd.read_csv('../data/hr_data.csv')

print("Dataset shape:", df.shape)
print("\nColumn names:\n", df.columns.tolist())
print("\nMissing values:\n", df.isnull().sum())

# --- 1. Attrition Rate Overview ---
attrition_counts = df['Attrition'].value_counts()
plt.figure(figsize=(6, 4))
attrition_counts.plot(kind='bar', color=['steelblue', 'salmon'])
plt.title('Overall Attrition: Yes vs No')
plt.xlabel('Attrition')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('../visuals/attrition_overview.png')
plt.show()

# --- 2. Attrition by Department ---
dept_attrition = df.groupby(['Department', 'Attrition']).size().unstack()
dept_attrition.plot(kind='bar', figsize=(8, 5), color=['steelblue', 'salmon'])
plt.title('Attrition by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('../visuals/attrition_by_department.png')
plt.show()

# --- 3. Monthly Income Distribution by Job Role ---
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='JobRole', y='MonthlyIncome', palette='Blues')
plt.title('Monthly Income Distribution by Job Role')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('../visuals/income_by_jobrole.png')
plt.show()

# --- 4. Job Satisfaction vs Attrition ---
sat_attr = df.groupby(['JobSatisfaction', 'Attrition']).size().unstack()
sat_attr.plot(kind='bar', figsize=(7, 5), color=['steelblue', 'salmon'])
plt.title('Job Satisfaction vs Attrition')
plt.xlabel('Job Satisfaction (1=Low, 4=High)')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('../visuals/satisfaction_vs_attrition.png')
plt.show()

# --- 5. Tenure vs Attrition ---
df['tenure_bucket'] = pd.cut(
    df['YearsAtCompany'],
    bins=[0, 2, 5, 10, 40],
    labels=['0-2 yrs', '3-5 yrs', '6-10 yrs', '10+ yrs']
)
tenure_attr = df.groupby(['tenure_bucket', 'Attrition']).size().unstack()
tenure_attr.plot(kind='bar', figsize=(8, 5), color=['steelblue', 'salmon'])
plt.title('Attrition by Tenure')
plt.xlabel('Years at Company')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('../visuals/attrition_by_tenure.png')
plt.show()

print("\nAll charts saved to /visuals folder.")
