class User:
    def __init__(self, name, subscribers, is_followed_by):
        pass
        self.name = name
        self.subscribers = int(subscribers)
        is_followed_by: array = []

    def follow(self, user: User) -> None:
        if self.name not in user.is_followed_by:
            user.is_followed_by.append(f'{self.username}')
            user.subscribers += 1