class user():

    def __init__(self, username, password, follows_amount = 0, follows = None, followers_amount = 0, followers = None, wallet_amount = 0):
        self.username = username
        self.password = password
        self.follows = follows
        self.followers = followers
        self.wallet_amount = wallet_amount
        self.follows_amount = follows_amount
        self.followers_amount = followers_amount

class description(user):

    def __init__(self, username, birthday_date = None, place_of_study = None, status = None, marital_status = None , about_user = None):
        super().__init__(username)
        self.birthday_date = birthday_date
        self.place_of_study = place_of_study
        self.status = status
        self.marital_status = marital_status
        self.about_user = about_user


VASYA = user('VASYA_1', '1223123')