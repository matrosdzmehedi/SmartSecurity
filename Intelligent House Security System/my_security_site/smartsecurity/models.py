from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save

# Create your models here.

class UserRegistration(models.Model):
    m_status = [('Married', 'Married'), ('Unmarried', 'Unmarried')]


    name=models.CharField( max_length=50,blank=False)
    flat_no=models.CharField( max_length=10,blank=False)
    phone_no = models.CharField(max_length=12)
    age=models.IntegerField(default=None)
    profession=models.CharField( max_length=50,blank=False)
    address=models.CharField( max_length=50,blank=False)
    slug=models.SlugField(unique=True)
    marig_status=models.CharField(max_length=20, choices=m_status)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users_data_details', kwargs={'slug': self.slug})



def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
	    instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_receiver, sender = UserRegistration)
