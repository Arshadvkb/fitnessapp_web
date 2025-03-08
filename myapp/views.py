from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from myapp.models import *
from datetime import datetime


# Create your views here.
#--------------------------------------------------------------------------------------------------------------
                   #login
def login(request):
    return render(request,'index.html')


def loginpost(request):
    uname=request.POST["textfield"]
    password=request.POST["textfield2"]
    ob=Login.objects.filter(username=uname,password=password)
    if ob.exists():
        ob2 = Login.objects.get(username=uname, password=password)
        if ob2.type=="admin":
            return HttpResponse('''<script>alert("admin login");window.location='/admin_home'</script>''')
        elif ob2.type=="trainer":
            request.session['lid']=ob2.id
            return HttpResponse('''<script>alert("trainer login");window.location='/trainer_home'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid usr");window.location='/'</script>''')

    else:
        return HttpResponse('''<script>alert("does not exist");window.location='/'</script>''')



#--------------------------------------------------------------------------------------------------------------
                            #ADMIN

def admin_home(request):
    return render(request,'admin/index.html')

def admin_add_expert(request):
    return render(request,'admin/addexpert.html')



def admin_edit_trainer(request,id):
    request.session["id"]=id
    ob=Trainer.objects.get(id=id)
    return  render(request,'admin/edittrainer.html',{'data':ob,"d":str(ob.dob)})



def admin_add_expert_post(request):
    aname=request.POST["textfield"]
    password=request.POST["textfield2"]
    confirm_password=request.POST["textfield6"]
    mail=request.POST["textfield5"]
    phone=request.POST["textfield3"]
    place=request.POST["textfield4"]
    pin=request.POST["pin"]
    gender=request.POST["radiobutton"]
    picture=request.FILES['file']
    if password==confirm_password:
        ob = Login()
        ob.username = aname
        ob.password = confirm_password
        ob.type = 'expert'
        ob.save()
        obj=Expert()
        obj.LOGIN=ob
        obj.name=aname
        obj.email=mail
        obj.phone=phone
        obj.place=place
        obj.gender=gender
        obj.pin=pin
        fs = FileSystemStorage()
        fp = fs.save(picture.name, picture)
        obj.image = fp
        obj.save()
        return HttpResponse('''<script>alert("Added");window.location='/admin_view_expert'</script>''')
    else:
        return HttpResponse('''<script>alert("Password mismatch");window.location='/admin_view_expert'</script>''')




def admin_ad_trainer(request):
    return render(request,'admin/addtrainer.html')


def admin_ad_trainer_post(request):
    tname=request.POST["textfield"]
    password=request.POST["textfield2"]
    confirm_password=request.POST["textfield6"]
    mail=request.POST["textfield5"]
    phone=request.POST["textfield3"]
    dob=request.POST["textfield7"]
    place=request.POST["textfield4"]
    expertice=request.POST["textfield8"]
    gender=request.POST["radiobutton"]
    picture=request.FILES["img"]
    pin=request.POST["pin"]
    passw=Login()
    passw.username=tname
    passw.password=confirm_password
    passw.type='trainer'
    passw.save()
    if password==confirm_password:
        ob = Trainer()
        ob.name = tname
        ob.email = mail
        ob.phone = phone
        ob.dob = dob
        ob.pin = pin
        ob.place = place
        ob.expertice = expertice
        ob.gender = gender
        ob.LOGIN = passw

        fs = FileSystemStorage()
        fp = fs.save(picture.name, picture)
        ob.image = fp

        ob.save()
        return HttpResponse('''<script>alert("Added");window.location='/admin_view_trainer'</script>''')
    else:
        return HttpResponse('''<script>alert("invalid");window.location='/admin_ad_trainer'</script>''')





def admin_batch_allocation(request):

    return render(request,'admin/batchallocation.html', {"trainer":Trainer.objects.all(),"user":User.objects.all()})


def admin_batch_allocation_post(request):
    trainer=request.POST["select"]
    user=request.POST["select2"]
    fee=request.POST["textfield4"]
    from_time=request.POST["from"]
    to_time=request.POST["to"]

    obj=Batch_Allocation()
    obj.USER=User.objects.get(id=user)
    obj.TRAINER=Trainer.objects.get(id=trainer)
    obj.fee=fee
    obj.from_time=from_time
    obj.to_time=to_time
    obj.save()

    ob=Fees_Payment()
    ob.fees=fee
    ob.status='pending'
    ob.date=datetime.now().today()
    ob.USER=User.objects.get(id=user)
    ob.TRAINER=Trainer.objects.get(id=trainer)
    ob.save()
    return HttpResponse('''<script>alert('new batch added');window.location='/admin_batch_allocation'</script>''')


def admin_view_events(request):
    ob=Events.objects.all()
    return  render(request,'admin/Viewevents.html',{'data':ob})
def admin_events(request):
    return  render(request,'admin/events.html')

def admin_events_post(request):
    event_title=request.POST["textfield"]
    event_discription=request.POST["form1"]
    date=request.POST["textfield3"]
    time=request.POST["textfield4"]
    picture=request.FILES["file"]
    ob=Events()
    fs=FileSystemStorage()
    fp=fs.save(picture.name,picture)
    ob.picture=fp
    ob.eventtitle=event_title
    ob.eventdescription=event_discription
    ob.date=date
    ob.time=time
    ob.save()
    return HttpResponse('''<script>alert('Event added');window.location='/admin_view_events'</script>''')

def admin_auto_delete_event(request,id):
    events = Events(id=id)
    d=datetime.now()
    if(events.date==d):
        events.delete()


def admin_delete_event(request,id):
    events=Events(id=id)
    events.delete()
    return HttpResponse('''<script>alert('Event deleted');window.location='/admin_view_events'</script>''')

def admin_edit_events(request,id):
    request.session["eid"] = id
    events = Events.objects.get(id=id)
    t = str(events.time)
    return render(request, 'admin/edit_events.html',{"data":events,"d":str(events.date),'t':t})

def admin_edit_events_post(request):
    try:
        event_title = request.POST["textfield"]
        event_discription = request.POST["form1"]
        date = request.POST["textfield3"]
        time = request.POST["textfield4"]
        picture = request.FILES["file"]
        fs = FileSystemStorage()
        fp = fs.save(picture.name, picture)
        ob=Events.objects.get(id=request.session["eid"] )
        ob.picture = fp
        ob.eventtitle = event_title
        ob.eventdescription = event_discription
        ob.date = date
        ob.time = time
        ob.save()
        return HttpResponse('''<script>alert('Event edited successffuly');window.location='/admin_view_events'</script>''')
    except:
        event_title = request.POST["textfield"]
        event_discription = request.POST["form1"]
        date = request.POST["textfield3"]
        time = request.POST["textfield4"]

        ob = Events.objects.get(id=request.session["eid"])
        ob.eventtitle = event_title
        ob.eventdescription = event_discription
        ob.date = date
        ob.time = time
        ob.save()
        return HttpResponse( '''<script>alert('Event edited successffuly');window.location='/admin_view_events'</script>''')


def admin_view_expert(request):
    ob=Expert.objects.all()

    return render(request,'admin/viewexpert.html',{'data':ob})

def admin_view_expert_post(request):

    return render(request,'admin/viewexpert.html')


def admin_delete_expert(request,id):

    login=Login.objects.get(id=id)
    login.delete()
    return HttpResponse('''<script>alert('expert Deleted');window.location='/admin_view_expert'</script>''')


def admin_edit_expert(request,id):
    request.session["id"]=id
    data=Expert.objects.get(id=id)

    return render(request, 'admin/editexpert.html',{'data':data})

def admin_edit_expert_post(request):
    id = request.session['id']
    ename = request.POST["textfield"]
    mail = request.POST["textfield5"]
    phone = request.POST["textfield3"]
    place = request.POST["textfield4"]
    gender = request.POST["radiobutton"]
    pin = request.POST["pin"]

    ob = Expert.objects.get(id=id)
    ob.name = ename
    ob.email = mail
    ob.phone = phone
    ob.pin = pin
    ob.place = place
    ob.gender = gender

    if 'img' in request.FILES:
        picture = request.FILES["img"]
        fs = FileSystemStorage()
        fp = fs.save(picture.name, picture)
        ob.image = fp
        ob.save()
    ob.save()
    return HttpResponse('''<script>alert("edited successfuly");window.location='/admin_view_expert'</script>''')






def admin_view_trainer(request):
    ob=Trainer.objects.all()
    return render(request,'admin/viewtrainer.html',{'data':ob})

def delete_trainer(request,id):
    trainer = Trainer.objects.get(id=id)
    trainer.delete()
    ob=Login.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('Trainer Deleted');window.location='/admin_view_trainer'</script>''')



def admin_work_allocation(request,id):
    request.session['tid']=id
    ob=Trainer.objects.get(id=id)
    return render(request,'admin/workallocation.html')

def admin_work_allocation_post(request):
    work=request.POST['textfield']
    date=request.POST['textfield2']
    time=request.POST['textfield3']
    ob=Workallocation()
    ob.work=work
    ob.date=date
    ob.time=time
    ob.status="pending"
    ob.TRAINER=Trainer.objects.get(id=request.session['tid'])
    ob.save()
    return HttpResponse('''<script>alert('work allocated');window.location='/admin_view_trainer'</script>''')


def admin_edit_trainer_post(request):
    id = request.session['id']
    tname = request.POST["textfield"]
    mail = request.POST["textfield5"]
    phone = request.POST["textfield3"]
    dob = request.POST["textfield7"]
    place = request.POST["textfield4"]
    expertice = request.POST["textfield8"]
    gender = request.POST["radiobutton"]
    pin = request.POST["pin"]

    ob = Trainer.objects.get(id=id)
    ob.name = tname
    ob.email = mail
    ob.phone = phone
    ob.dob = dob
    ob.pin = pin
    ob.place = place
    ob.expertice = expertice
    ob.gender = gender

    if 'img' in request.FILES:
        picture = request.FILES["img"]
        fs = FileSystemStorage()
        fp = fs.save(picture.name, picture)
        ob.image = fp
        ob.save()
    ob.save()

    return HttpResponse('''<script>alert("edited successfuly");window.location='/admin_view_trainer'</script>''')


def admin_view_user(req):
    ob=User.objects.all()
    return render(req,"admin/view_user.html",{"data":ob})

def Admin_fee_pending(req):
    a =Fees_Payment.objects.filter(status='pending')
    return render(req,'admin/fees.html',{'data':a})
















#-----------------------------------------------------------------------------------------------------------
                                 #TRAINER


def trainer_home(request):
    obj = Trainer.objects.filter(LOGIN_id=request.session['lid']).first()  # Get the first result

    if obj:  # Ensure that a trainer object was found
        request.session['t'] = obj.name
    else:
        # Handle case where no trainer was found (optional)
        request.session['t'] = "Trainer not found"
    return render(request,'trainer/index.html',{"data":obj})

def trainer_view_video(req):
    a=Online_Training.objects.filter(TRAINER__LOGIN_id=req.session["lid"])
    return render(req,"trainer/trainer_view_video.html",{"ob":a})


def Admin_view_work_status(req):
    obj=Workallocation.objects.all()
    return render(req,"admin/Admin_view_work_status.html",{"data":obj})


def Trainer_view_accepted_work(req):
    obj=Workallocation.objects.filter(status="accepted",TRAINER__LOGIN__id=req.session["lid"])
    return  render(req,'trainer/accepted_work.html',{"data":obj})



def trainer_online_training_video(request):
    return render(request,'trainer/onlinetrainingvideo.html')

def trainer_view_attendance(request):
    return render(request,'trainer/viewattandance.html')

def trainer_view_times_schedule(request):
    time=Batch_Allocation.objects.filter(TRAINER__LOGIN__id=request.session['lid'])
    return render(request,'trainer/viewtimeschedule.html',{"data":time})


def Triner_View_Attandance(req):
    obj=Attendance.objects.all()

    return render(req,"trainer/trainer_view_attandance.html",{"data":obj})


def Trainer_Edit_video(req,id):
    req.session['id']=id
    obj = Online_Training.objects.get(id=id)
    return render(req,"trainer/edit_video.html",{"data":obj})



def Trainer_Manage_work(req):
    obj=Workallocation.objects.filter(TRAINER__LOGIN__id=req.session["lid"],status='pending')
    print(obj)
    return render(req,"trainer/manage_allocated_work.html",{"data":obj})


def trainer_online_training_video_post(req):
    video_name=req.POST["textfield"]
    description=req.POST["textarea"]
    video=req.FILES['file']
    fs=FileSystemStorage()
    fp=fs.save(video.name,video)
    obj=Online_Training()
    obj.TRAINER=Trainer.objects.get(LOGIN_id=req.session['lid'])
    obj.video=fp
    obj.video_name=video_name
    obj.description=description
    obj.save()
    return HttpResponse('''<script>alert('new video added');window.location='/trainer_view_video'</script>''')


def Trainer_Delete_video(req,id):
    obj=Online_Training.objects.get(id=id)
    obj.delete()
    return HttpResponse('''<script>alert('video deleted');window.location='/trainer_view_video'</script>''')


def Trainer_Edit_video_Post(req):
    name=req.POST["textfield"]
    desc=req.POST["textarea"]



    obj=Online_Training.objects.get(id=  req.session['id'])
    if 'file' in req.FILES:
        video = req.FILES['file']
        fs = FileSystemStorage()
        fp = fs.save(video.name, video)
        obj.video=fp
    obj.video_name=name
    obj.description=desc
    obj.TRAINER=Trainer.objects.get(LOGIN__id=req.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert('video edited successfuly');window.location='/trainer_view_video'</script>''')

def Trainer_accept_Work(req,id):
    obj = Workallocation.objects.filter(id=id).update(status='accepted')

    return HttpResponse('''<script>alert('accepted ');window.location='/Trainer_view_accepted_work'</script>''')


def Trainer_reject_Work(req,id):
    obj = Workallocation.objects.filter(id=id).update(status='rejected')

    return HttpResponse('''<script>alert('Rejected ');window.location='/Trainer_Manage_work'</script>''')

def Trainer_completed_work(req,id):
    obj = Workallocation.objects.filter(id=id).update(status='completed')

    return HttpResponse('''<script>window.location='/Trainer_view_accepted_work'</script>''')







# ====================================================================================================================================================

                                                #  FLUTTER
                                                 



#=================================================================================================================
                                                # login





def androiod_login_POST(request):
    print(request.POST,'lllllllllllllllllll')
    username=request.POST['username']
    password=request.POST['password']
    try:
        ob=Login.objects.get(username=username,password=password)
        if ob.type=="user":
            print('OKKKKkkkkkkkkkkkkk')
            return JsonResponse({'status':'ok', 'lid':str(ob.id), 'type':ob.type})
        elif ob.type=="expert":
            return JsonResponse({'status':'ok', 'lid':str(ob.id), 'type':ob.type})
    
        else:
            return JsonResponse({'status':'invalid'})
        
    except:
        return JsonResponse({'status':'invalid'})
# ========================================================================================================
                                                # user

def user_viewvideo(request):
    ob = Online_Training.objects.all()
    l = []
    for i in ob:
        l.append({
            'id':i.id,
            'TRAINER':i.TRAINER.name,
            'video':str(i.video),
            'video_name':i.video_name,
            'description':i.description,
        })
    return JsonResponse({'status':'ok','data':l})


def user_register(request):
    print(request.POST)
    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']
    place=request.POST['place'] 
    gender=request.POST['gender']
    dob=request.POST['dob']
    goal=request.POST['goal']
    height=request.POST['height']
    weight=request.POST['weight']
    description=request.POST['description']
    password=request.POST['password']   
    confirm_password=request.POST['confirm_password']
    image=request.FILES['image']
    fs=FileSystemStorage()
    path=fs.save(image.name,image)
    if password==confirm_password:
        ob=Login()
        ob.username=name
        ob.password=confirm_password
        ob.type='user'
        ob.save()
        obj=User()
        obj.LOGIN=ob
        obj.name=name
        obj.phone=phone
        obj.email=email
        obj.place=place
        obj.image=path
        obj.gender=gender
        obj.goal=goal
        obj.dob=dob
        obj.height=height
        obj.weight=weight
        obj.description=description
        obj.save()
        return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status':'invalid'})
    

import json

def user_view_time(req):
 
    data = json.loads(req.body)
    uid = data.get('lid')  # Access 'lid' from the parsed JSON

    if not uid:
        return JsonResponse({"status": "error", "message": "LID is missing"}, status=400)

    obj = Batch_Allocation.objects.filter(USER__LOGIN_id=uid)
    a = []

    # Prepare the response data
    for i in obj:
        a.append({
            'id': i.id,
            'TRAINER': i.TRAINER.name,
            'from_time': str(i.from_time),
            'to_time': str(i.to_time),
        })
    

    return JsonResponse({"status": "ok", "data": a})
  


def user_home(req):

       data = json.loads(req.body)
       uid = data.get('lid')  # Access 'lid' from the parsed JSON

       if not uid:
        return JsonResponse({"status": "error", "message": "LID is missing"}, status=400)
       obj = User.objects.filter(USER__LOGIN_id=uid)
       a = []
       for i in obj:
        a.append({
            'id': i.id,
            'name': i.name,
            'phone': i.phone,
            'email': i.email,
            'place': i.place,
            'image': str(i.image),
        })
        return JsonResponse({"status": "ok", "data": a})
       

#  =============================================================================================================================================================      
#                                             # expert
def expert_helth_tips(request):
        print(request.POST)
        title=request.POST['tip_title']
        lid=request.POST['lid']
        description=request.POST['tip_description']
        obj=Expert_Health_Tips()
        obj.EXPERT=Expert.objects.filter(LOGIN__id=lid).first()
        obj.tipstitle=title
        obj.description=description
        obj.date=datetime.now().today()
        obj.save() 
        return JsonResponse({'status':'ok'})

       