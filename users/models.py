from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    first_name = models.CharField(
    	"First Name", 
    	max_length=50, 
    	blank=False, 
    	null=False,
    	error_messages={
			'required':'First name is required.'
		}
    )
    last_name = models.CharField(
    	"Last Name", 
    	max_length=50, 
		blank=False, 
		null=False,
		error_messages={
			'required':'Last name is required.'
		}
    )
    email = models.EmailField(
		"Email",
		max_length=100,
		unique=True,
		error_messages={
			'required':'Email is required.',
			'unique':'This email has already been registered.'
		}
	)
    birthday = models.DateField(
    	"Birthday", 
    	blank=False, 
    	null=False,
    	error_messages={
			'required':'Birthday is required.'
		}
    )
    random_number = models.IntegerField(
    	"Random Number",
    	blank=False, 
    	null=False,
    	error_messages={
			'required':'This number is required.'
		}
	)

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + ' ' + self.last_name