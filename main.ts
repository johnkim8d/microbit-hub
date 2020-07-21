radio.onReceivedString(function (receivedString) {
    basic.showIcon(IconNames.Happy)
    serial.writeLine(receivedString)
    basic.clearScreen()
})
radio.setGroup(1)
basic.forever(function () {
    basic.showIcon(IconNames.SmallHeart)
    basic.pause(100)
    basic.clearScreen()
    basic.pause(5000)
})
