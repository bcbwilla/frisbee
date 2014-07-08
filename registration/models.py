from django.db import models

class Player(models.Model):
    GENDER_CHOICES = (
        ('f', 'female'),
        ('m', 'male'),
    )

    SKILL_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    SHIRT_SIZE_CHOICES = (
        ('s', 'small'),
        ('m','medium'),
        ('l','large'),
    )

    POSITION_CHOICES = (
        ('ic', 'in cutter'),
        ('oc', 'out cutter'),
        ('sdh', 'short distance handler'),
        ('ldh', 'long distance handler'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=30)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)
    skill = models.IntegerField(choices=SKILL_CHOICES)
    wants_shirt = models.BooleanField()
    wants_frisbee = models.BooleanField()
#    buy_options = models.CharField(max_length=1,default=None)
    shirt_size = models.CharField(choices=SHIRT_SIZE_CHOICES,max_length=1)
    position = models.CharField(choices=POSITION_CHOICES,max_length=3)

    def __unicode__(self):
        return self.first_name + " " + self.last_name
