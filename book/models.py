from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField
    book_title = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
    book_price = models.IntegerField(default=0)
    book_desc = models.CharField(max_length=300)
    book_pub_date = models.DateField()
    book_image = models.ImageField(upload_to="book/images", default="")

    def __str__(self):
        return (str(self.book_name) + " by " + str(self.book_author))
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return (str(self.name + " - " + self.email  + " - " + self.phone + " - " + self.desc))
    
class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=50)
    cust_email = models.CharField(max_length=50)
    cust_phone = models.CharField(max_length=50)
    cust_password = models.CharField(max_length=50)
    
    def __str__(self):
        return (str(self.cust_name + " - " + self.cust_email  + " - " + self.cust_phone + " - " + self.cust_password))
    
    @staticmethod
    def get_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    @staticmethod
    def get_pass(password):
        try:
            return Customer.objects.get(password=password)
        except:
            return False

    @staticmethod
    def get_detail(email):
        return Customer.objects.get(email=email)