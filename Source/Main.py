from Window import Window
from Helpers import Loader

class Plistr:
    def __init__ (self, Filename):
        self.Filename = Filename
        self.Items = Loader.LoadFile (self.Filename)

        self.Window = Window (Filename)

    def Run (self):
        self.Window.Run (self.Items)
