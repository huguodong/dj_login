from demo.models import TB_User


class MyCustomBackend:
    def authenticate(self, username=None, password=None):
        try:
            user = TB_User.objects.get(UserName=username)
        except TB_User.DoesNotExist:
            pass
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return TB_User.objects.get(pk=user_id)
        except TB_User.DoesNotExist:
            return None
