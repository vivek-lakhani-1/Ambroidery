from django.shortcuts import render
from .models import user_register
from .models import partymodel
from .models import challanin as cln
from .models import challandata
from django.shortcuts import redirect
import random
import string
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from twilio.rest import Client

def generate_invoice_number():
    now = datetime.now()
    return now.strftime("%Y%m%d%H%M%S")

def calculate_total_amount(items):
    total_amount = 0
    for item in items:
        total_amount += int(item['price']) * int(item['quantity'])
    return total_amount


def generate_invoice(customer_name, items):
    invoice_number = generate_invoice_number()
    total_amount = calculate_total_amount(items)
    filename = f"static/download/Invoice_{invoice_number}.pdf"
    
    doc = canvas.Canvas(filename, pagesize=letter)
    doc.setFont('Helvetica-Bold', 16)
    doc.drawString(1 * inch, 10.5 * inch, f"Customer: {customer_name}")
    doc.setFont('Helvetica', 12)
    doc.drawString(1 * inch, 10 * inch, f"GST : {customer_name}")
    doc.setFont('Helvetica-Bold', 12)
  
    doc.drawString(1 * inch, 9 * inch, "Item")
    doc.drawString(3 * inch, 9 * inch, "Price")
    doc.drawString(4.5 * inch, 9 * inch, "Quantity")
    doc.drawString(6 * inch, 9 * inch, "Total")

    y = 8.5 * inch
    for item in items:
        doc.setFont('Helvetica', 12)
        doc.drawString(1 * inch, y, item['name'])
        doc.drawString(3 * inch, y, str(item['price']))
        doc.drawString(4.5 * inch, y, str(item['quantity']))
        doc.drawString(6 * inch, y, str(item['price'] * item['quantity']))
        y -= 0.3 * inch
    doc.setFont('Helvetica-Bold', 12)
    doc.drawString(6 * inch, 1.5 * inch, f"Total amount: {total_amount}")
    doc.save()
    
    return filename
    # print(f"Invoice {invoice_number} generated successfully for {customer_name}. Total amount: {total_amount}")



def generate_custom_string():
    string_length = 8
    characters = string.ascii_letters + string.digits
    custom_string = ''.join(random.choice(characters) for i in range(string_length))
    return custom_string




def register(request):
    
    if(request.method == "POST"):
        us = user_register()
        us.first_name = request.POST['firstn']
        us.last_name = request.POST['lastn']
        us.firm = request.POST['firmn']
        us.pancard = request.POST['panno']
        us.username = request.POST['mobno']
        us.address = request.POST['address']
        us.password = request.POST['password']
        us.gst = request.POST['gstno']
        us.save()
        request.session['user'] = request.POST['mobno']
        return redirect('/')
    return render(request,'signup.html')


def login(request):
    
    if(request.method=="POST"):
            print("YES")
            data = user_register.objects.filter(username=request.POST['username'],password = request.POST['password']).values()
            data = dict(data[0])
            if(data == {}):
                return render(request,'login.html')
            else:
                request.session['user'] = request.POST['username']
                return redirect('/')
            
    
    else:
        return render(request,'login.html')


def challanin(request):
    if(request.method=="POST"):
        cn = cln()
        cn.to = "vivek"
        cn.from_to = request.POST['from']
        cn.Item_id = request.POST['iid']
        cn.item_name =request.POST['iiname']
        cn.price = request.POST['price']
        cn.date = request.POST['date']
        cn.save()
        
    data = cln.objects.filter(to="vivek").values()
    
    price = []
    item_id = []
    item_name = []
    from_ = []
    from__ = []
    for i in range(len(data)):

        d = dict(data[i])
        
        item_id.append(d['Item_id'])
        price.append(d['price'])
        item_name.append(d['item_name'])
        from_.append(d['Item_id']+"+"+d['from_to'])
        from__.append(d['from_to'])
    
    dd = zip(from__,item_id,item_name,price,from_)
    
    dd2 = []
    data = partymodel.objects.filter(username="vivek").values()
        
    for i in range(len(data)):
         d = dict(data[i])
         dd2.append(d['firmname'])
    frm = {
        'data':dd,
        'data2':dd2,
        'username': request.session.get('user')
    }
    
            
    return render(request,'challanin.html',frm)


def challanout(request):
    
    if(request.method=="POST"):
        data = challandata.objects.filter(challan_id=request.POST['select']).values()
        data = dict(data[0])
    
        pdfpath = data['invoice']
        frm = {
            'challanid':request.POST['select'],
            'pdf_no':pdfpath,
            'username': request.session.get('user')
        }
        

        


        return render(request,'challanout2.html',frm)
    
    data = challandata.objects.all().values()
    challanid=[]
    for i in range(len(data)):
        d = dict(data[i])
        challanid.append(d['challan_id'])
    
    frm ={
        'data':challanid,
        'username': request.session.get('user')
    }
    
    return render(request,'challanout.html',frm)



def party(request):
    if(request.method=="POST"):
        
        p = partymodel()
        p.username = "vivek"
        p.firmname = request.POST['firmname']
        p.GST_no = request.POST['gstno']
        p.address = request.POST['add']
        p.mobile_no = request.POST['number']
        p.save()
    
    data = partymodel.objects.filter(username="vivek").values()
    firm = []
    gst = []
    address = []
    mobile = []
    for i in range(len(data)):
        d = dict(data[i])
        firm.append(d['firmname'])
        gst.append(d['GST_no'])
        address.append(d['address'])
        mobile.append(d['mobile_no'])
    
    dd = zip(firm,gst,address,mobile)
    frm = {
        'data':dd
    }
    return render(request,'party.html',frm)


def action(request,id):
    partymodel.objects.filter(GST_no=id).delete()
    return redirect('/party')

def action2(request,id):
    id = id.split("+")
    id1 = id[0]
    id2 = id[1]

    cln.objects.filter(Item_id = id1,from_to = id2).delete()
    return redirect('/challanin')

def genchallan(request):
   
   
    if(request.method=="POST"):
        from__ = request.POST["from"]
        data = cln.objects.filter(from_to = from__).values()
        
        items = [
               
            ]
        print(data)
        price = 0
        for i in range(len(data)):
            dd = {'name':0,'price':0,'quantity':1}
            d = dict(data[i])
            dd['name'] = d['item_name']
            dd['price'] = d['price']
            price = price + int(d['price'])
            dd['quantity'] = 1
            items.append(dd)
        
        
        
        
        custom = generate_custom_string()
        pdf_name = generate_invoice(request.POST["from"], items)
        chn = challandata()
        chn.challan_id = custom
        chn.invoice = pdf_name
        chn.save()
        cln.objects.filter(from_to = from__).delete()
        frm = {
            'challanid' :custom,
            'pdf_no': pdf_name,
            'username': request.session.get('user')
            
        }
        
        number = partymodel.objects.filter(firmname = from__ ).values()[0]['mobile_no']
       
        account_sid = 'AC29870e967b494e1e53aa4dd19535b224'
        auth_token = '6a411246d97449c263900a90c4c7fb6f'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f'Hello Sir, Your invoice is generated you have to pay {price} and your challanid is {custom}',
            from_='+16318835851',
            to="+91"+number 
        )
                

    
    return render(request,"challanout2.html",frm)


def profile(request):
    
    
    
    if(request.method=="POST"):
        profile = user_register()
        profile.username = request.session.get('user')
        profile.firm = request.POST['first']
        profile.gst = request.POST['gst']
        profile.pancard = request.POST['pancard']
        profile.address = request.POST['address']
        profile.save()
        # return render(request,'profile.html')
   
    data = user_register.objects.filter(username=request.session.get('user')).values()[0]
    frm = {
            'firm' : data['firm'],
            'gst' : data['gst'],
            'pancard':data['pancard'],
            'address' : data['address'],
            'mobile' : data['username']
        }
    return render(request,'profile.html',frm)