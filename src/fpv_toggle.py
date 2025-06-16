# fpv_toggle.py – GPIO Relay Control for FPV Cam

import RPi.GPIO as GPIO
import time

RELAY_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

def turn_on():
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    print("FPV Camera ON")

def turn_off():
    GPIO.output(RELAY_PIN, GPIO.LOW)
    print("FPV Camera OFF")

if __name__ == "__main__":
    try:
        while True:
            cmd = input("Enter ON or OFF (q to quit): ").strip().lower()
            if cmd == "on":
                turn_on()
            elif cmd == "off":
                turn_off()
            elif cmd == "q":
                break
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
