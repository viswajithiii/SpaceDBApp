from django.db import models

# Create your models here.

class Astronaut(models.Model):

    firstName = models.CharField(max_length=15)
    middleName = models.CharField(max_length=15,null=True)
    lastName = models.CharField(max_length=15)
    country = models.CharField(max_length=30)
    dob = models.DateField()

class Astronomer(models.Model):

    firstName = models.CharField(max_length=15)
    middleName = models.CharField(max_length=15,null=True)
    lastName = models.CharField(max_length=15)
    country = models.CharField(max_length=30)
    dob = models.DateField()

class Comet(models.Model):

    name = models.CharField(max_length=30)
    approachPeriod = models.FloatField()
    orbitalVelocity = models.FloatField()
    astronomer = models.ForeignKey('Astronomer')

class EducationAstronaut(models.Model):

    university = models.CharField(max_length=30)
    year = models.IntegerField()
    astronaut = models.ForeignKey('Astronaut')

class EducationAstronomer(models.Model):

    university = models.CharField(max_length=30)
    year = models.IntegerField()
    astronomer = models.ForeignKey('Astronomer')

class Galaxy(models.Model):

    name = models.CharField(max_length=30)
    galaxytype = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    distfromMilkyWay = models.FloatField()
    discoverer = models.ForeignKey('Astronomer')

class Moon(models.Model):

    name = models.CharField(max_length=30)
    radius = models.FloatField()
    waterPresent = models.BooleanField()
    mass = models.FloatField()
    density = models.FloatField()
    gravity = models.FloatField()
    rotationPeriod = models.FloatField()
    temperature = models.FloatField()
    planet = models.ForeignKey('Planet')
    revolutionPeriod = models.FloatField()
    discoverer = models.ForeignKey('Astronomer')

class Planet(models.Model):

    name = models.CharField(max_length=30)
    radius = models.FloatField()
    waterPresent = models.BooleanField()
    mass = models.FloatField()
    density = models.FloatField()
    gravity = models.FloatField()
    rotationPeriod = models.FloatField()
    temperature = models.FloatField()
    star = models.ForeignKey('Star')
    revolutionPeriod =  models.FloatField()
    planetSystem = models.CharField(max_length=30)
    discoverer = models.ForeignKey('Astronomer')

class Star(models.Model):

    name = models.CharField(max_length=30)
    colour = models.CharField(max_length=30)
    spectralclass = models.CharField(max_length=1)
    mass = models.FloatField()
    radius = models.FloatField()
    temperature = models.FloatField()
    galaxy = models.ForeignKey('Galaxy')
    discoverer = models.ForeignKey('Astronomer')
    secondaryStar = models.ForeignKey('self')

class SpaceFlight(models.Model):

    country = models.CharField(max_length=30)
    year = models.IntegerField()
    launchVehicle = models.CharField(max_length=30)
    satellite = models.ForeignKey('Satellite',null=True)
    moon = models.ForeignKey('Moon',null=True)
    leader = models.ForeignKey('Astronaut',related_name='Leader')
    nextFlight = models.ForeignKey('self')
    members = models.ManyToManyField('Astronaut')

class Satellite(models.Model):

    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    launchyear = models.IntegerField()
    revolutionPeriod = models.FloatField()
    satellitetype = models.CharField(max_length=30)
    launchVehicle = models.CharField(max_length=30)
    planet = models.ForeignKey('Planet',null=True)
    moon = models.ForeignKey('Moon',null=True)

class GasesInAtmosphere(models.Model):

    planet = models.ForeignKey('Planet')
    gas = models.CharField(max_length=30)

