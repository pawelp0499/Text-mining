from services.read_file import read_file
from wordcloud import *
import matplotlib.pyplot as plt


read_and_cleaned_csv = read_file("./data/true.csv", "title")
print(read_and_cleaned_csv)

text = read_and_cleaned_csv[0]
wordcloud = WordCloud(width=640, height=480,
                      background_color='white').generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('./images/wordcloud.png')
plt.show()
