input.onPinPressed(TouchPin.P0, function () {
    radio.sendString("" + (Hungry))
})
input.onButtonPressed(Button.A, function () {
    radio.sendString("" + (Happy))
})
input.onPinPressed(TouchPin.P2, function () {
    radio.sendString("" + (Assist))
})
input.onButtonPressed(Button.AB, function () {
    radio.sendString("" + (Angry))
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == Hungry) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        basic.showLeds(`
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            . # # # .
            `)
    } else {
        if (receivedString == Thirsty) {
            music.playTone(262, music.beat(BeatFraction.Whole))
            basic.showLeds(`
                . . # . .
                . # # # .
                . # # # .
                . # # # .
                . # # # .
                `)
        }
        if (receivedString == Assist) {
            for (let index = 0; index < 5; index++) {
                music.playTone(262, music.beat(BeatFraction.Whole))
                basic.showIcon(IconNames.No)
                basic.showLeds(`
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    `)
            }
        }
        if (receivedString == Happy) {
            music.playTone(262, music.beat(BeatFraction.Whole))
            basic.showIcon(IconNames.Happy)
        }
    }
    if (receivedString == Sad) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        basic.showIcon(IconNames.Sad)
    }
    if (receivedString == Angry) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        basic.showIcon(IconNames.Angry)
    }
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("" + (Sad))
})
input.onPinPressed(TouchPin.P1, function () {
    radio.sendString("" + (Thirsty))
})
input.onGesture(Gesture.Shake, function () {
    Timer = randint(3, 15)
    basic.showLeds(`
        . # . # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # . # .
        # . # . #
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # . # .
        # . # . #
        . # . # .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        . . . . .
        `)
    basic.showLeds(`
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        `)
    while (Timer > 0) {
        Timer += -1
        basic.pause(1000)
    }
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    music.playTone(262, music.beat(BeatFraction.Whole))
})
let Timer = 0
let Angry = ""
let Sad = ""
let Happy = ""
let Assist = ""
let Thirsty = ""
let Hungry = ""
Hungry = "Hungry"
Thirsty = "Thirsty"
Assist = "Assist"
Happy = "Happy"
Sad = "Sad"
Angry = "Angry"
radio.setGroup(77)
