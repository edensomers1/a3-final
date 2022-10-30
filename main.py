def on_pin_pressed_p0():
    radio.send_string("" + (Hungry))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    radio.send_string("" + (Happy))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    radio.send_string("" + (Assist))
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    radio.send_string("" + (Angry))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    if receivedString == Hungry:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.show_leds("""
            . # . # .
                        . . . . .
                        . # # # .
                        # . . . #
                        . # # # .
        """)
    else:
        if receivedString == Thirsty:
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
            basic.show_leds("""
                . . # . .
                                . # # # .
                                . # # # .
                                . # # # .
                                . # # # .
            """)
        if receivedString == Assist:
            for index in range(5):
                music.play_tone(262, music.beat(BeatFraction.WHOLE))
                basic.show_icon(IconNames.NO)
                basic.show_leds("""
                    . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                """)
        if receivedString == Happy:
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
            basic.show_icon(IconNames.HAPPY)
    if receivedString == Sad:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.show_icon(IconNames.SAD)
    if receivedString == Angry:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.show_icon(IconNames.ANGRY)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("" + (Sad))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    radio.send_string("" + (Thirsty))
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_gesture_shake():
    global Timer
    Timer = randint(3, 15)
    basic.show_leds("""
        . # . # .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . # . # .
                # . # . #
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . # . # .
                # . # . #
                . # . # .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . # . # .
                # . # . #
                . # . # .
                # . # . #
                . . . . .
    """)
    basic.show_leds("""
        . # . # .
                # . # . #
                . # . # .
                # . # . #
                . # . # .
    """)
    while Timer > 0:
        Timer += -1
        basic.pause(1000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Timer = 0
Angry = ""
Sad = ""
Happy = ""
Assist = ""
Thirsty = ""
Hungry = ""
Hungry = "Hungry"
Thirsty = "Thirsty"
Assist = "Assist"
Happy = "Happy"
Sad = "Sad"
Angry = "Angry"
radio.set_group(77)