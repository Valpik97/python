import gc
from abc import abstractmethod

class IShowable:
    @abstractmethod
    def show(self):
        pass

class ISendable:
    @abstractmethod
    def send(self):
        pass

class IFollowable:
    @abstractmethod
    def follow(self):
        pass

class chat(IShowable, ISendable):

    def __init__(self, chat_name, usernames = [], messages = []):
        self.chat_name = chat_name
        self.usernames = usernames
        self.messages = messages

    def send_message(self, message_name):
        self.messages.append(f"{message_name.user.username}: \n {message_name.message} \n ({message_name.send_time})")

    def show(self):
        for i in self.messages:
            print(i)


class Message(chat):

    def __init__(self, chat_name, user, to_username, send_time, message):
        super().__init__(chat_name)
        self.user = user
        self.send_time = send_time
        self.to_username = to_username
        self.message = message


class user(IShowable, IFollowable):

    def __init__(self, username, birthday, place_of_study, status, followers_amount = 0, followers = [],
                 following_amount = 0, following=[]):
        self.followers = followers
        self.following = following
        self.followers_amount = followers_amount
        self.following_amount = following_amount
        self.username = username
        self.birthday = birthday
        self.place_of_study = place_of_study
        self.status = status


    def follow(self, followed_username) -> None:
        if followed_username not in self.following:
            self.following.append(f'{followed_username}')
            self.following_amount += 1
            followed_username.followers_amount += 1
            followed_username.followers.append(f'{self.username}')


    def show_follow(self):
        print(self.username, "'s followers:", sep='')
        for i in self.followers:
            print(i)
        print(self.username, "'s following:", sep='')
        for i in self.following:
            print(i)


    def __str__(self):
        return f'{self.username} |{self.status}| \n' \
               f' {self.followers_amount} followers | {self.following_amount} following \n' \
               f' birthday - {self.birthday} \n' \
               f' place of study - {self.place_of_study}'

class Place_of_study(user, IShowable):

    def __init__(self, naming, students_amount = 0, students = []):
        self.naming = naming
        self.students_amount = students_amount
        self.students = students
        for i in gc.get_objects():
            if isinstance(i, user):
                self.students.append(f'{i}')

    def __str__(self):
        for j in self.students:
            return f'{self.naming} \n students:{j}'




Alex = user('Alex', '12.05', 'Itmo', 'Python')
Tom = user('Tom', '24.11', 'Itmo', 'c#')

newchat = chat('ChatWithAlex', (Alex, Tom))

m1 = Message(newchat, Tom, Alex, '12:22, 04.06.24', 'hello')
newchat.send_message(m1)

m2 = Message(newchat, Alex, Tom, '12:25 04.06.24', 'hello!')
newchat.send_message(m2)

newchat.show()
print()

Alex.follow(Tom)
Tom.show()
Alex.show()

Itmo = Place_of_study('Itmo')
print(Itmo)
