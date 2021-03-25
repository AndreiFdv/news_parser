from .models import *
import newspaper

cnn_paper = newspaper.build('http://cnn.com')

for a in cnn_paper.articles:
   article_=Article(a.url)
   article_.download()
   article_.parse()
   article(title=article_.title,content=article_.text).save()



