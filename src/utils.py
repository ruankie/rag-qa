class Greetings():
    def __init__(self, greeting:str = "Hello World") -> None:
        self.greeting = greeting

    def get_greeting(self) -> None:
        return self.greeting
    
    def set_greeting(self, new_greeting:str) -> None:
        self.greeting = new_greeting