from __future__ import unicode_literals

from django.db import models

# Create your models here.

class File(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    filename = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title   

class Person(models.Model):
    names = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=True, blank=True)
    dates = models.CharField(max_length=200, null=True, blank=True)
    information = models.TextField(null=True, blank=True)
    shortname =  models.CharField(max_length=50, null=True, blank=True)
    @property
    def name(self):
        return '{n} {s}'.format(n=self.names, s=self.surname)           
    def __str__(self):
        return '{n} {s}'.format(n=self.names, s=self.surname)    
    class Meta:
        ordering = ['surname']

class Instrument(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True) 
    def __str__(self):
        return self.name   

class Instrumentation(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True) 
    description = models.CharField(max_length=255, null=True, blank=True) 
    def __str__(self):
        return self.name

class Editor(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)  
	def __str__(self):
	   	return self.name

class Licensing(models.Model):
	licence = models.CharField(max_length=200, null=True, blank=True)
	url = models.CharField(max_length=100, null=True, blank=True) 
	short_name  = models.CharField(max_length=50, null=True, blank=True)
	def __str__(self):
		return self.short_name

class Piece(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    vdgs = models.CharField(max_length=20, null=True, blank=True)
    composer = models.ForeignKey(Person, null=True, blank=True)
    lyricist = models.ForeignKey(Person, null=True, blank=True, related_name='composed_piece')    
    instrument = models.ManyToManyField(Instrument, blank=True)
    parts = models.IntegerField()
    instrumentation = models.ManyToManyField(Instrumentation, blank=True)
    files = models.ManyToManyField(File, blank=True)
    shortname = models.CharField(max_length=50, null=True, blank=True)
    shortinst = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    lulu = models.CharField(max_length=200, null=True, blank=True)
    editor = models.ForeignKey(Editor, null=True, blank=True)
    source = models.ForeignKey(Editor, null=True, blank=True, related_name='transcribed')
    conversion = models.ForeignKey(Editor, null=True, blank=True, related_name='converted')
    licence = models.ForeignKey(Licensing, null=True, blank=True)
    def __str__(self):
        return self.title   
    class Meta:
        ordering = ['title']
