from mycroft import MycroftSkill, intent_file_handler
import requests


class ZodCalendar(MycroftSkill):
    def __init__(self):
        self.url="localhost:8000/calendar"
        self.email = self.settings.get("CalendarEmail")
        MycroftSkill.__init__(self)

    @intent_file_handler('today.calendar.zod.intent')
    def handle_calendar_zod(self, message):
        post_data = {'action': 'events_today', 'email':self.email}
        x = requests.post(self.url, data = post_data)
        events = self.today_appointments_constructor(x)
        self.speak(events)
        self.speak_dialog('calendar.zod')

    @intent_file_handler('insert.calendar.zod.intent')
    def handle_calendar_zod(self, message):
        self.speak_dialog('calendar.zod')

    def today_appointments_constructor(self, data):
        result = "For today you have the following appointments: "
        counter = 0
        for event in data:
            if counter == 0:
                result + f"First you have {event.summary}, from {event.start} until {event.end} at {event.location}."
            else:
                result + f"Then you have {event.summary}, from {event.start} until {event.end} at {event.locations}."              
            counter + 1
        return result
def create_skill():
    return ZodCalendar()

