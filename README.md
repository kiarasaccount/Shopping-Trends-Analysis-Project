# Shopping-Trends-Analysis-Project
A mini project showcasing seasonal shopping trends by age groups
This workspace contains two similar analysis scripts that summarise shopping behavior by age groups:

- `Project attempt 1.py`
- `python age_shopping_analysis.py`

This project analyzes how age affects shopping preferences, focusing on:

How much money different age groups spend?

How frequently they shop?

How these behaviors vary across months/seasons?

The analysis is based on a dataset called Shopping_behavior_updated.csv, which contains customer demographic and shopping behavior data. Sourced from https://www.kaggle.com/datasets/brandmustafa/shopping-trends 

Findings:

Younger customers (18–24) spend the most in Winter, Fall and Spring however spend the least in Summer.

Middle-aged groups (33–45) tend to spend more consistently year-round.

Older groups (45+) spend more in specific seasons (e.g., holidays).

It is important to remember that this data is USA specific therefore, I wouldn't apply these findings to analysing consumers worldwide.
Prices tend to spike in Summer, hence why older age groups may spend more during that season, they typically have more disposable income.










If you see "ModuleNotFoundError: No module named 'matplotlib'" or similar, install dependencies first.

Install dependencies (PowerShell):

```powershell
python -m pip install -r requirements.txt
```

Then run the scripts (PowerShell):

```powershell
python "Project attempt 1.py"
python "python age_shopping_analysis.py"
```

If plotting libraries are missing, the scripts will still run and will print summaries to the console instead of showing plots.

Saved plots
-----------
If matplotlib and seaborn are installed the scripts will also save PNG files to the `plots/` directory in this project. Filenames include a timestamp, for example:

```
plots/average_spending_by_agegroup_20251109_142530.png
plots/average_frequency_by_agegroup_20251109_142531.png
```

Install dependencies and re-run the scripts to produce those images.
