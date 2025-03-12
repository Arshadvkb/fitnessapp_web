from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=20)

class Expert(models.Model):
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    image = models.FileField()
    phone = models.BigIntegerField()
    gender= models.CharField(max_length=7)
    email= models.CharField(max_length=20)
    pin= models.IntegerField()
    place= models.CharField(max_length=100)

class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=30)
    height=models.FloatField()
    weight=models.FloatField()
    goal=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    image=models.FileField()
class Trainer(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    pin = models.IntegerField()
    place = models.CharField(max_length=100)
    image = models.FileField()
    expertice=models.CharField(max_length=30)
    dob=models.DateField()
class Workallocation(models.Model):
    TRAINER=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    work= models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=15)

class Events(models.Model):
    eventtitle = models.CharField(max_length=20)
    eventdescription = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
    picture = models.FileField()
class Fees_Payment(models.Model):
    fees = models.BigIntegerField()
    date = models.DateField()
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    TRAINER = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    status = models.CharField(max_length=15)



class Notification(models.Model):
    notification=models.CharField(max_length=50)
    discription=models.CharField(max_length=150)
    start_date=models.DateField()
    end_date=models.DateField()

class Expert_Health_Tips(models.Model):
    EXPERT = models.ForeignKey(Expert,on_delete=models.CASCADE)
    tipstitle = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    date = models.DateField()
class Chat(models.Model):
    FROM=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='from_id')
    TO = models.ForeignKey(Login, on_delete=models.CASCADE,related_name='to_id')
    message=models.CharField(max_length=100)
    date=models.DateField()

class Complaint(models.Model):
    complaint = models.CharField(max_length=500)
    date = models.DateField()
    reply = models.CharField(max_length=500)
    USER = models.ForeignKey(User,on_delete=models.CASCADE)

class Batch_Allocation(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    TRAINER = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    from_time=models.TimeField()
    to_time=models.TimeField()

class Attendance(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=15)


class Online_Training(models.Model):
    video=models.FileField()
    TRAINER = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    video_name=models.TextField(max_length=100)
    description=models.TextField(max_length=500)

class Diet(models.Model):
    food=models.TextField(max_length=100)
    quantity=models.IntegerField()
    time=models.TimeField()

class Workout(models.Model):
  
    reps=models.IntegerField()
    set=models.IntegerField()
    weight=models.FloatField()
    name=models.TextField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)