
class Guru():
    def __init__(self, name=""):
        self.name = name
        self.user = ''
        
    def greeting(self, user=""):
        self.user = user
        return "Hello "+user+", I am "+self.name+" the Guru"
            
    def ask(self, question):
        if (self.user == ''):
            return "You lazy fool, greet me before asking such a question"
        elif (self.user == 'Shakeel'):
            return "You cannot afford my wisdom"
        else:
            return "That is a good question, let me think about it"

