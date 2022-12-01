
class User:
    users = {}

    def __init__(self, username, password, followed_by_amount = 0, followed_by = [], following_amount = 0,
                 following=[],birthday_date=None, place_of_study=None, status=None, marital_status=None,
                 about_user=None,friends_amount = 0, friends = [], wallet_amount = 0):
        self._username = username
        self._password = password
        self.followed_by = followed_by
        self.following = following
        self.wallet_amount = wallet_amount
        self.followed_by_amount = followed_by_amount
        self.following_amount = following_amount
        self.__class__.users[self._username] = self._password
        self.__birthday_date = birthday_date
        self.__place_of_study = place_of_study
        self.__status = status
        self.__marital_status = marital_status
        self.__about_user = about_user
        self.friends_amount = friends_amount
        self.friends = friends

    def follow(self, username_imp, password_imp, followed_username) -> None:
        if username_imp == self._username and password_imp == self._password:
            if followed_username not in self.following:
                self.following.append(f'{followed_username}')
                self.following_amount += 1
                followed_username.followed_by_amount += 1
                followed_username.followed_by.append(f'{self._username}')
        
    def add_friend(self, username_imp, password_imp, friend_add_username) -> None:
        if username_imp == self._username and password_imp == self._password:
            if friend_add_username not in self.friends:
                self.friends.append(f'{friend_add_username}')
                self.friends_amount += 1
                friend_add_username.friends_amount += 1
                friend_add_username.friends.append(f'{self._username}')

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
        return f'{self._username} \n' \
               f' {self.followed_by_amount} подписчиков | {self.following_amount} подписок \n'\
               f' день рождения: {self.birthday_date} \n место учёбы: ' \
               f'{self.place_of_study} \n статус: {self.status} \n семейное положение: {self.marital_status}' \
               f' \n обо мне: {self.about_user}'




vasya_1 = User('VASYA_1', '1223123')
misha = User('misha', '123321')
vasya_1.follow('VASYA_1', '1223123', misha)
vasya_1.birthday_date = 'VASYA_1', '1223123', '12.21'
vasya_1.place_of_study = 'VASYA_1', '1223123', 'Itmo'
vasya_1.status = 'VASYA_1', '1223123', 'ok'
vasya_1.marital_status = 'VASYA_1', '1223123', 'married'
vasya_1.about_user = 'VASYA_1', '1223123', "I'm programming on python"
print(vasya_1)
print(misha)
