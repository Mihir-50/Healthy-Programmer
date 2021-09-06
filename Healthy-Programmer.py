#Healthy Programmer : Run this program when you are about to start your job which is at 9 A.M everyday.
import time
import datetime
from pygame import mixer

# Drinking water alarm after every 25 minutes
i=1
while i<=18:
    time.sleep(1500)  #1500 in second = 25 minute
    # Starting the mixer
    mixer.init()
    # Loading the song
    mixer.music.load("C:\\Users\\ASUS\\Downloads/water.mp3")
    # Setting the volume
    mixer.music.set_volume(1)
    # Start playing the song
    mixer.music.play()
    # infinite loop
    while True:
        print("Press 'Drank' to exit the program")
        input_to_stop = input(" ")
        if input_to_stop == 'Drank':
            # Stop the mixer
            mixer.music.stop()
            #Append Date and time after music stop in a log file
            with open("log.txt","a") as f:
                w=f.write(str([str(datetime.datetime.now())]) + " He Drank Water\n")
            break


#Eye exercise after every 30 minutes from the start of program

    time.sleep(300)  #300 in second = 5 minute
    # Starting the mixer
    mixer.init()
    # Loading the song
    mixer.music.load("C:\\Users\\ASUS\\Downloads/eye.mp3")
    # Setting the volume
    mixer.music.set_volume(1)
    # Start playing the song
    mixer.music.play()
    # infinite loop
    while True:
        print("Press 'EyeDone' to exit the program")
        input_toinput_to_stop = input(" ")
        if input_toinput_to_stop == 'EyeDone':
            # Stop the mixer
            mixer.music.stop()
            #Append Date and time afte music stop in a log file
            with open("log.txt","a") as f:
                w=f.write(str([str(datetime.datetime.now())]) + " Eye Exercise Done \n")
            break


#Physical Exercise after every 45 minutes from the start of program

    time.sleep(900)  # 900 in second = 15 minute
    # Starting the mixer
    mixer.init()
    # Loading the song
    mixer.music.load("C:\\Users\\ASUS\\Downloads/physical.mp3")
    # Setting the volume
    mixer.music.set_volume(1)
    # Start playing the song
    mixer.music.play()
    # infinite loop
    while True:
        print("Press 'ExDone' to exit the program")
        input_to_stop = input(" ")
        if input_to_stop == 'ExDone':
            # Stop the mixer
            mixer.music.stop()
            # Append Date and time afte music stop in a log file
            with open("log.txt", "a") as f:
                w = f.write(str([str(datetime.datetime.now())]) + " Physical Exercise Done \n")
            break

    i+=1