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
import json  # Add this import
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

            # 4. Parse items_json for invoice
            try:
                items = json.loads(order.items_json)
                formatted_items = []
                
                # Handle different possible formats of items_json
                if isinstance(items, dict):
                    # Handle dictionary format (key-value pairs)
                    for item_id, item_data in items.items():
                        if isinstance(item_data, list) and len(item_data) >= 3:
                            # Format: {item_id: [qty, name, price]}
                            formatted_items.append({
                                'name': item_data[1],
                                'quantity': item_data[0],
                                'price': float(item_data[2]),
                                'total': float(item_data[2]) * int(item_data[0])
                            })
                        elif isinstance(item_data, dict):
                            # Format: {item_id: {name: x, qty: y, price: z}}
                            formatted_items.append({
                                'name': item_data.get('name', 'Unknown Item'),
                                'quantity': item_data.get('qty', 1),
                                'price': float(item_data.get('price', 0)),
                                'total': float(item_data.get('price', 0)) * int(item_data.get('qty', 1))
                            })
                elif isinstance(items, list):
                    # Handle list format
                    for item in items:
                        if isinstance(item, dict):
                            formatted_items.append({
                                'name': item.get('name', 'Unknown Item'),
                                'quantity': item.get('qty', 1),
                                'price': float(item.get('price', 0)),
                                'total': float(item.get('price', 0)) * int(item.get('qty', 1))
                            })
            except (json.JSONDecodeError, ValueError, TypeError) as e:
                # If there's any error parsing the JSON, create a fallback item
                formatted_items = [{
                    'name': 'Order Items',
                    'quantity': 1,
                    'price': float(order.amount),
                    'total': float(order.amount)
                }]

            # 5. Render invoice
            return render(request, 'invoice.html', {
                'order': order,
                'items': formatted_items,
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


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to view your profile")
        return redirect('/authcart/login/')
    
    # Get all orders for the current user
    orders = Orders.objects.filter(email=request.user.email).order_by('-timestamp')
    
    context = {
        'orders': orders
    }
    
    return render(request, "profile.html", context)


def view_order(request, order_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to view order details")
        return redirect('/authcart/login/')
    
    try:
        # Get the order
        order = Orders.objects.get(order_id=order_id)
        
        # Verify that the order belongs to the current user
        if order.email != request.user.email:
            messages.warning(request, "You don't have permission to view this order")
            return redirect('/profile/')
        
        # Get order updates
        updates = OrderUpdate.objects.filter(order_id=order_id)
        
        # Parse items_json
        try:
            items = json.loads(order.items_json)
            formatted_items = []
            
            # Handle different JSON formats
            if isinstance(items, dict):
                for item_id, item_data in items.items():
                    if isinstance(item_data, list):
                        # Format: {item_id: [qty, name, price]}
                        formatted_items.append({
                            'name': item_data[1],
                            'quantity': item_data[0],
                            'price': float(item_data[2]),
                            'total': float(item_data[2]) * int(item_data[0])
                        })
                    elif isinstance(item_data, dict):
                        # Format: {item_id: {name: x, qty: y, price: z}}
                        formatted_items.append({
                            'name': item_data.get('name', 'Unknown Item'),
                            'quantity': item_data.get('qty', 1),
                            'price': float(item_data.get('price', 0)),
                            'total': float(item_data.get('price', 0)) * int(item_data.get('qty', 1))
                        })
            elif isinstance(items, list):
                # Handle list format
                for item in items:
                    formatted_items.append({
                        'name': item.get('name', 'Unknown Item'),
                        'quantity': item.get('qty', 1),
                        'price': float(item.get('price', 0)),
                        'total': float(item.get('price', 0)) * int(item.get('qty', 1))
                    })
        except Exception as e:
            formatted_items = []
            print(f"Error parsing items_json: {e}")
        
        context = {
            'order': order,
            'updates': updates,
            'items': formatted_items
        }
        
        return render(request, "order_detail.html", context)
    
    except Orders.DoesNotExist:
        messages.warning(request, "Order not found")
        return redirect('/profile/')