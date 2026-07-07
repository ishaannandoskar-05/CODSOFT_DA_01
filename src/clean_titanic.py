import pandas as pd
import numpy as np

df = pd.read_csv('titanic.csv')
original_shape = df.shape

print("="*60)
print("STEP 5: CLEANING")
print("="*60)

# 1. Handle missing Age -> fill with median (skewed by outliers, robust)
df['Age'] = df['Age'].fillna(df['Age'].median())
print(f"Filled {177} missing Age values with median: {df['Age'].median()}")

# 2. Handle missing Embarked -> fill with mode (only 2 missing)
mode_embarked = df['Embarked'].mode()[0]
df['Embarked'] = df['Embarked'].fillna(mode_embarked)
print(f"Filled missing Embarked values with mode: '{mode_embarked}'")

# 3. Handle Cabin -> 77% missing, too sparse to impute meaningfully.
#    Create a binary flag instead of dropping the column entirely.
df['Has_Cabin'] = df['Cabin'].notna().astype(int)
df.drop(columns=['Cabin'], inplace=True)
print("Dropped 'Cabin' column (77% missing), replaced with binary 'Has_Cabin' flag")

# 4. Remove exact duplicate rows (defensive, even though count was 0)
before = len(df)
df = df.drop_duplicates()
print(f"Removed {before - len(df)} duplicate rows")

# 5. Correct data types
df['Survived'] = df['Survived'].astype('category')
df['Pclass'] = df['Pclass'].astype('category')
df['Sex'] = df['Sex'].astype('category')
df['Embarked'] = df['Embarked'].astype('category')
print("Converted Survived, Pclass, Sex, Embarked to categorical dtype")

# 6. Standardize text (Sex/Embarked already clean, but strip just in case)
for col in ['Sex', 'Embarked']:
    df[col] = df[col].astype(str).str.strip()

# 7. Sanity checks on numeric ranges
assert df['Age'].between(0, 100).all(), "Invalid age found"
assert df['Fare'].ge(0).all(), "Negative fare found"
print("Passed sanity checks: Age in [0,100], Fare >= 0")

df.reset_index(drop=True, inplace=True)

print("\n" + "="*60)
print("STEP 6: FINAL VALIDATION")
print("="*60)
print("Shape before:", original_shape, "-> after:", df.shape)
print("\nRemaining missing values:\n", df.isnull().sum())
print("\nFinal dtypes:\n", df.dtypes)

# Bonus: Save cleaned dataset
df.to_csv('titanic_cleaned.csv', index=False)
print("\nSaved cleaned dataset to titanic_cleaned.csv")
