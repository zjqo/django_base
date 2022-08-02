from django.db import models

# Create your models here.
class bookinfo(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
    class Meta:
        db_table = 'bookinfo'
        verbose_name = 'suji'
    def __str__(self):
        return self.name
class peopleinfo(models.Model):
    GENDER_CHOICE = (
        (1,'male'),
        (2,'female')
    )
    name = models.CharField(max_length=10,unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE,default=1)
    description = models.CharField(max_length=100,null=True)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(bookinfo,on_delete=models.CASCADE)
    class Meta:
        db_table = 'peopleinfo'
        verbose_name = 'renwu'
    def __str__(self):
        return self.name