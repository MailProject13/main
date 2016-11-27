#ver .02

class User():
     def __init__(self, Name=None, href=None):
        self.name=Name
        self.href=href
        self.friends = {None}
        self.picture = None
