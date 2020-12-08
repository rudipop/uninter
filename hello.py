class Hello:

    def __init__(self, name):
        
        self._name = name

    def gree(self):
        print('Hello! And Welcome, {name}!', format(name=self.name))
    
