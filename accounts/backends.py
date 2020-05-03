from django.contrib.auth.models import User


class EmailAuth:
    '''Authenticate a user by exact match on email and password'''

    def authenticate(self, username=None, password=None):
        '''Get an instance of 'User' based off the email
        and verify pw. Username and password are equals to None
        by default'''

        try:
            '''try to get a user where email address is username on form'''
            user = User.objects.get(email=username)

            '''check password'''
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        '''Used by the Django authentication system
        to retrieve user instance'''

        try:
            '''PK is Primary Key used by Django and compare it to user_id'''
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
