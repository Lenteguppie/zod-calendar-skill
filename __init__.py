from mycroft import MycroftSkill, intent_file_handler


class ZodCalendar(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('calendar.zod.intent')
    def handle_calendar_zod(self, message):
        self.speak_dialog('calendar.zod')


def create_skill():
    return ZodCalendar()

