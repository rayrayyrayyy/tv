# create test driver program
# import class
from Television import TV
# define function for tv 1
def television_1():
    channel = int(input("TV 1's channel is: "))
    volume = int(input("TV 1's volume is: "))
    tv_1 = TV()
    tv_1.open_tv()
    tv_1.set_channel(channel)
    tv_1.set_volume(volume)
    output_tv1 = "tv1's channel is " + str(tv_1.tv_channel()) + " and volume level is " + str(tv_1.tv_volume())
    final_tv1.config(text = output_tv1)
    
# define function for tv 2
def television_2():
    channel = int(input("TV 2's channel is: "))
    volume = int(input("TV 2's volume is: "))
    tv_2 = TV()
    tv_2.open_tv()
    tv_2.set_channel(channel)
    tv_2.set_volume(volume)
    output_tv2 = "tv2's channel is " + str(tv_2.tv_channel()) + " and volume level is " + str(tv_2.tv_volume())
    final_tv2.config(text = output_tv2)
    

# import module
from tkinter import *
main = Tk()
main.title("Test Driver")
main.geometry("500x200+800+350")
main.config(bg = "purple")

final_tv1 = Label(main, text='TV 1', bg = "purple", fg = "white", font = ('Times', 20), justify = CENTER)
final_tv1.place(x=10, y=50)

final_tv2 = Label(main, text='TV 2', bg = "purple", fg = "white", font = ('Times', 20), justify = CENTER)
final_tv2.place(x=10, y=90)

# call functions
television_1()
television_2()

mainloop() # end program