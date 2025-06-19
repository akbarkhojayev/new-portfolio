from aiogram.dispatcher.filters.state import State, StatesGroup

class ContactForm(StatesGroup):
    name = State()
    email = State()
    subject = State()
    message = State()
