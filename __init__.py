from mycroft import MycroftSkill, intent_file_handler
import subprocess

class Kineticinit(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('kineticinit.intent')
    def handle_kineticinit(self, message):
        self.speak_dialog('kineticinit')

    subprocess.call(["roscore"])

def create_skill():
    return Kineticinit()
