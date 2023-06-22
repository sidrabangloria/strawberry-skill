from mycroft import MycroftSkill, intent_file_handler


class Strawberry(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('strawberry.intent')
    def handle_strawberry(self, message):
        self.speak_dialog('strawberry')


def create_skill():
    return Strawberry()

