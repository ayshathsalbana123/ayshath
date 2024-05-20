from django.db import models


# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class Productdetails(models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.IntegerField(null=True)
    product_stock=models.IntegerField(null=True)
    product_category= models.CharField(max_length=20, null=True)
    product_subcategory= models.CharField(max_length=20, null=True)
    product_image = models.FileField()


    def __str__(self):
        return self.product_name



class cart(models.Model):
    user_details=models.ForeignKey(Register,on_delete=models.CASCADE)
    product_details=models.ForeignKey(Productdetails,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total_price = models.IntegerField(default=0)


class Wishlist(models.Model):
    user_details = models.ForeignKey(Register, on_delete=models.CASCADE)
    product_details = models.ForeignKey(Productdetails, on_delete=models.CASCADE)


class PasswordReset(models.Model):
    user=models.ForeignKey(Register,on_delete=models.CASCADE)
    token=models.CharField(max_length=40)



class deliverydetails(models.Model):
    user_details=models.ForeignKey(Register,on_delete=models.CASCADE)
    product_details_2=models.ForeignKey(Productdetails,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=20,null=True)
    phone = models.IntegerField(null=True)
    pincode=models.CharField(max_length=10,null=True)
    state=models.CharField(max_length=15,null=True)
    address=models.CharField(max_length=40,null=True)
    city = models.CharField(max_length=20,null=True)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(null=True)
    payment_status = models.CharField(max_length=20, null='PAID')
    purchase_date = models.DateTimeField(auto_now=True, null=True)
    product_status = models.CharField(max_length=50, null=True, default='Order Placed')
    instruction = models.CharField(max_length=50, null=True, default='Your Order Has Been Successfully Placed')


