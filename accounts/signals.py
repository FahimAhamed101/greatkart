from .models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.contrib.auth.models import User
from allauth.account.signals import user_logged_in

@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
   
    if created:
       
        
        
            
        
        instance.is_active = False
        UserProfile.objects.create(user=instance)
        




