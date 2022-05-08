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


y = result[['type']]
X = result[['title']]

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=1)

vectorizer = CountVectorizer(tokenizer=text_tokenizer)

X_train_array = vectorizer.fit_transform(X_train).toarray()
X_test_array = vectorizer.fit_transform(X_test).toarray()
y_train_array = vectorizer.fit_transform(y_train).toarray()
y_test_array = vectorizer.fit_transform(y_test).toarray()

# Decision Tree  Classifier

clf = DecisionTreeClassifier()

clf = clf.fit(X_train_array, y_train_array)

y_pred = clf.predict(X_test_array)

print("Accuracy:", metrics.accuracy_score(y_test_array, y_pred))

# Random forest

crf = RandomForestClassifier(n_estimators=100)

crf.fit(X_train_array, y_train_array)

y_pred = crf.predict(X_test_array)

print("Accuracy:", metrics.accuracy_score(y_test_array, y_pred))
