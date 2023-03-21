# Loan Approval Prediction Model

![Loan_pic](/loan_pic.jpg)


This is a machine learning project that aims to predict loan approval status for borrowers based on their data. The project uses a loan dataset that includes information about borrowers' gender, education, credit history, and other features. The ultimate goal of this project is to help banks and financial institutions accurately assess the risk of a borrower approval on a loan, which can result in a loss of revenue and damage to their reputation.

## Dependencies

The project relies on the following Python packages: <br>
```pandas``` <br>
```numpy``` <br>
```scikit-learn``` <br>
```matplotbli``` <br>
```seaborn``` <br>


## Feature Engineering

In the loan dataset, we dropped the Loan_ID column as it is irrelevant to our analysis. We also replaced missing values with their mean and applied label encoding to the categorical features to convert them to numerical values.

## Research Questions
The project answers the following research questions through visualizations:

1. What is the distribution of loan_status among the different gender groups in the dataset? Are men more likely to get approved for a loan than women?

2. How does the applicant's education level affect their loan approval status? Are graduates more likely to get approved than undergraduates?

3. Does credit_history have a significant impact on loan approval status? Are applicants with a good credit history more likely to get approved for a loan than those with a poor credit history?

4. Can we predict loan_status accurately based on the given features using a machine learning algorithm? If so, which algorithm performs the best? What features are most important in predicting loan approval status?

## Building the Model

The project uses the following machine learning models to predict loan approval status:

KNeighborsClassifier
Support Vector Classifier (SVC)
Logistic Regression
Random Forest Classifier
We used cross-validation to evaluate the performance of each model, and found that Logistic Regression had the highest accuracy, with a score of 80.28%.

## Conclusion
Overall, the project demonstrates the importance of credit history in the loan approval process, and underscores the need for applicants to maintain a good credit score to increase their chances of being approved for a loan. The project also shows that machine learning algorithms can accurately predict loan approval status based on the given features, and Logistic Regression is the most suitable algorithm for this task.