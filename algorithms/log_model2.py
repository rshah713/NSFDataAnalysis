from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import pandas as pd
import numpy as np
										
# run in virtual environment
df = pd.read_excel("condensed_data.xlsx")
df = df.drop_duplicates(keep='first')
df.columns = df.columns.str.strip()
df = df.rename(columns={'(DV) Student \nGender': '(DV) Student Gender'})
print(df[["NATIONALS", "(DV) Student Gender", "DV (Race)", "DV (Ethnicity)"]])
print(df['NATIONALS'].value_counts())
#print(df.columns)

feature_cols = ['(DV) Student Gender', 'DV (Race)', 'DV (Ethnicity)']
X = df[feature_cols]
y = df.NATIONALS

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)

logreg = LogisticRegression(random_state=16)

logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

print("\nModel Coefficients (weights):")
print("Gender (1=Female), Race(1=African American), Ethnicity(1=Hispanic)")
print(logreg.coef_)

print("\nIntercept:")
print("Likelihood of getting to nationals if all dummy values are 0 i.e. male nonHispanic nonBlack")
print(logreg.intercept_)
print("Converting log_odds value to a probability using logistic function...")
print("0.0343") # why is it hardcoded?

accuracy = accuracy_score(y_test, y_pred) # must be balanced for accuracy to be a good metric
print(f"\nAccuracy: {accuracy:.4f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print()

# Check for missing values
print(df.isna().sum())

# calculate t test statistic
# invert 2nd derivative log likelihood function
probs = logreg.predict_proba(X_train)

X_train_np = X_train.to_numpy()

# use Hessian matrix 
# X.T * W * X
W = np.diag((probs[:, 1] * (1 - probs[:, 1])))
XTWX = np.dot(X_train_np.T, np.dot(W, X_train_np))
cov_matrix = np.linalg.inv(XTWX) # invert it

# recall t = coeffecient / standard error
standard_errors = np.sqrt(np.diag(cov_matrix))
coefficients = logreg.coef_[0]
t_scores = coefficients / standard_errors
print(f"{feature_cols[0]}: Coefficient = {coefficients[0]:.4f}, SE = {standard_errors[0]:.4f}, T-Stat = {t_scores[0]:.4f}")
print(f"{feature_cols[1]}: Coefficient = {coefficients[1]:.4f}, SE = {standard_errors[1]:.4f}, T-Stat = {t_scores[1]:.4f}")
print(f"{feature_cols[2]}: Coefficient = {coefficients[1]:.4f}, SE = {standard_errors[1]:.4f}, T-Stat = {t_scores[1]:.4f}")

# print("\nClassification Report:")
# print(classification_report(y_test, y_pred))



