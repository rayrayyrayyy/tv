# Ray Allessandra Pacis | BSCPE 1-5

# create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create two objects from Class TV
# create class named TV
class TV:

    def __init__(self): 
        # create instance variables
        self.channel = 0
        self.volume = 0
        self.power = False

    # define functions for tv
    # Tv power ON/OFf
    def open_tv(self):
        self.power = True
        print("TV is already ON.")
        
    def close_tv(self):
        self.power = False
        print("TV is OFF.")

    # Tv channel
    def tv_channel(self):
        return self.channel
    
    def set_channel(self, channel):
        self.channel = channel
        '''output message to terminal'''
        print("channel changed")

    # Tv volume
    def tv_volume(self):
        return self.volume
    
    def set_volume(self, volume):
        self.volume = volume
        '''output message to terminal'''
        print("volume set")