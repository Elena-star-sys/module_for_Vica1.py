import time
from os import replace


class User:

    def __init__(self, nickname, password, age):
        self.nickname = 'name'
        self.password = hash(password)
        self.age = int(age)


class Video:

    def __init__(self, title, duration, time_now, adult_mode):
        self.title = 'title'
        self.duration = duration  # int(time.time(duration))
        self.time_now = 0
        self.adult_mode = False

    def toggle_adult_mode(self):
        self.adult_mode = not self.adult_mode


class UrTube:

    def __init__(self,users, videos, current_user):
        self.users = {}
        self.videos = []


    def log_in(self, nickname, password):
        user =  self.users.get(nickname)
        password = self.users.get(hash(password))
        if user in self.users and password in self.log_in(password):
            replace(current_user, user)















