class Human:
    def __init__(self, name):
        self.name = name
        self.head = self.Head()
    def display(self):
        print("Name:", self.name)
        self.head.talk()
        self.head.brain.think()
    class Head():

        def __init__(self):
            self.brain = self.Brain()
        def talk(self):
            print("Talking...")
        class Brain:

            def think(self):
                print("Thinking....")
h = Human("Durga")
h.display()
