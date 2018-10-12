#Making a school class
#Must include Name, A year of establishment and Address

#####Article variables
Name="Aschool"
establishment="2000"
Address="korea"

Name="Bschool"
establishment="2010"
Address="Singapore"

Name="cschool"
establishment="2020"
Address="UnitedState"

class Article:
    def __init__(self, Name, establishment, Address):
        self.Name=Name
        self.establishment=establishment
        self.Address=Address

article1=Article("Aschool","2000","korea")
article2=Article("Bschool","2010","Singapore")
article3=Article("Cschool","2020","UnitedState")

article=Article("Aschool","2000","korea")

print(article.Name)
print(article.establishment)
print(article.Address)
