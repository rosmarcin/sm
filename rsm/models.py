from django.db import models
from django.contrib.auth.models import User


from datetime import datetime
from django.utils.translation import ugettext_lazy as _


# Roche Sales Models System
# Create your models here.


class UserProfile(models.Model):
    """ Profile is associated to physical person and application user. One physical person may have multiple users and multiple User Profiles 
    <TBC>
    
    """
 
 
    USER_PROFILE_TYPE = (
    (1, 'Busines Analyst'),
    (2, 'Data Scientist'),
    (3, 'Admin'),
    )
     

    USER_PROFILE_DOCUMENT_ID_TYPE = (
        (1, 'National ID'),
        (2, 'Passport'),
        (3, 'Driving License'),
        (4, 'Other'),
    )

    first_login_date = models.DateTimeField(null=True, blank=True, verbose_name=_("first_login_date"))
    first_name = models.CharField(max_length=30, null=False, blank=False, verbose_name=_("first_name"))
    last_name = models.CharField(max_length=30, null=False, blank=False, verbose_name=_("last_name"))
  
    roche_email = models.EmailField(unique=True, blank=True, null=True, verbose_name=_("personal_email"))   
    #user_profile_image = models.ImageField(upload_to=user_directory_path , default="fob/images/user1.jpg", blank=True, null=True, verbose_name=_("user_profile_image")) 
    application_user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='application_user', verbose_name=_("application_user"))   
    user_profile_type = models.PositiveSmallIntegerField(choices=USER_PROFILE_TYPE , null=False, blank=False, default=1, verbose_name=_("USER_PROFILE_TYPE"))  
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    # def application_user_names(self):
    #     return [i for i in self.application_user.all()]

    def __str__(self):
        return str(self.roche_email)
        
    class Meta:
        verbose_name ="User Profile"
        verbose_name_plural = "User Profiles"


class SalesModel(models.Model):
    """
    User's Model Collection 
    Each user can have multiple version of Sales Model

   
    """
    user=models.ForeignKey(User , related_name='user_model', on_delete=models.CASCADE)
    model_name=models.CharField(max_length=50, null=False, blank=False)
    version=models.CharField(max_length=20, null=False, blank=False)
    product_name=models.CharField(max_length=50, null=False, blank=False)
    indication=models.CharField(max_length=50, null=False, blank=False)
    description=models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.model_name) + str(self.version)

    class Meta:
#        unique_together=('tos_version', 'user',)
        verbose_name ='Sales Model'
        verbose_name_plural ='Sales Models'

    

class ParametersGroup(models.Model):
    """
    Eeach Model has multiple Parameter Groups (collection)  
    Each Parameter Group belongs to one Sales Model 

   
    """

    COUNTRY = (
    ('CH', 'CH - Swiss'),
    ('DE', 'DE - Germany'),
    ('IT', 'IT - Italia'),
    ('NL', 'NL - Netherlands'),
    ('PL', 'PL - Poland'),
    )

    sales_model=models.ForeignKey(SalesModel, related_name='sales_model',  on_delete=models.CASCADE)
    name=models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(choices=COUNTRY , max_length=2, null=False, blank=False, default=1, verbose_name="COUNTRY")  
    required=models.BooleanField(default = False)
    description=models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sales_model) + str(self.name)+ str(self.country)

    class Meta:
#        unique_together=('tos_version', 'user',)
        verbose_name ='Parameters Group'
        verbose_name_plural ='Parameters Groups'
        


class Parameter(models.Model):
    """
    Eeach Model has multiple Parameter  (collection)  
    Each Parameter belongs to one Sales Model 
   
    """

    sales_model=models.ForeignKey(SalesModel, related_name='parameter_sales_model', on_delete=models.CASCADE)
    name=models.CharField(max_length=50, null=False, blank=False)
    parameter_config = models.JSONField(null=False, blank=False)
    required=models.BooleanField(default = False)
    description=models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sales_model) + str(self.name)

    class Meta:
#        unique_together=('tos_version', 'user',)
        verbose_name ='Parameter'
        verbose_name_plural ='Parameters'
        
