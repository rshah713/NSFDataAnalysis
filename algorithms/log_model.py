from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd


"download the second sheet of condensed data into excel (.xlsx)"

df = pd.read_excel("condensed_data.xlsx")

print(df)
"""X is the independent varaibles"""


X = df[["first name", "last name", "student gender", "student's njit college", "race", 
        "ethnicity", "faculty advisor gender", "faculty advisor race", 
        "faculty advisor ethnicity", "entrepreneur mentor gender", "entrepreneur mentor race", 
        "entrepreneur mentor ethnicity", "batch", "Which college did the entrepreneur graduate from?", 
        "Year Graduated and Field of Study", "phd or postdoc entrepreneur?", "industry mentor name", 
        "industry mentor gender", "industry mentor race", "nationals"]]
y = df["nationals"]


"""dummify all data"""
X_dummies = pd.get_dummies(X, drop_files=True)
df = df.drop(X.columns, axis=1)
df_final = pd.concat([df, X_dummies], axis=1)
'''data_with_dummies = pd.get_dummies(data, columns = [])'''

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state = 42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

"""Tasks: finish matching the teams, add the nationals columns to the data, 
clean up the spreadsheet data and properly align columns, create dummy variables 
for all independent varaibles, build linear regression model"""
"run this when teseting out code in virtual environment: pip install pandas scikit-learn openpyxl"

"rough goal for next week: finish the first draft for logistic model code, finish matching up the teams, and finish cleaning up the categories"