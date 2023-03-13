import base64


from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import Account,Accounts,images,Image
from .forms import ImageForm




def sendexammails(request):
    if request.method=='POST':
        all=request.POST
        alldata=Accounts.objects.values_list('email')
        for i in alldata:
            a=i[0]
            subject = 'Dear student'
            message = all['emailcontent']
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [a]
            send_mail(subject, message, email_from,recipient_list)
    return render(request,'sendmails.html')

def image_upload_view(request,para):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        form.save()
        one=str(para)
        dat=one.encode('ascii')
        dat=base64.b64encode(dat)
        dat=dat.decode('ascii')
        return redirect('http://127.0.0.1:8000/account/'+str(dat))
        
    else:
        form = ImageForm()
        a=Accounts.objects.filter(id=para).values() 
        for i in a:
            id=i['id']
            name=i['name']
            email=i['email']
            roll_no=i['roll_no']
            department=i['department']
            one=str(id)
        dat=one.encode('ascii')
        dat=base64.b64encode(dat)
        dat=dat.decode('ascii')
        image=Image.objects.filter(title=id).values()
        iimage="images/venu1.jpg"
        for i in image:
            iimage=i['image']
        data={'Done':["index.html",'clubs','logout'],'data':{'name':name,'email':email,'roll_no':roll_no,'department':department},'para':'s/'+dat,'para1':'image_upload_view/{}'.format(id),'image':iimage,'form': form,'id':para}
    
    return render(request, 'homepage.html',data)
def homepage(request):
    data={'Done':["homepagemain.html",'#',"login"],'data':{'name':'name','email':'email','roll_no':'roll_no','department':'department'},'image':"images/venu1.jpg"}
    return render(request,'homepage.html',data)
def s(request,para):
    base64_bytes = para.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    string=sample_string
    string=int(string)
    a=Accounts.objects.filter(id=string).values() 
    for i in a:
        id=i['id']
        name=i['name']
        email=i['email']
        roll_no=i['roll_no']
        department=i['department']
    one=str(id)
    dat=one.encode('ascii')
    dat=base64.b64encode(dat)
    dat=dat.decode('ascii')
    image=Image.objects.filter(title=id).values()
    iimage="images/venu1.jpg"
    for i in image:
        iimage=i['image']
    data={'Done':["homepagemain.html",'club','logout'],'data':{'name':name,'email':email,'roll_no':roll_no,'department':department},'para':'s/'+dat,'para1':'image_upload_view/{}'.format(id),'image':iimage}
    return render(request,'homepage.html',data)
def clubs(request,para):
    base64_bytes = para.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    string=sample_string
    string=int(string)
    a=Accounts.objects.filter(id=string).values() 
    for i in a:
        id=i['id']
        name=i['name']
        email=i['email']
        roll_no=i['roll_no']
        department=i['department']
    one=str(id)
    dat=one.encode('ascii')
    dat=base64.b64encode(dat)
    dat=dat.decode('ascii')
    image=Image.objects.filter(title=id).values()
    iimage="images/venu1.jpg"

    for i in image:
        iimage=i['image']
    
    data={'Done':["clubs.html",'club','logout'],'data':{'name':name,'email':email,'roll_no':roll_no,'department':department},'para':'s/'+dat,'para1':'image_upload_view/{}'.format(id),'image':iimage}
    return render(request,'homepage.html',data)
def pythonclub(request):
    return render(request,'Python Club.html')
def codeingclub(request):
    return render(request,'Coding Club.html')
def debateclubs(request):
    return render(request,'debate club.html')
def graphicclubs(request):
    return render(request,'Graphic Club.html')
def ideaclubs(request):
    return render(request,'idea club.html')
def literacyclubs(request):
    return render(request,'Literacy Club.html')
def speakingclubs(request):
    return render(request,'Speaking Club.html')
def womenclubs(request):
    return render(request,'women .html')
def innerwheel(request):
    return render(request,'innerwheelclub.html')
def euphoria(request):
    return render(request,'euphoriaclub.html')
def project(request):
    return render(request,'projectclub.html')
def campusradio(request):
    return render(request,'Campus Radio.html')
def abouts(request,para):
    one=str(para)
    dat=one.encode('ascii')
    dat=base64.b64encode(dat)
    dat=dat.decode('ascii')
    data={'Done':["departments.html",'#',"logout"],'para':dat}
    return render(request,'about.html')
def about(request):
    return render(request,'about.html')
def departmentss(request,para):
    base64_bytes = para.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    string=sample_string
    string=int(string)
    a=Accounts.objects.filter(id=string).values() 
    for i in a:
        id=i['id']
        name=i['name']
        email=i['email']
        roll_no=i['roll_no']
        department=i['department']
    one=str(id)
    dat=one.encode('ascii')
    dat=base64.b64encode(dat)
    dat=dat.decode('ascii')
    image=Image.objects.filter(title=id).values()
    iimage="images/venu1.jpg"
    for i in image:
        iimage=i['image']
    data={'Done':["departments.html",'club','logout'],'data':{'name':name,'email':email,'roll_no':roll_no,'department':department},'para':'s/'+dat,'para1':'image_upload_view/{}'.format(id),'image':iimage}
    return render(request,'homepage.html',data)

def departments(request):
    data={'Done':["departments.html",'#',"login"],'data':{'name':'name','email':'email','roll_no':'roll_no','department':'department'},'image':"images/venu1.jpg"}
    return render(request,'homepage.html',data)
def computerscienceandengineering(request):
    return render(request,'cse.html')
def computerscienceandengineeringai(request):
    return render(request,'ai.html')
def computerscienceandengineeringds(request):
    return render(request,'cds.html')
def electricalandelectronicsengineering(request):
    return render(request,'eee.html')
def civilengineering(request):
    return render(request,'civil.html')
def mechanicalengineering(request):
    return render(request,'mech.html')
def electronicsandcommunicationsengineering(request):
    return render(request,'ece.html')
def humanitiesandbasicsciences(request):
    return render(request,'h and b.html')
def departmentofmanagementstudies(request):
    return render(request,'mbamca.html')
def cybersecrity(request):
    return render(request,'cybersecurity.html')
def login(request):
    if request.method=='POST':
        all=request.POST
        if 'name' and 'password' in all:
            name=all['name']
            password=all['password']
            alldata1=Accounts.objects.values_list('name')
            namelist=[]
            for i in alldata1:
                   namelist.append(i[0])
            alldata1=Accounts.objects.values_list('password')
            passwordlist=[]
            for i in alldata1:
                   passwordlist.append(i[0])
            if name in namelist and password in passwordlist:
                       allin=Accounts.objects.filter(name=name,password=password).values()
                       for dat in allin:
                           one=dat['id']
                           one=str(one)
                           dat=one.encode('ascii')
                           dat=base64.b64encode(dat)
                           dat=dat.decode('ascii')
                       return HttpResponseRedirect('/account/'+dat)
        data={'Done':["startforms.html",'#',"login"],'data':{'name':'name','email':'email','roll_no':'roll_no','department':'department'},'image':"images/venu1.jpg"}
        return render(request,'homepage.html',data)    
    data={'Done':["startforms.html",'#',"login"],'data':{'name':'name','email':'email','roll_no':'roll_no','department':'department'},'image':"images/venu1.jpg"}
    return render(request,'homepage.html',data)
def logout(request):
    data={'Done':["homepagemain.html",'#',"login"],'data':{'name':'name','email':'email','roll_no':'roll_no','department':'department'},'image':"images/venu1.jpg"}
    return render(request,'homepage.html',data)
def accounts(request,para):
        return HttpResponseRedirect('/account/'+para)    
def signup(request):
    if request.method=='POST':
        all=request.POST
        name=all['sendname'][:4]
        password=all['sendpassword'][:4]
        email=all['sendemail'][:4]
        if name and password and email =='Done':
            alldata=Accounts.objects.values_list('email')
            emaillist=[]
            for i in alldata:
                emaillist.append(i[0])
            if all['sendemail'][4:] not in emaillist:
                data='Done'
                entry = Accounts()
                entry.name=all['sendname'][4:]
                entry.password=all['sendpassword'][4:]
                entry.email=all['sendemail'][4:]
                entry.save()
                id=entry.id
                a=Accounts.objects.filter(id=id).values() 
                for i in a:
                    id=i['id']
                    name=i['name']
                    email=i['email']
                    roll_no=i['roll_no']
                    department=i['department']
                one=str(id)
                dat=one.encode('ascii')
                dat=base64.b64encode(dat)
                dat=dat.decode('ascii')
                data={'Done':["homepagemain.html",'club','logout'],'data':{'name':name,'email':email,'roll_no':roll_no,'department':department},'para':'s/'+dat,'image':"images/venu1.jpg"}        
                return render(request,'homepage.html',data)
            else:
                data="alredy exist"
                return HttpResponse("<div><center>"+data+"</center></div>")
        return render(request,'homepage.html',data)
    return render(request,'startforms.html')
class Otp():
    def __init__(self):
        self.otp1={}
    def otpsend(self,otp):
        self.otp1.update({'otp':otp})
    def otprecive(self):
        return self.otp1
Otp1=Otp()
def otpverify(request):
    if request.method=='POST':
        all=request.POST
        print(all)
        if 'otp' in all:
            if all['otp'] == str(Otp1.otprecive()['otp']):
                data='Done'
                return HttpResponse(data)
            else:
                data="None"
                return HttpResponse(data)
        else:
            try:
                a=all['email']
                b=len(a*743)
                print(all)
                Otp1.otpsend(b)
                subject = 'verification'
                message = 'Hi '+all['name'] +', thank you for registering in your code.'+str(b)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [all['email'] ]
                send_mail(subject, message, email_from,recipient_list)
                data="Done"
                return HttpResponse(data)
            except:
                data="None"
                print("kjfjk")
                return HttpResponse(data)
    return render(request,'startforms.html')
class Email():
    def _init_(self):
        self.Email1={}
    def Emailsend(self,Email):
        self.Email1.update({'Email':Email})
    def Emailrecive(self):
        return self.Email1
Email1=Email()
def forget(request):
    if request.method=='POST':
        all=request.POST
        print(all)
        data='Done'
        if 'forgetpassword' and 'forgetpasswordco' in all:
            password1=all['forgetpasswordco']
            email=all['email'][4:]
            print(email)
            try:
                alldata=Accounts.objects.get(email=email)
                alldata.password=password1
                alldata.save()
            except:
                return "no email exist"
            data={'Done':["homepagemain.html",'#',"login"]}
            return render(request,'homepage.html',data)
        elif 'otp' in all:
            if all['otp'] == str(Otp1.otprecive()['otp']):
                data='Done'
                return HttpResponse(data)
            else:
                data="None"
                return HttpResponse(data)  
        try:
            a=all['email']
            b=len(a*743)
            Otp1.otpsend(b)
            subject = 'forget password'
            message = 'Hi their your forword code .'+str(b)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [all['email'] ]
            send_mail(subject, message, email_from,recipient_list)
        except:
            data="not valid"
            print("kjfjk")
            return HttpResponse(data)
        return redirect('/')
    return render(request,'startforms.html')
def account(request,para):
    if request.method=='POST':
        x_forwarded_for = request.META
        print(x_forwarded_for)
        return render(request,'homepage.html')
    base64_bytes = para.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    string=sample_string
    string=int(string)
    a=Accounts.objects.filter(id=string).values() 
    for i in a:
        id=i['id']
        name=i['name']
        email=i['email']
        roll_no=i['roll_no']
        department=i['department']
    one=str(id)
    dat=one.encode('ascii')
    dat=base64.b64encode(dat)
    dat=dat.decode('ascii')
    image=Image.objects.filter(title=str(id)).values()
    iimage="images/venu1.jpg"
    for i in image:
        iimage=i['image']
        if iimage == None:
            iimage="images/venu1.jpg"
        print(iimage)
    
    data={'Done':["homepagemain.html",'club','logout'],'data':{'name':name,'email':email,'roll_no':roll_no,'department':department},'para':'s/'+dat,'para1':'image_upload_view/{}'.format(id),'image':iimage}
    return render(request,'homepage.html',data )
def departandroll(request,para):
    if request.method=='POST':
        all=request.POST
        base64_bytes = para.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        string=sample_string
        string=int(string)
        try:
            alldata=Accounts.objects.get(id=string)
            alldata.roll_no=all['roll_no']
            alldata.department=all['department']
            alldata.save()
        except:
                return "no email exist"
        a=Accounts.objects.filter(id=string).values() 
        for i in a:
            id=i['id']
            name=i['name']
            email=i['email']
            roll_no=i['roll_no']
            department=i['department']
        one=str(id)
        dat=one.encode('ascii')
        dat=base64.b64encode(dat)
        dat=dat.decode('ascii')
        image=Image.objects.filter(title=str(id)).values()
        iimage="images/venu1.jpg"
        for i in image:
            iimage=i['image']
            if iimage == None:
                iimage="images/venu1.jpg"
            print(iimage)
    data={'Done':["homepagemain.html",'club','logout'],'data':{'name':name,'email':email,'roll_no':roll_no,'department':department},'para':'s/'+dat,'para1':'image_upload_view/{}'.format(id),'image':iimage}
    return render(request,'homepage.html',data)