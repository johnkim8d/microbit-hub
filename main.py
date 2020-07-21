def on_received_string(receivedString):
    basic.show_icon(IconNames.HAPPY)
    serial.write_line(receivedString)
    basic.clear_screen()
radio.on_received_string(on_received_string)

radio.set_group(1)

def on_forever():
    basic.show_icon(IconNames.SMALL_HEART)
    basic.pause(100)
    basic.clear_screen()
    basic.pause(5000)
basic.forever(on_forever)
