class chat:

    def __init__(self, chat_name, usernames = [], messages = []):
        self.chat_name = chat_name
        self.usernames = usernames
        self.messages = messages

    def send_message(self, message_name):
        self.messages.append(f"{message_name.user.username}: \n {message_name.message} \n ({message_name.send_time})")

    def show_chat(self):
        for i in self.messages:
            print(i)


class user(chat):

    def __init__(self, username, birthday, place_of_study, status):
        self.username = username
        self.birthday = birthday
        self.place_of_study = place_of_study
        self.status = status

    def __str__(self):
        return f'{self.username} |{self.status}| \n birthday - {self.birthday} \n place of study - {self.place_of_study}'


class Message(chat):

    def __init__(self, chat_name, user, to_username, send_time, message):
        super().__init__(chat_name)
        self.user = user
        self.send_time = send_time
        self.to_username = to_username
        self.message = message



Alex = user('Alex', '12.05', 'Itmo', 'Python')
Tom = user('Tom', '24.11', 'Itmo', 'c#')

newchat = chat('ChatWithAlex', (Alex, Tom))

m1 = Message(newchat, Tom, Alex, '12:22, 04.06.24', 'hello')
newchat.send_message(m1)

m2 = Message(newchat, Alex, Tom, '12:25 04.06.24', 'hello!')
newchat.send_message(m2)

newchat.show_chat()