# ===============================
# Shopping Trends Age & Monthly Analysis
# ===============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load dataset ---
df = pd.read_csv("Shopping_behavior_updated.csv")

# --- Quick check ---
print("Preview of dataset:")
print(df.head(), "\n")

# --- Clean relevant columns ---
df = df.dropna(subset=['Age', 'Purchase Amount (USD)', 'Previous Purchases', 'Season'])

# --- Create Age Groups ---
bins = [17, 24, 32, 45, 120]
labels = ['18-24', '25-32', '33-45', '45+']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

# --- Create a Month column from 'Season' ---
# Assuming 'Season' is categorical (Winter, Spring, Summer, Fall)
# We'll map it to an approximate month number for time-based grouping
season_to_month = {
    'Winter': 1,
    'Spring': 4,
    'Summer': 7,
    'Fall': 10
}
df['Month'] = df['Season'].map(season_to_month)

# --- Check mapping success ---
if df['Month'].isna().any():
    print("⚠️ Some Season values didn’t map correctly — check unique values in 'Season':")
    print(df['Season'].unique())

# --- Group by AgeGroup and Month ---
grouped = (
    df.groupby(['AgeGroup', 'Month'])
    .agg({
        'Purchase Amount (USD)': 'mean',
        'Previous Purchases': 'mean'
    })
    .reset_index()
)

# --- Analysis summaries ---
print("\nAverage spending and frequency by age group and month:")
print(grouped.head(10))

# --- Visualization 1: Spending by Age Group per Month ---
plt.figure(figsize=(10, 6))
sns.lineplot(data=grouped, x='Month', y='Purchase Amount (USD)', hue='AgeGroup', marker='o')
plt.title('Average Monthly Spending by Age Group')
plt.xlabel('Month (approx. based on Season)')
plt.ylabel('Average Purchase Amount (USD)')
plt.xticks([1, 4, 7, 10], ['Winter', 'Spring', 'Summer', 'Fall'])
plt.legend(title='Age Group')
plt.tight_layout()
plt.show()

# --- Visualization 2: Frequency by Age Group per Month ---
plt.figure(figsize=(10, 6))
sns.lineplot(data=grouped, x='Month', y='Previous Purchases', hue='AgeGroup', marker='o')
plt.title('Average Monthly Shopping Frequency by Age Group')
plt.xlabel('Month (approx. based on Season)')
plt.ylabel('Average Number of Previous Purchases')
plt.xticks([1, 4, 7, 10], ['Winter', 'Spring', 'Summer', 'Fall'])
plt.legend(title='Age Group')
plt.tight_layout()
plt.show()

# --- Visualization 3: Combined bar chart for Spending vs Frequency ---
melted = grouped.melt(
    id_vars=['AgeGroup', 'Month'],
    value_vars=['Purchase Amount (USD)', 'Previous Purchases'],
    var_name='Metric',
    value_name='Average Value'
)

plt.figure(figsize=(10, 6))
sns.barplot(data=melted, x='Month', y='Average Value', hue='Metric', palette='coolwarm')
plt.title('Comparison of Spending and Frequency by Month (All Age Groups)')
plt.xlabel('Month (approx. based on Season)')
plt.ylabel('Average Value')
plt.xticks([0, 1, 2, 3], ['Winter', 'Spring', 'Summer', 'Fall'])
plt.tight_layout()
plt.show()

# --- Correlation check ---
corr = df['Age'].corr(df['Purchase Amount (USD)'])
print(f"\nCorrelation between Age and Purchase Amount: {corr:.2f}")

