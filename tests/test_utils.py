from src.utils import Greetings

def test_greeting_init():
    gr = Greetings()
    assert isinstance(gr.greeting, str)

def test_get_default_greeting():
    gr = Greetings()
    default_greeting = gr.get_greeting()
    assert default_greeting == "Hello World"

def test_custom_greeting_init():
    custom_greeting = "Hello all"
    gr = Greetings(custom_greeting)
    assert gr.greeting == custom_greeting

def test_set_custom_greeting():
    gr = Greetings()
    custom_greeting = "Hello all"
    gr.set_greeting(custom_greeting)
    assert gr.greeting == custom_greeting