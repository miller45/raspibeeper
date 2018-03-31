import RPi.GPIO as GPIO
import time

BuzzerPin = 11

# CL = [0, 131, 147, 165, 175, 196, 211, 248]  # Low C Note Frequency
# CM = [0, 262, 294, 330, 350, 393, 441, 495]  # Middle C Note Frequency
# CH = [0, 525, 589, 661, 700, 786, 882, 990]  # High C Note Frequency

CL = [0, 131, 147, 165, 175, 196, 220, 247]  # Low C Note Frequency
CM = [0, 262, 294, 330, 350, 392, 440, 494]  # Middle C Note Frequency
CH = [0, 523, 587, 659, 699, 784, 880, 988]  # High C Note Frequency
CV = [0, 1047, 1175, 1319, 1397, 1568, 1760, 1976]  # High C Note Frequency

jingle_1 = [CL[1], CL[2], CM[3], CM[4], CH[5], CH[6], CV[2]]

jingle_2 = [CV[4], CH[6], CH[5], CM[4], CM[3], CL[2], CL[1]]

song_1 = [CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6],  # Sound Notes 1
          CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
          CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
          CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5]]

beat_1 = [1, 1, 3, 1, 1, 3, 1, 1,  # Beats of song 1, 1 means 1/8 beats
          1, 1, 1, 1, 1, 1, 3, 1,
          1, 3, 1, 1, 1, 1, 1, 1,
          1, 2, 1, 1, 1, 1, 1, 1,
          1, 1, 3]

song_2 = [CM[1], CM[1], CM[1], CL[5], CM[3], CM[3], CM[3], CM[1],  # Sound Notes 2
          CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2],
          CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1],
          CM[3], CM[2], CL[5], CL[7], CM[2], CM[1]]

beat_2 = [1, 1, 2, 2, 1, 1, 2, 2,  # Beats of song 2, 1 means 1/8 beats
          1, 1, 2, 2, 1, 1, 3, 1,
          1, 2, 2, 1, 1, 2, 2, 1,
          1, 2, 2, 1, 1, 3]


def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(BuzzerPin, GPIO.OUT)  # Set pins' mode is output
    global Buzz  # Assign a global variable to replace GPIO.PWM
    Buzz = GPIO.PWM(BuzzerPin, 440)  # 440 is initial frequency.


def loop():
    while True:
        play_jingle1()
        time.sleep(1)  # Wait a second for next song.
        play_jingle2()
        time.sleep(1)


def play_jingle1():
    Buzz.start(50)  # Start BuzzerPin pin with 50% duty ration
    print('\n Playing jingle 1...')
    for i in range(1, len(jingle_1)):  # Play song 1
        Buzz.ChangeFrequency(jingle_1[i])  # Change the frequency along the song note
        time.sleep(0.2 if i == 1 else 0.1)  # delay a note for beat * 0.5s
    Buzz.stop()  # Stop the BuzzerPin


def play_jingle2():
    Buzz.start(50)  # Start BuzzerPin pin with 50% duty ration
    print('\n Playing jingle 2...')
    for i in range(1, len(jingle_2)):  # Play song 1
        Buzz.ChangeFrequency(jingle_2[i])  # Change the frequency along the song note
        time.sleep(0.2 if (i + 1) == len(jingle_2) else 0.1)  # delay a note for beat * 0.5s
    Buzz.stop()  # Stop the BuzzerPin


def play_song1():
    Buzz.start(50)  # Start BuzzerPin pin with 50% duty ration
    print('\n Playing song 1...')
    for i in range(1, len(song_1)):  # Play song 1
        Buzz.ChangeFrequency(song_1[i])  # Change the frequency along the song note
        time.sleep(float(beat_1[i]) * 0.4)  # delay a note for beat * 0.5s
    Buzz.stop()  # Stop the BuzzerPin


def play_song2():
    Buzz.start(50)  # Start BuzzerPin pin with 50% duty ration
    print('\n\n Playing song 2...')
    for i in range(1, len(song_2)):  # Play song 1
        Buzz.ChangeFrequency(song_2[i])  # Change the frequency along the song note
        time.sleep(beat_2[i] * 0.4)  # delay a note for beat * 0.5s
    Buzz.stop()  # Stop the BuzzerPin


def destroy():
    Buzz.stop()  # Stop the BuzzerPin
    GPIO.output(BuzzerPin, 0)  # Set BuzzerPin pin to High
    GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
        destroy()
