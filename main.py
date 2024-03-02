from gpt import userDirection
import keyboard

print("Listening for recording....")


while True:
    try:
        if keyboard.is_pressed('v'):
            print("holding v")
            break
    except:
        break