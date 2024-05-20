from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
import os
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from datetime import datetime
import razorpay
# import pkg_resources





# Create your views here.


def display(request):
    return HttpResponse("ayshath")


def index(request):
    if 'id' in request.session:
        user=Register.objects.get(username=request.session['id'])
        data=Productdetails.objects.all()
        l=[]
        l1=[]
        try:
            data1=cart.objects.filter(user_details=user)
            for i in data1:
                l.append(i.product_details)
        except:
            pass
        try:
            wish=Wishlist.objects.filter(user_details=user)
            for i in wish:
                l1.append(i.product_details)
        except:
            pass

        return render(request,'index.html',{'data':user,'data1':data,'d1':data,'d2':wish,'list':l})
    return redirect(login)



def register(request):
        if request.method=='POST':
            username=request.POST['n1']
            email=request.POST['n2']
            phone=request.POST['n3']
            password=request.POST['n4']
            c_password=request.POST['n5']
            if password == c_password:
                if Register.objects.filter(username=username).exists():
                    messages.info(request, "Username already Registered", extra_tags="signup")
                    return redirect(register)
                else:
                    val=Register.objects.create(username=username, email=email, phone=phone, password=password)
                    val.save()
                    messages.info(request, "Registered Successfully", extra_tags="signup")
                    return redirect(login)
            else:
                messages.info(request, "Password doesn't match", extra_tags="signup")
                return redirect(register)

        return render(request, 'register.html')


def adminhome(request):
    return render(request, 'adminhome.html')


def login(request):
    if request.method=='POST':
        u=request.POST['n1']
        p=request.POST['n2']
        try:
            data=Register.objects.get(username=u)
            if p==data.password:
                request.session['id']=u#session creation using id
                return redirect(userhome)
            else:
                messages.error(request,'Incorrect password')
        except Exception:
            if u=='admin' and p=='admin':
                request.session['id1']=u
                return redirect(adminhome)
            else:
                messages.error(request,"incorrect password and username")
    return render(request,'login.html')


def wishlist(request):
    return render(request, 'wishlist.html')


def shop(request):
    return render(request, 'shop.html')


def checkout(request):
    return render(request, 'checkout.html')


def userhome(request):
    if 'id' in request.session:
        user=Register.objects.get(username=request.session['id'])
        data=Productdetails.objects.all()
        d1=cart.objects.all()
        print(d1)
        l=[]
        l1=[]
        try:
            data1=cart.objects.filter(user_details=user)
            for i in data1:
                l.append(i.product_details)
        except:
            pass
        try:
            wish=Wishlist.objects.filter(user_details=user)
            for i in wish:
                l1.append(i.product_details)
        except:
            pass

        return render(request,'userhome.html',{'data':user,'data1':data,'d1':d1,'d2':wish,'list':l,'list1':l1})
    return redirect(login)



def contact(request):
    return render(request, 'contact.html')


def empty_contact(request):
    return render(request, 'empty_contact.html')


def about(request):
    return render(request, 'about.html')


def empty_about(request):
    return render(request, 'empty_about.html')


def myaccount(request):
    return render(request, 'my-account.html')


def viewuser(request):
    data =Register.objects.all()
    return render(request, 'viewuser.html', {'data': data})


def add_product(request):
    if request.method == 'POST':
        product_name = request.POST['n1']
        product_price = request.POST['n2']
        product_stock = request.POST['n3']
        product_image = request.FILES['n4']
        product_category= request.POST['n5']
        product_subcategory= request.POST['n6']
        data = Productdetails.objects.create(product_name=product_name, product_price=product_price,
             product_stock=product_stock, product_image=product_image,product_category=product_category,product_subcategory=product_subcategory)
        data.save()
        messages.success(request, 'Data Saved')
        return render(request, 'add_product.html')
    return render(request, 'add_product.html')




def display_product(request):
    data = Productdetails.objects.all()
    return render(request, 'display_product.html', {'data': data})

def delete_product(request,d):
    data=Productdetails.objects.filter(pk=d)
    data.delete()
    messages.success(request,'Data Deleted')
    return redirect(display_product)


def update_details(request,d):
    data=Productdetails.objects.get(id=d)
    if request.method=='POST':
        if len(request.FILES)!=0:
            if len(data.product_image)>0:
                os.remove(data.product_image.path)
            data.product_image=request.FILES['n4']
        data.product_name= request.POST.get('n1')
        data.product_price = request.POST.get('n2')
        data.product_stock = request.POST.get('n3')
        data.product_category = request.POST.get('n5')
        data.product_subcategory = request.POST.get('n6')
        data.save()
        messages.success(request,'Product Updated Successfully')
        return redirect(display_product)
    data=Productdetails.objects.filter(pk=d)
    return render(request,'update.html',{'data':data})


def logout(request):
    return render(request, 'logout.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        print("email",email)
        try:
            user = Register.objects.get(email=email)
            print(user)
        except:
            messages.info(request,"Email id not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user=user, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            # return render(request, 'emailsent.html')
        except:
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'forgot_password.html')

def reset_pwd(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    usr = Register.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            password_reset.user.password=new_password
            password_reset.user.save()
            # password_reset.delete()
            return redirect(login)
    return render(request, 'reset_pwd.html',{'token':token})


def empty_cart(request):
    return render(request, 'empty_cart.html')

def empty_wishlist(request):
    return render(request, 'empty_wishlist.html')


def add_cart(request,pid):
    if 'id' in request.session:
        user=Register.objects.get(username=request.session['id'])
        data=Productdetails.objects.get(pk=pid)
        cart_details = cart.objects.create(user_details=user, product_details=data, )
        cart_details.save()
        messages.success(request, 'cart added successfully')
        return redirect(userhome)
    return redirect(login)


def display_cart(request):
    data=Register.objects.get(username=request.session['id'])
    user=cart.objects.filter(user_details=data)
    qty=1
    total=0
    c=0
    for i in user:
        print(i.product_details.product_price)
        c=c+1
        total +=i.product_details.product_price*i.quantity
        print(total)
    return render(request,'cart.html',{'key':user,'total':total,'qty':qty})


def delete_from_cart(request,d):
    data=cart.objects.filter(pk=d)
    data.delete()
    messages.success(request,'removed from cart')
    return redirect(display_cart)


def wishlist(request,d):
    if 'id' in request.session:
        user=Register.objects.get(username=request.session['id'])
        product=Productdetails.objects.get(pk=d)
        if Wishlist.objects.filter(product_details_id=d).exists():
            messages.error(request, 'Already added to wishlist')
        else:
            cartdetails=Wishlist.objects.create(user_details=user,product_details=product)
            cartdetails.save()
            messages.success(request,'added to wishlist')
        return redirect(display_wishlist)
    return render(request, 'userhome.html')

def display_wishlist(request):
    user_name=Register.objects.get(username=request.session['id'])
    userdetails=Wishlist.objects.filter(user_details=user_name)
    return render(request,'wishlist.html',{'key':userdetails})


def remove_wishlist(request,d):
    data=Wishlist.objects.filter(pk=d)
    data.delete()
    messages.success(request,'removed from wishlist')
    return redirect(display_wishlist)


def increment_quantity(request,cart_id):
    cart_item=cart.objects.get(pk=cart_id)
    if cart_item.product_details.product_stock>0:
        cart_item.quantity+=1
        cart_item.save()
        cart_item.total_price=cart_item.quantity*cart_item.product_details.product_price
        cart_item.save()

    return redirect(display_cart)

def decrement_quantity(request,cart_id):
    cart_item=cart.objects.get(pk=cart_id)
    if cart_item.quantity>1:
        cart_item.quantity-=1
        cart_item.save()
    return redirect(display_cart)


def newborn(request):
        if 'id' in request.session:
            d=Productdetails.objects.filter(product_category='newborn')
            return render(request, 'newborn.html', {'data': d})
        return redirect(login)


def baby_boy(request):
    if 'id' in request.session:
        d = Productdetails.objects.filter(product_category='baby boy')
        return render(request, 'baby_boys.html', {'data': d})
    return redirect(login)


def upto6_boy(request):
    if 'id' in request.session:
        d = Productdetails.objects.filter(product_subcategory='3-6M_boy')
        return render(request, '3-6M_boy.html', {'data': d})
    return redirect(login)


def upto9_boy(request):
    if 'id' in request.session:
        d = Productdetails.objects.filter(product_subcategory='6-9M_boy')
        return render(request, '6-9M_boy.html', {'data': d})
    return redirect(login)


def upto12_boy(request):
    if 'id' in request.session:
        d = Productdetails.objects.filter(product_subcategory='9-12M_boy')
        return render(request, '9-12M_boy.html', {'data': d})
    return redirect(login)


def upto18_boy(request):
    if 'id' in request.session:
        d = Productdetails.objects.filter(product_subcategory='12-18M_boy')
        return render(request, '12-18M_boy.html', {'data': d})
    return redirect(login)


def upto24_boy(request):
    if 'id' in request.session:
        d = Productdetails.objects.filter(product_subcategory='18-24M_boy')
        return render(request, '18-24M_boy.html', {'data': d})
    return redirect(login)



def baby_girl(request):
    if 'id' in request.session:
        d = Productdetails.objects.filter(product_category='baby girl')
        return render(request, 'baby_girls.html', {'data': d})
    return redirect(login)


def upto6_girl(request):
    if 'id' in request.session:
        d = Productdetails.objects.filter(product_subcategory='3-6M_girl')
        return render(request, '3-6M_girl.html', {'data': d})
    return redirect(login)


def upto9_girl(request):
    if 'id' in request.session:
        d = Productdetails.objects.filter(product_subcategory='6-9M_girl')
        return render(request, '6-9M_girl.html', {'data': d})
    return redirect(login)


def upto12_girl(request):
    if 'id' in request.session:
        d = Productdetails.objects.filter(product_subcategory='9-12M_girl')
        return render(request, '9-12M_girl.html', {'data': d})
    return redirect(login)


def upto18_girl(request):
    if 'id' in request.session:
        d = Productdetails.objects.filter(product_subcategory='12-18M_girl')
        return render(request, '12-18M_girl.html', {'data': d})
    return redirect(login)


def upto24_girl(request):
    if 'id' in request.session:
        d = Productdetails.objects.filter(product_subcategory='18-24M_girl')
        return render(request, '18-24M_girl.html', {'data': d})
    return redirect(login)


def delivery_details(request,d):
    f = Productdetails.objects.get(pk=d)
    if request.method == "POST":
        s=Register.objects.get(username=request.session['id'])
        amount=f.product_price
        fullname=request.POST['name']
        phone=request.POST['phone']
        total_price= request.POST['total_price']
        pincode=request.POST['pincode']
        state=request.POST['state']
        address= request.POST['address']
        city= request.POST['city']
        user=deliverydetails.objects.create(fullname=fullname,phone=phone,total_price=total_price,pincode=pincode,state=state,address=address,city=city,user_details=s,product_details_2=f,payment_status='PAID')
        user.save()
        f.product_stock=f.product_stock-1
        f.save()
        messages.success(request,"Payment successfully")
        return redirect('payment',amount)

    else:
        user1= Register.objects.get(username=request.session['id'])
        return render(request,"delivery_details.html",{"user1":user1,"item":f})



def payment(request,amount):
    print(amount)
    amount = int(amount) * 100
    order_currency = 'INR'
    client = razorpay.Client(auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    return render(request, "payment.html",{'amount':amount})


def success_page(request):
    return render(request, 'success_page.html')


def profile(request):
    if 'id' in request.session:
        data = Register.objects.get(username=request.session['id'])
        return render(request,'userprofile.html',{'data':data})
    return redirect(login)

def updateprofile(request):
    if 'id' in request.session:
        if request.method == 'POST':
            b = request.POST['phone']
            c = request.POST['email']
            d = request.POST['username']
            Register.objects.filter(username=request.session['id']).update( phone=b, email=c, username=d)
            messages.success(request,'Profile Updated')
        return redirect(profile)


def user_recentorders(request):
    if 'id' in request.session:
        user = Register.objects.get(username=request.session['id'])
        order = deliverydetails.objects.filter(user_details=user,payment_status='PAID').order_by('purchase_date')
        print(order)
        return render(request, 'recentorder.html',{'data':order})
    return redirect(login)


def changepassword(request):
    if 'id' in request.session:
        if request.method == 'POST':
            a = request.POST.get('current_password')
            b = request.POST.get('new_password')
            c = request.POST.get('confirm_password')
            try:
                data = Register.objects.get(username=request.session['id'])
                if data.password == a:
                    if b == c:
                        Register.objects.filter(username=request.session['id']).update(password=b)
                        messages.success(request, 'Password Updated')
                        return redirect(profile)
                    else:
                        messages.error(request, 'Passwords Do not Match')
                        return redirect(profile)
                else:
                    messages.error(request, 'Password Incorrect')
                    return redirect(profile)
            except Exception:
                return redirect(profile)



def checkout_cart(request,total):
    user = Register.objects.get(username=request.session['id'])
    print(user,"User")
    pro=cart.objects.filter(user_details=user)
    print(pro)
    order_ids = []
    if request.method == 'POST':
        a = request.POST['name']
        c = request.POST['address']
        d = request.POST['city']
        e = request.POST['state']
        g = request.POST['pincode']
        h = request.POST['phone']
        print("a",a,c)
        for i in pro:
            cn = i.product_details
            cq = i.quantity
            ct = i.product_details.product_price * i.quantity
            v=deliverydetails(user_details=user, fullname=a, address=c, city=d, state=e, pincode=g, product_details_2=cn,quantity=cq,total_price=total,phone=h,payment_status='PAID')
            v.save()
            de=cart.objects.filter(product_details=cn)
            de.delete()
            value1 = v.pk
            order_ids.append(value1)
            Productdetails.objects.filter(pk=i.product_details.pk).update(product_stock=i.product_details.product_stock-cq)
        request.session['order_ids'] = order_ids

        return redirect(payment_cart,total)
    return render(request,'checkout_cart.html',{'user':user,'data':pro,'total':total})

def payment_cart(request, l):
    print("l",l)
    amount = int(l)* 100
    print("amount",amount)
    order_currency = 'INR'
    client = razorpay.Client(
        auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return render(request, "payment_cart.html",{'amount':amount})


def payment_success_cart(request):
    if 'id' in request.session:
        user = Register.objects.get(username=request.session['id'])
        order_ids = request.session.get('order_ids', [])
        print(order_ids)
        for i in order_ids:
            print("i",i)
            c = i
            b = 'PAID'
            deliverydetails.objects.filter(pk=c).update(payment_status=b)
        send_mail('Payment Successful',
                  f'Hey {user.username}, Your payment was successful and your ordered items has been successfully placed. \nWe are working on your order. \nOrder status will be updated soon.\n\nTHANK YOU.. \n\nBest regards',
                  'settings.EMAIL_HOST_USER', [user.email], fail_silently=False)

        send_mail('Out of Stock',
                  f' {user}, has placed a some new orders\nPlease review and update the order status',
                  'settings.EMAIL_HOST_USER', ['ayshathsalbana@gmail.com'], fail_silently=False)
        return render(request, "success_page.html")
    return redirect(login)


def low_stock(request):
    # if 'admin' in re.session:
        a = Productdetails.objects.all()
        l=[]
        for i in a:
            if i.product_stock is not None and i.product_stock < 5:
                l.append(i)
                # print(i.Stock)
        print("l",l)
        return render(request,'lowstock.html',{'item':l})


def admin_orders(request):
    if 'id' in request.session:
        order = deliverydetails.objects.all()
        return render(request, 'adminorderdetails.html',{'data':order})
    return redirect(adminhome)


def adminorderupdate(request,d):
    if 'id' in request.session:
        ord = deliverydetails.objects.get(pk=d)
        print(ord)
        if request.method == 'POST':
            a = request.POST.get('odsts')
            b = request.POST.get('inst')
            deliverydetails.objects.filter(pk=d).update(product_status=a, instruction=b)
            return redirect(admin_orders)
        return render(request,'adminorderupdate.html',{'data':ord})
    return redirect(login)
