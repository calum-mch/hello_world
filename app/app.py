from google import search

# The Guru
class Guru():
    def __init__(self, name=""):
        self.name = name
        self.user = ''
        self.search_size = 20;
        
    def greeting(self, user=""):
        self.user = user
        return "Hello "+user+", I am "+self.name+" the Guru"
            
    def ask(self, question):
        if (self.user == ''):
            return "You lazy fool, greet me before asking such a question"
        elif (self.user == 'Shakeel'):
            return "You cannot afford my wisdom"
        else:
            results = []
            for url in search(question, stop=self.search_size):
                results.append(url)
            return results

