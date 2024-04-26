from django.db import models
from django.utils import timezone

# Create your models here.
class LibraryMember(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

class Books(models.Model):
    bookID=models.CharField(primary_key=True,max_length=20)
    bookname=models.CharField(max_length=50)
    authorname=models.CharField(max_length=50)

class Issuedbooks(models.Model):
    bookID=models.ForeignKey(Books,on_delete=models.CASCADE)
    username=models.ForeignKey(LibraryMember,on_delete=models.CASCADE)
    email = models.ForeignKey(LibraryMember, on_delete=models.CASCADE, related_name='issued_books_email')
    issuedate=models.DateField(default=timezone.now)
    returndate=models.DateField(null=True,blank=True)
    dailydate=models.DateField(null=True,blank=True)


class Availablebooks(models.Model):
    bookID=models.CharField(primary_key=True,max_length=20)
    bookname=models.CharField(max_length=50)
    authorname=models.CharField(max_length=50)

class DeletedBooks(models.Model):
    bookID = models.CharField(primary_key=True, max_length=20)
    bookname = models.CharField(max_length=50)
    authorname = models.CharField(max_length=50)







