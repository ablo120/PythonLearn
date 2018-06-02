# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import jieba

f = open(u'text.txt','r').read()
cut_text="".join(jieba.cut(f))
wordcloud = WordCloud(font_path='./font/simhei.ttf',background_color="white",width=1000, height=860, margin=2).generate(cut_text)


import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

