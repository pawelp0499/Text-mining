from sklearn.feature_extraction.text import CountVectorizer
from services.text_tokenizer import text_tokenizer
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier


true = pd.read_csv('./data/True.csv', usecols=['title', 'text'])
true['type'] = 'True'

fake = pd.read_csv('./data/Fake.csv', usecols=['title', 'text'])
fake['type'] = 'Fake'

frames = [true, fake]
result = pd.concat(frames)

y = result['type']
X = result['title']

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=0)

vectorizer = CountVectorizer(tokenizer=text_tokenizer)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print(X_train.shape)

# Decision Tree

clf = DecisionTreeClassifier()

clf = clf.fit(X_train, y_train)

y_pred_1 = clf.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred_1))
print("Accuracy:", metrics.classification_report(y_test, y_pred_1))

'''
# Random forest

crf = RandomForestClassifier(n_estimators=100)

crf.fit(X_train, y_train)

y_pred_2 = crf.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred_2))
print("Accuracy:", metrics.classification_report(y_test, y_pred_2))
'''