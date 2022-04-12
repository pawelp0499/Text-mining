from main import *
import matplotlib.pyplot as plt
from tabulate import tabulate


''' Bar plot of quantity top 10 tokens in true news '''

top_10_tokens = titles[np.argpartition(column_sum, -10)[-10:]]
top_10_quantity = column_sum[max_val_col]

plt.barh(top_10_tokens, top_10_quantity, color='cyan')
plt.title('Number of top 10 tokens in true news')
plt.xlabel('Quantity')
plt.ylabel('Tokens')
plt.savefig('./images/quantity.png')
plt.show()

''' Pretty table '''

df_1 = pd.DataFrame({'titles': top_10_tokens, 'quantity': top_10_quantity})

top_10_tf_tokens = titles[np.argpartition(tf_col_sum, -10)[-10:]]
top_10_tf_quantity = tf_col_sum[max_tf_val_col]
print(tabulate(df_1, headers='keys', tablefmt='psql'))

''' Bar plot of TF-IDF indexes top 10 most important tokens in true news '''

plt.barh(top_10_tf_tokens, top_10_tf_quantity, color='magenta')
plt.title('TFIDF of top 10 most important tokens in true news')
plt.xlabel('TFIDF')
plt.ylabel('Tokens')
plt.savefig('./images/tf-idf.png')
plt.show()

''' Pretty table '''

df_2 = pd.DataFrame({'titles': top_10_tf_tokens, 'TFIDF': top_10_tf_quantity})
print(tabulate(df_2, headers='keys', tablefmt='psql'))

'''Binary weight'''

vectorizer_bw = CountVectorizer(tokenizer=text_tokenizer, binary=True)
X_transform_bw_sample = vectorizer_bw.fit_transform(sample)
titles_bw = (vectorizer_bw.get_feature_names_out())
array_bw = X_transform_bw_sample.toarray()

column_sum_bw = np.sum(array_bw, axis=0)
max_val_col_bw = np.argpartition(column_sum_bw, -10)[-10:]
top_10_bw = column_sum_bw[max_val_col_bw]
print(top_10_bw)
print(titles_bw[np.argpartition(column_sum_bw, -10)[-10:]])

top_10_bw_terms = titles_bw[np.argpartition(column_sum_bw, -10)[-10:]]

plt.barh(top_10_bw_terms, top_10_bw, color='red')
plt.title('Top 10 Crucial Tokens based on binary weight')
plt.xlabel('Weight')
plt.ylabel('Term')
plt.savefig('./images/tf-binary-weight.png')
plt.show()

''' Pretty table '''

df_3 = pd.DataFrame({'term': top_10_bw_terms, 'weight': top_10_bw})
print(tabulate(df_3, headers='keys', tablefmt='psql'))