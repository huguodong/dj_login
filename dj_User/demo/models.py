from django.db import models
import hashlib


# Create your models here.
class TB_User(models.Model):
    UID = models.BigIntegerField(primary_key=True)
    UserName = models.CharField(max_length=20)
    UserPwd = models.CharField(max_length=100)
    UserEmail = models.EmailField()
    UserState = models.BooleanField(default=1)
    UserRole = models.BigIntegerField(default=2)
    CreateTime = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)

    def is_authenticated(self):
        return True

    def hashed_password(self, password=None):
        if not password:
            return self.UserPwd
        else:
            return hashlib.md5(password).hexdigest()

    def check_password(self, password):
        if self.hashed_password(password) == self.UserPwd:
            return True
        return False


class TB_Role(models.Model):
    RoleID = models.BigIntegerField(primary_key=True)
    RoleName = models.CharField(max_length=20)
    RoleNote = models.CharField(max_length=100)


class TB_Per(models.Model):
    PID = models.BigIntegerField(primary_key=True)
    PName = models.CharField(max_length=20)
    PNote = models.CharField(max_length=100)


class TB_Role_Per(models.Model):
    RPID = models.BigIntegerField(primary_key=True)
    RoleID = models.BigIntegerField()
    PID = models.BigIntegerField()
    Note = models.CharField(max_length=100)
