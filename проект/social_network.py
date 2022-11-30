
class user():

    def __init__(self, username, password, follows_amount = 0, follows = None, followers_amount = 0, followers = None, wallet_amount = 0):
        self._username = username
        self._password = password
        self.description = description
        self.follows = follows
        self.followers = followers
        self.wallet_amount = wallet_amount
        self.follows_amount = follows_amount
        self.followers_amount = followers_amount


class description(user):

    def __init__(self, username, password, birthday_date = None, place_of_study = None, status = None, marital_status = None , about_user = None):
        super().__init__(username, password)
        self.__birthday_date = birthday_date
        self.__place_of_study = place_of_study
        self.__status = status
        self.__marital_status = marital_status
        self.__about_user = about_user

    @property
    def birthday_date(self):
        return self.__birthday_date
    @birthday_date.setter
    def birthday_date(self, username_imp_password_imp_birthday_date_imp):
        username_imp, password_imp, birthday_date_imp = username_imp_password_imp_birthday_date_imp
        if username_imp == self._username and password_imp == self._password:
            self.__birthday_date = birthday_date_imp


    @property
    def place_of_study(self):
        return self.__place_of_study
    @place_of_study.setter
    def place_of_study(self, username_imp_password_imp_place_of_study_imp):
        username_imp, password_imp, place_of_study_imp = username_imp_password_imp_place_of_study_imp
        if username_imp == self._username and password_imp == self._password:
            self.__place_of_study = place_of_study_imp


    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, username_imp_password_imp_status_imp):
        username_imp, password_imp, status_imp = username_imp_password_imp_status_imp
        if username_imp == self._username and password_imp == self._password:
            self.__status = status_imp


    @property
    def marital_status(self):
        return self.__marital_status
    @marital_status.setter
    def marital_status(self, username_imp_password_imp_marital_status_imp):
        username_imp, password_imp, marital_status_imp = username_imp_password_imp_marital_status_imp
        if username_imp == self._username and password_imp == self._password:
            self.__marital_status = marital_status_imp


    @property
    def about_user(self):
        return self.__about_user
    @about_user.setter
    def about_user(self, username_imp_password_imp_about_user_imp):
        username_imp, password_imp, about_user_imp = username_imp_password_imp_about_user_imp
        if username_imp == self._username and password_imp == self._password:
            self.__about_user = about_user_imp


    def __str__(self):
        return f'{self._username} \n день рождения: {self.birthday_date} \n место учёбы: {self.place_of_study} \n статус: {self.status} \n семейное положение: {self.marital_status} \n обо мне: {self.about_user}'



VASYA_1 = user('VASYA_1', '1223123')
VASYA_1_description = description('VASYA_1', '1223123')
VASYA_1_description.birthday_date = 'VASYA_1', '1223123', '12.21'
VASYA_1_description.place_of_study = 'VASYA_1', '1223123', 'Itmo'
VASYA_1_description.status = 'VASYA_1', '1223123', 'ok'
VASYA_1_description.marital_status = 'VASYA_1', '1223123', 'married'
VASYA_1_description.about_user = 'VASYA_1', '1223123', "I'm programming on python"
print(VASYA_1_description)
