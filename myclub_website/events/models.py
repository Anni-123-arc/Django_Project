from django.db import models

# Create your models here.

class Venue(models.Model):
    name = models.CharField('Venue name', max_length=180)
    address = models.CharField(max_length=300)
    pin_code = models.CharField('Pin code',max_length=10)
    phone = models.CharField('Contact',max_length=10)
    web = models.URLField('web url')
    email_address = models.EmailField('Email')
    
    def __str__(self):
        return self.name
      

class MyClubUser(models.Model):
    first_name = models.CharField('user name' , max_length=180)
    last_name = models.CharField('user name' , max_length=180)
    email = models.EmailField('User Email')
    
    
    def __str__(self):
        return self.first_name  + " " + self.last_name  + " " +  self.email  

 
class Event(models.Model):
    name = models.CharField('Event name' , max_length=180)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue,blank=True,on_delete=models.CASCADE)
    manager =models.CharField(max_length=60)
    description =models.TextField(blank=True)
    attendees =models.ManyToManyField(MyClubUser)
    

    def __str__(self):
        return self.name  + ' on '+ str(self.event_date)+ " by "+self.manager  
