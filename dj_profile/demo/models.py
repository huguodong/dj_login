from dj_profile import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Car(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        permissions = (
            ('view_car', '查看车辆信息'),
        )


class Account(models.Model):
    SEX_CHOICES = ((1, u'男'),
                   (2, u'女'),)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.SmallIntegerField(u'性别', default=1, choices=SEX_CHOICES)
    birth = models.DateField(u'生日', blank=True, null=True)
    age = models.SmallIntegerField(u'年龄', blank=True, null=True)
    picture = models.ImageField(u'头像', blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'Account'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.pk:
            try:
                p = Account.objects.get(user=self.user)
                self.pk = p.pk
            except Account.DoesNotExist:
                pass
        super(Account, self).save()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Account()
        profile.user = instance
        profile.save()


post_save.connect(create_user_profile, sender=User)
