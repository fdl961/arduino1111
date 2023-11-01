import time
from fhict_cb_01.custom_telemetrix import CustomTelemetrix

board = CustomTelemetrix()

LED4_PIN = 4
LED5_PIN = 5

def setup():
    board.set_pin_mode_digital_output(LED4_PIN)
    board.set_pin_mode_digital_output(LED5_PIN)

def loop():
    # Turn on LED 4
    board.digital_write(LED4_PIN, 1)
    
    # Display the countdown timer on the display
    for countdown in range(10, 0, -1):
        board.displayShow(countdown)
        time.sleep(1)
    
    # Turn off LED 4 and turn on LED 5
    board.digital_write(LED4_PIN, 0)
    board.digital_write(LED5_PIN, 1)
    time.sleep(90)  # Keep LED 5 on for 10 seconds

if __name__ == "__main__":
    setup()
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        print('shutdown')
        board.shutdown()

