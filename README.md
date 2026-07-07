# Titanic Dataset — Data Cleaning Project

**CodSoft Internship — Data Science Track**
**Task 1: Data Cleaning**

## Task Objectives
- Import a dataset using Python and inspect its structure
- Identify missing values, duplicate records, and inconsistent data entries
- Clean the dataset by handling null values, removing duplicates, and correcting data types
- Prepare the data for further analysis using Pandas
- Bonus: Save the cleaned dataset as a new CSV file

## Dataset
- **Name:** Titanic - Machine Learning from Disaster
- **Original source (Kaggle):** https://www.kaggle.com/competitions/titanic/data
- **Direct download used in this project (GitHub mirror, no login required):**
  https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

> Note: Kaggle requires a free account + API token to download directly via their API/CLI.
> If you want the file straight from Kaggle:
> 1. Create an account at kaggle.com
> 2. Go to the link above and click "Download"
> 3. Or use the Kaggle CLI: `kaggle competitions download -c titanic`

## Folder Structure

```
titanic-data-cleaning/
├── data/
│   ├── raw/
│   │   └── titanic.csv              # original, unmodified dataset (891 rows)
│   └── processed/
│       └── titanic_cleaned.csv      # cleaned dataset, ready for analysis
├── notebooks/
│   └── data_cleaning.ipynb          # step-by-step cleaning notebook (with outputs)
├── src/
│   └── clean_titanic.py             # standalone script version of the cleaning steps
└── README.md
```

## What was cleaned
| Column     | Issue                        | Fix                                             |
|------------|-------------------------------|--------------------------------------------------|
| Age        | 177 missing (19.87%)          | Filled with median                                |
| Embarked   | 2 missing (0.22%)             | Filled with mode                                  |
| Cabin      | 687 missing (77.1%)           | Dropped column, replaced with binary `Has_Cabin`  |
| Survived/Pclass/Sex/Embarked | stored as generic types | Converted to `category` dtype |
| Duplicates | 0 found                       | Verified with `drop_duplicates()`                 |

## How to run
```bash
cd notebooks
jupyter notebook data_cleaning.ipynb
```
or run the script directly:
```bash
cd src
python clean_titanic.py
```

## Submission
Completed as part of the **CodSoft Data Science Internship**, Task 1 (Data Cleaning).