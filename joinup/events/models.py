from django.db import models
from django.utils import timezone
from slugify import slugify


class Tag(models.Model):
    name = models.CharField(max_length=63, unique=True, primary_key=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    members = models.ManyToManyField('auth.User')
    tags = models.ManyToManyField(Tag)
    name = models.CharField(max_length=5000)
    name_url = models.CharField(max_length=5000)
    text = models.TextField()

    def prepare_database_save(self, field):
        if field == 'name':
            self.name_url = slugify(self.name)
    #def save(self, force_insert=False, force_update=False, using=None,
    #         update_fields=None):
    #    self.name_url = slugify(self.name)
    #    super(Group, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name + ' (' +self.name_url+ ')'

class Event(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    organizers = models.ManyToManyField('auth.User')
    name = models.CharField(max_length=5000)
    name_url = models.CharField(max_length=5000)
    text = models.TextField()
    location = models.CharField(max_length=5000, blank=True, null=True)
    time_start = models.DateTimeField(blank=True, null=True)
    time_end   = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        #return self.title + ' | ' + ', '.join(
        # map(self.organizers.all(), lambda x: x.name))

        if self.location == None:
            location = ' @ -'
        else:
            location = ' @ ' + self.location
        return self.name + location

class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    date_time = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.author