# Classification

- A `classification` is a supervised machine learning approach used to label an example
as belonging to one of a finite set of categories or classes
- Binary classification (when only two classes exist), 
  - Example: Deciding whether an email message is spam or not
- Multi-class classification, when more than two classes exist
- Multi-label classification, when an example can belongs to more than one classe

## Some Example of Classifier Models

### KNN

- One of simplest supervised learning approach used for classification as well as regression problems.
- "*New examples are assigned a label or class based on how similar they are to other examples in the training*" data using 
the majority vote technique
- Gives poor results when classes ara imbalanced
- Note scalable when the training data is large:
  - Need to reduce training size in this case and one could use K-Fold cross validation for performance evaluation
- Influenced by features' scales (when they have different scales)

### Logistic Regression
 - Example
   - [sklearn.linear_model.LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)