# from django.shortcuts import render,redirect
# from ecommerceapp.models import Contact,Product,OrderUpdate,Orders
# from django.contrib import messages
# from math import ceil
# from ecommerceapp import keys
# from django.conf import settings
# MERCHANT_KEY=keys.MK
# import json
# from django.views.decorators.csrf import  csrf_exempt
# from PayTm import Checksum

# # Create your views here.
# def index(request):
#     allProds = []
#     catprods = Product.objects.values('category','id')
#     # print(catprods)
#     cats = {item['category'] for item in catprods}
#     for cat in cats:
#         prod= Product.objects.filter(category=cat)
#         n=len(prod)
#         nSlides = n // 4 + ceil((n / 4) - (n // 4))
#         allProds.append([prod, range(1, nSlides), nSlides])

#     params= {'allProds':allProds}
#     return render(request, "index.html", params)

# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         desc = request.POST.get("desc")
#         pnumber = request.POST.get("pnumber")
#         myquery = Contact(name=name, email=email, desc=desc, phonenumeber=pnumber)
#         myquery.save()
#         messages.info(request, "We will get back to you soon..")
#         return render(request, "contact.html")
#     return render(request, "contact.html")

# def about(request):
#     return render(request, "about.html")



# def checkout(request):
#     if not request.user.is_authenticated:
#         messages.warning(request,"Login & Try Again")
#         return redirect('/auth/login')

#     if request.method=="POST":
#         items_json = request.POST.get('itemsJson', '')
#         name = request.POST.get('name', '')
#         amount = request.POST.get('amt')
#         email = request.POST.get('email', '')
#         address1 = request.POST.get('address1', '')
#         address2 = request.POST.get('address2','')
#         city = request.POST.get('city', '')
#         state = request.POST.get('state', '')
#         zip_code = request.POST.get('zip_code', '')
#         phone = request.POST.get('phone', '')
#         Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
#         print(amount)
#         Order.save()
#         update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
#         update.save()
#         thank = True
# # # PAYMENT INTEGRATION

#         id = Order.order_id
#         oid=str(id)+"ShopyCart"
#         param_dict = {

#             'MID':keys.MID,
#             'ORDER_ID': oid,
#             'TXN_AMOUNT': str(amount),
#             'CUST_ID': email,
#             'INDUSTRY_TYPE_ID': 'Retail',
#             'WEBSITE': 'WEBSTAGING',
#             'CHANNEL_ID': 'WEB',
#             'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

#         }
#         param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
#         return render(request, 'paytm.html', {'param_dict': param_dict})

#     return render(request, 'checkout.html')


# @csrf_exempt
# def handlerequest(request):
#     # paytm will send you post request here
#     form = request.POST
#     response_dict = {}
#     checksum = None
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]

#     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             print('order successful')
#             a=response_dict['ORDERID']
#             b=response_dict['TXNAMOUNT']
#             rid=a.replace("ShopyCart","")
           
#             print(rid)
#             filter2= Orders.objects.filter(order_id=rid)
#             print(filter2)
#             print(a,b)
#             for post1 in filter2:

#                 post1.oid=a
#                 post1.amountpaid=b
#                 post1.paymentstatus="PAID"
#                 post1.save()
#             print("run agede function")
#         else:
#             print('order was not successful because' + response_dict['RESPMSG'])
#     return render(request, 'paymentstatus.html', {'response': response_dict})







#--------------------------------------------------------------------------------------------------------------------

from django.shortcuts import render, redirect
from ecommerceapp.models import Contact, Product, OrderUpdate, Orders
from django.contrib import messages
from math import ceil
from ecommerceapp import keys
import razorpay
from django.views.decorators.csrf import csrf_exempt



# Razorpay Credentials
RAZORPAY_KEY_ID = keys.RAZORPAY_KEY_ID
RAZORPAY_KEY_SECRET = keys.RAZORPAY_KEY_SECRET
razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, "index.html", params)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        pnumber = request.POST.get("pnumber")
        myquery = Contact(name=name, email=email, desc=desc, phonenumeber=pnumber)
        myquery.save()
        messages.info(request, "We will get back to you soon..")
        return render(request, "contact.html")
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


# def checkout(request):
#     if not request.user.is_authenticated:
#         messages.warning(request, "Login & Try Again")
#         return redirect('/auth/login')

#     if request.method == "POST":
#         items_json = request.POST.get('itemsJson', '')
#         name = request.POST.get('name', '')
#         amount = float(request.POST.get('amt')) * 100  # Razorpay expects amount in paise
#         email = request.POST.get('email', '')
#         address1 = request.POST.get('address1', '')
#         address2 = request.POST.get('address2', '')
#         city = request.POST.get('city', '')
#         state = request.POST.get('state', '')
#         zip_code = request.POST.get('zip_code', '')
#         phone = request.POST.get('phone', '')

#         order = Orders(
#             items_json=items_json, name=name, amount=amount / 100, email=email,
#             address1=address1, address2=address2, city=city,
#             state=state, zip_code=zip_code, phone=phone
#         )
#         order.save()

#         # Create Razorpay Order
#         razorpay_order = razorpay_client.order.create({
#             "amount": int(amount),
#             "currency": "INR",
#             "payment_capture": "1"  # Auto capture
#         })

#         order.oid = razorpay_order["id"]
#         order.save()

#         context = {
#             "razorpay_order_id": razorpay_order["id"],
#             "razorpay_key": RAZORPAY_KEY_ID,
#             "amount": int(amount),
#             "name": name,
#             "email": email,
#             "phone": phone
#         }
#         return render(request, 'razorpay_payment.html', context)

#     return render(request, 'checkout.html')


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login & Try Again")
        return redirect('/authcart/login/')

    if request.method == "POST":
        amount = int(float(request.POST.get('amt')) * 100)  # Convert to paisa
        try:
            # Create Razorpay Order
            razorpay_order = razorpay_client.order.create({
                "amount": amount,
                "currency": "INR",
                "payment_capture": "1"
            })
        except razorpay.errors.BadRequestError as e:
            messages.error(request, "Payment failed. Please wait a moment and try again.")
            return redirect('/checkout/')  # Redirect instead of crashing

        # Create database entry
        order = Orders.objects.create(
            order_id=razorpay_order['id'],
            items_json=request.POST.get('itemsJson', ''),
            name=request.POST.get('name', ''),
            amount=amount / 100,
            email=request.POST.get('email', ''),
            address1=request.POST.get('address1', ''),
            address2=request.POST.get('address2', ''),
            city=request.POST.get('city', ''),
            state=request.POST.get('state', ''),
            zip_code=request.POST.get('zip_code', ''),
            phone=request.POST.get('phone', ''),
            paymentstatus="PENDING"
        )

        # Redirect to payment page
        return render(request, 'razorpay_payment.html', {
            "razorpay_order_id": razorpay_order['id'],
            "razorpay_key": RAZORPAY_KEY_ID,
            "amount": amount,
            "currency": "INR",
            "user": request.user
        })

    return render(request, 'checkout.html')


# @csrf_exempt
# def handlerequest(request):
#     if request.method == "POST":
#         data = request.POST
#         try:
#             razorpay_payment_id = data["razorpay_payment_id"]
#             razorpay_order_id = data["razorpay_order_id"]
#             razorpay_signature = data["razorpay_signature"]

#             params_dict = {
#                 "razorpay_order_id": razorpay_order_id,
#                 "razorpay_payment_id": razorpay_payment_id,
#                 "razorpay_signature": razorpay_signature
#             }

#             # Verify payment
#             result = razorpay_client.utility.verify_payment_signature(params_dict)
#             if result:
#                 order = Orders.objects.get(oid=razorpay_order_id)
#                 order.paymentstatus = "PAID"
#                 order.amountpaid = order.amount
#                 order.save()

#                 update = OrderUpdate(order_id=order.order_id, update_desc="Order has been placed and paid successfully")
#                 update.save()

#                 return render(request, 'paymentstatus.html', {'response': "Payment Successful!"})
#             else:
#                 return render(request, 'paymentstatus.html', {'response': "Payment Verification Failed!"})
#         except Exception as e:
#             return render(request, 'paymentstatus.html', {'response': f"Error: {str(e)}"})

#     return redirect("/")

@csrf_exempt
def handlerequest(request):
    if request.method == "POST":
        try:
            # 1. Get payment data with proper parameter order
            payment_data = {
                'razorpay_order_id': request.POST.get('razorpay_order_id'),
                'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
                'razorpay_signature': request.POST.get('razorpay_signature')
            }

            # 2. Verify payment signature
            razorpay_client.utility.verify_payment_signature(payment_data)

            # 3. Update order status
            order = Orders.objects.get(order_id=payment_data['razorpay_order_id'])
            order.oid = payment_data['razorpay_order_id']
            order.paymentstatus = "PAID"
            order.amountpaid = order.amount
            order.save()

            # 4. Create order update record
            OrderUpdate.objects.create(
                order_id=order.order_id,
                update_desc="Payment Successful! Order Placed"
            )

            # 5. Pass ALL required data to template
            return render(request, 'paymentstatus.html', {
                'response': 'PAYMENT SUCCESS',
                'order_id': order.order_id,
                'amount': order.amount,
                'transaction_id': payment_data['razorpay_payment_id']
            })

        except Orders.DoesNotExist:
            return render(request, 'paymentstatus.html', {
                'response': 'ORDER FAILURE',
                'error_message': f"Order {payment_data.get('razorpay_order_id')} not found in database"
            })
            
        except razorpay.errors.SignatureVerificationError:
            return render(request, 'paymentstatus.html', {
                'response': 'ORDER FAILURE',
                'error_message': "Payment signature verification failed"
            })
            
        except Exception as e:
            return render(request, 'paymentstatus.html', {
                'response': 'ORDER FAILURE',
                'error_message': f"Server error: {str(e)}"
            })

    return redirect('/')