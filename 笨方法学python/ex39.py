class song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_mi_a_song(self):
        for line in self.lyrics:
            print line

happy_somg=song(["Happy birthday to you",
                 "I don't wang to get sued",
                 "So,i will stop right there"])

bulls_on_parade=song(["They really around the family",
                      "With pockets of shells"])

happy_somg.sing_mi_a_song()
bulls_on_parade.sing_mi_a_song()
