from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import pandas as pd
										
# run in virtual environment
df = pd.read_excel("condensed_data.xlsx")
df.columns = df.columns.str.strip()
df = df.rename(columns={'(DV) Student \nGender': '(DV) Student Gender'})
print(df[["NATIONALS", "(DV) Student Gender", "DV (Race)"]])
#print(df.columns)

feature_cols = ['(DV) Student Gender', 'DV (Race)']
X = df[feature_cols]
y = df.NATIONALS

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)

logreg = LogisticRegression(random_state=16)

logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

print("\nModel Coefficients (weights):")
print(logreg.coef_)

print("\nIntercept:")
print(logreg.intercept_)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.4f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))



