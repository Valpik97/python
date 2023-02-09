import gc
from abc import abstractmethod, ABC


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
    def follow(self, followed_username):
        pass


class Chat(IShowable, ISendable, ABC):

    def __init__(self, chat_name, usernames: list = None, messages: list = None) -> None:
        if usernames is None:
            usernames = []
        if messages is None:
            messages = []
        self.chat_name = chat_name
        self.usernames = usernames
        self.messages = messages

    def send_message(self, message_name) -> None:
        self.messages.append(f"{message_name.user.username}: \n {message_name.message} \n ({message_name.send_time})")

    def show(self) -> None:
        for i in self.messages:
            print(i)


class Message(Chat, ABC):

    def __init__(self, chat_name, user_, to_username, send_time: str, message: str) -> None:
        super().__init__(chat_name)
        self.user = user_
        self.send_time = send_time
        self.to_username = to_username
        self.message = message


class user(IShowable, IFollowable, ABC):

    def __init__(self, username: str, birthday: str, place_of_study: str, status: str, followers_amount: int = 0,
                 followers: list = None, following_amount: int = 0, following: list = None, friends: list = None,
                 friends_amount: int = 0) -> None:
        if friends is None:
            friends = []
        if followers is None:
            followers = []
        if following is None:
            following = []
        self.friends_amount = friends_amount
        self.followers = followers
        self.following = following
        self.friends = friends
        self.followers_amount = followers_amount
        self.following_amount = following_amount
        self.username = username
        self.birthday = birthday
        self.place_of_study = place_of_study
        self.status = status

    def follow(self, followed_username, followed_username_str: str) -> None:
        if followed_username not in self.following:
            if self.username in followed_username.following:
                self.friends.append(followed_username_str)
                self.friends_amount += 1
                followed_username.friends.append(f'{self.username}')
                followed_username.friends_amount += 1
                followed_username.following_amount -= 1
                followed_username.following.remove(f'{self.username}')
                self.followers.remove(followed_username_str)
                self.followers_amount -= 1
            else:
                self.following.append(followed_username_str)
                self.following_amount += 1
                followed_username.followers_amount += 1
                followed_username.followers.append(f'{self.username}')

    def show_follow(self) -> None:
        print(self.username, "'s followers:", sep='')
        for i in self.followers:
            print(i)
        print(self.username, "'s following:", sep='')
        for i in self.following:
            print(i)

    def show_friends(self) -> None:
        print(self.username, "'s friends:", sep='')
        for i in self.friends:
            print(i)

    def __str__(self) -> str:
        return f'{self.username} |{self.status}| \n' \
               f' {self.followers_amount} followers | {self.following_amount} following \n' \
               f' birthday - {self.birthday} \n' \
               f' place of study - {self.place_of_study}'


class Place_of_study(IShowable, ABC):

    def __init__(self, naming: str, students_amount: int = 0, students: list = None) -> None:
        if students is None:
            students = []
        self.naming = naming
        self.students_amount = students_amount
        self.students = students
        for i in gc.get_objects():
            if isinstance(i, user):
                self.students.append(f'{i.username}')
                self.students_amount += 1

    def __str__(self):
        return f"{self.naming}'s students: \n {self.students}"


Alex = user('Alex', '12.05', 'Itmo', 'Python')
Tom = user('Tom', '24.11', 'Itmo', 'c#')

newchat = Chat('ChatWithAlex', (Alex, Tom))

m1 = Message(newchat, Tom, Alex, '12:22, 04.06.24', 'hello')
newchat.send_message(m1)

m2 = Message(newchat, Alex, Tom, '12:25 04.06.24', 'hello!')
newchat.send_message(m2)

newchat.show()
print()
Alex.follow(Tom, 'Tom')
print()
Tom.show_follow()
Alex.show_follow()
print()
print()
Tom.follow(Alex, 'Alex')
Tom.show_follow()
Alex.show_follow()
print()
print()
Tom.show_friends()
Alex.show_friends()
print()
print()
Itmo = Place_of_study('Itmo')
print(Itmo)
