from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Catagory(models.Model):
    catagory_name = models.CharField(max_length=255)
    def __str__(self):
        return self.catagory_name

    def get_cata_count(self):
        catagory=Catagory.objects.get(catagory_name=self.catagory_name)
        return catagory.catagories.all().count()



class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    post_detail = models.TextField()
    author = models.ForeignKey(Author,related_name='posts',on_delete=models.CASCADE)
    catagory = models.ForeignKey(Catagory,related_name="catagories",on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering =['-pub_date']

    def summary(self):
        return self.post_detail[:100]+"..."

    def __str__(self):
        return self.title

    def comment_count(self):
        comment = Post.objects.get(title=self.title)
        return comment.comments.all().count()



class Comment(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    post =models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    user_comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    approve_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['-comment_date']

    def approve(self):
        self.approve_comment =True
        self.save()

    def __str__(self):
        return self.user_comment

class Problem(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()

    def __str__(self):
        return self.title

