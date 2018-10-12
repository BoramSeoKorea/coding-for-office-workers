#클래스 class

#####Article variables
titlel="development"
author1="marco"
content1="it is easy to develop"
view_count1=0

title2="coaching"
author2="marco"
content2="it is easy to coach"
view_count2=0

title3="founding"
author3="marco"
contecnt3="it is easy to found"
view_count3=0

#####Article class
#class Article:
#    title="development"
#    author="marco"
#    content="it is easy to develop"
#    view_count=0

#article1=Article()
#print(article1.title)
#article2=Article()
#article2.title="coaching"
#print(article1.title)
#print(article2.title)

#####Article class with __int__
class Article:
    author="marco"
    view_count=0

    def __init__(self, title, content):
        self.title=title
        self.conent=content

    def read(self):
        self.view_count=self.view_count+1

article1 = Article("development", "it is easy to develop")
article2 = Article("coaching", "it is easy to coach")
article3 = Article("fouding", "it is easy to found")

# print(article1.view_count)
# article1.read()
# #article.view_count1=article.view_coun1+1
# print(article1.view_count)


#####Article class inheritance 상속
class BrunchArticle(Article):
    source="brunch"

    def read(self):
        self.view_count=self.view_count+2

brunch_article=BrunchArticle("development", "it is easy to develop")
print(brunch_article.title)
print(brunch_article.source)
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)
