
class CAnimal:
    name="unname"
    def __init__(self,voice="hello"):
        self.voice=voice
    def __del__(self):
        pass
    def say(self):
        print self.voice

t=CAnimal()
t.say()
dog=CAnimal("wow")
dog.say()

class CAnimal:
    name="unname"
    def __init__(self,voice="hello"):
        self.voice=voice
    def say(self):
        print self.voice
    def run(self):
        pass

class CDog(CAnimal):
    def setvoice(self,voice):
        self.voice=voice
    def run(self):
        print "running"

bob=CDog()
bob.setvoice("My name is bob!")
bob.say()
bob.run()