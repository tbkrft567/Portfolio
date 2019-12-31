from django.db import models
# from datetime import *

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title'])*len(postData['network'])*len(postData['releaseDate']) == 0:
            errors['requiredFields'] = 'All Fields are Required'
        else:
            # if postData['releaseDate'] > datetime.today():
                # errors['futureDate'] = 'Date must be entered as past date'
            if len(postData['title']) < 2:
                errors['titleError'] = 'The title must be at least 2 characters'
            if len(postData['network']) < 3:
                errors['networkError'] = 'The network must be at least 3 characters'
            if len(postData['description'])>0:
                if len(postData['description']) < 10:
                    errors['descriptionError'] = 'The description must be at least 10 characters'
        return errors

    def duplicateTitle(self, postData, id):
        titleError = {}
        shows = Show.objects.all()
        for show in shows:
            if show.title == postData['title'] and show.id != id: 
                titleError['duplicate'] = 'The show title already exists in the database. Please provide a unique name. Select Go Back to see the list of Shows.'
            return titleError

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=10)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()