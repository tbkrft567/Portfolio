from django.db import models
from datetime import *
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['firstName']) < 2:
            errors['firstNameError'] = 'Your first name must be at least 2 characters'
        if len(postData['lastName']) < 2:
            errors['lastNameError'] = 'Your last name must be at least 2 characters'
        if len(postData['password']) < 8:        
            errors['pasUsersword'] = 'Your password must be at least 8 characters'
        if postData['password'] != postData['password_conf']:
            errors['passwordMatch'] = "The confirmed password doesn't match"

        emailValidator = re.compile(r'^[a-zA-z0-9._+-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not emailValidator.match(postData['email']):
            errors['emailError'] = 'Your email is not in the correct format'
        else:
            findEmail = User.objects.filter(email=postData['email'])
            if findEmail:
                errors['emailDuplicate'] = 'This email has already been used'

        return errors

    def quoteValidator(self, postData):
        errors = {}
        if len(postData['quoted_by']) < 2:
            errors['quoted_byError'] = 'The Quoted By must be at least 2 characters'
        if len(postData['quote_text']) < 10:
            errors['quote_textError'] = 'The Quote must be at least 10 characters'
        print('completed')

        return errors

class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Quote(models.Model):
    quote_text = models.TextField()
    quoted_by = models.CharField(max_length=45)
    favorited_by = models.ManyToManyField(User, related_name="quotes")
    creator = models.ForeignKey(User, related_name="quotesCreator")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

