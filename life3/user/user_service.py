from .models import LifeUser


# TODO: implement
class UserService:

    @staticmethod
    def is_valid_user(account_id: str):
        user = LifeUser.objects.filter(account_id=account_id, is_active=True)
        return True if user else False

    # TODO: consider using obj instead dict
    @staticmethod
    def update_user_profile(profile: dict):
        user = LifeUser.objects.get(account_id=profile['userId'], is_active=True)
        user.account_token = profile['accessToken']

    # TODO: consider using obj instead dict
    @staticmethod
    def create_user_profile(profile: dict):
        user = LifeUser()
        user.account_id = profile['userId']
        user.account_token = profile['accessToken']
        user.profile_name = profile['userName']
        user.profile_email = 'test@email.com'
        user.account_type = profile['type']
        user.save()
