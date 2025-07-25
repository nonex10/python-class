from django.db import models
#making a good model/ projects or table of database
#django ORM, helps in mapping
# Create your models here.

#class <modelname>, ORM feature in python by using models.Model for inheritance
class Blog(models.Model):
    # id=models.UUIDField()
    title=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=500)

    description=models.TimeField()

    def str(self):
        return self.title

    class Meta:
        db_table="Blogs"

class Comments(models.Model):
    review=models.CharField(max_length=200)
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)

    def str(self):
        return self.review
    class Meta:
        db_table="comments"