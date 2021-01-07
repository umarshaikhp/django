from django.shortcuts import render
# i have created the views
# Create your views here.
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
from django.http import HttpResponse  
from mac import settings  
from django.core.mail import send_mail  

def mail(request): 
    print("pythonjava") 
    subject = "Greetings"  
    msg     = "Congratulations for your Order"  
    to      = "umarfala1234@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return render(request,"shop/tracker.html" )  

def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nslides = n // 4 + ceil((n / 4) - (n // 4))

    allProds = []
    catprods  = Product.objects.values('category', 'id')
    # print(catprods)
    cats = {item['category'] for item in catprods}
    # print(cats)

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        # print(prod)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nslides), nslides])



    # allprodes = [[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    params = {'allprods':allProds}

    # params = {'no_of_slides': nslides, 'range': range(1, nslides), 'product': products}
    return render(request, 'shop/index.html', params)
def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        # print('query',query,'category',item.category.lower())
        return True
    elif query in item.desc.upper() or query in item.product_name.upper() or query in item.category.upper(): 
        return True
    elif query in item.desc or query in item.product_name or query in item.category: 
        return True        
    else: 
        return False
    

def search(request):

    query = request.GET.get('search')
    print(query)
    # print(query)
    allProds = []
    # product.objects.value return the query set full dictionaries
    catprods  = Product.objects.values('category', 'id')
    print(catprods)
    cats = {item['category'] for item in catprods}

    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        print("welocme")
        print(prod)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) !=0:
            allProds.append([prod, range(1, nslides), nslides])
            break
    params = {'allprods':allProds, 'msg': ""}
    if len(prod) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}


    return render(request,'shop/search.html',params)


def about(request):
    return render(request, 'shop/about.html')



def contact(request):
    if request.method=="POST" :
        print(request)
        name = request.POST.get('name','')
        # default value blank we are given
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        print(name)

        contact = Contact(name=name, email=email, phone=phone ,desc=desc)
        contact.save()
        show = True
        return render(request,'shop/contact.html',{'show':show})

    return render(request,'shop/contact.html')


def tracker(request):
    if request.method=="POST" :
        orderId = request.POST.get('orderId','')
        # default value blank we are given
        email = request.POST.get('email','')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            print("hiii")
            print(len(order))
            if len(order)>0:        
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                    response = json.dumps({"status":"success", "updates":updates, "itemsJson":order[0].items_json} , default=str)
                def mail():
                    emails = Orders.objects.get(email = email)
                    desc   = OrderUpdate.objects.get(order_id = orderId)
                    subject = "Your Order Status"  
                    msg     =   desc.update_desc
                    to      = emails.email  
                    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])      
                    if(res == 1):  
                        msg = "Mail Sent Successfuly"  
                    else:  
                        msg = "Mail could not sent"  
                mail();  

                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitems"}')
        except Exception as e:
            print(e)
            return HttpResponse('{"status":"error"}')
                                               
    return render(request,'shop/tracker.html')





def productview(request,myid):
    # fetch the data using the id
    product = Product.objects.filter(id=myid)
    print(product);
    return render(request,'shop/prodView.html',{'product': product[0]})


def checkout(request):
    if request.method=="POST" :
        print(request)
        # json format in string
        items_Json = request.POST.get('itemsJson','')
        print(items_Json)
        name = request.POST.get('name','')
        # default value blank we are given
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + " " + request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip','')
        phone = request.POST.get('phone','')
        order = Orders(items_json=items_Json, name=name, email=email,address=address,city=city,state=state,zip_code=zip_code, phone=phone)

        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="This order has been placed")
        update.save()
        
        

        # print(name)
        thank = True
        id = order.order_id
        print(id);
        return render(request,'shop/checkout.html',{'thank':thank, 'id':id})

        
    return render(request,'shop/checkout.html')

