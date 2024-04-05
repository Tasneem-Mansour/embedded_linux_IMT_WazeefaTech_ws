import RPi.GPIO as GPIO
import serial
import time

# Serial port configuration
serial_port = '/dev/ttyAMA0'  # Adjust this according to your USB to TTL module
baud_rate = 9600

# LED pin
output_pin = 26  # GPIO pin for LED output

# Initialize serial port
ser = serial.Serial(
    port=serial_port,
    baudrate=baud_rate,
    timeout=0.1  # Adjust timeout as needed
)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(output_pin, GPIO.OUT)

#try:
while True:
    # Read data from serial port
    data = ser.readline().decode().strip()

    if data:
        # If data is received, turn on the LED
        GPIO.output(output_pin, GPIO.HIGH)
        print("Received data:", data)
    else:
        # If no data received, turn off the LED
        #GPIO.output(output_pin, GPIO.HIGH)
        GPIO.output(output_pin, GPIO.LOW)
    
    time.sleep(0.1)  # Add a small delay to avoid excessive CPU usage

#except KeyboardInterrupt:
 #   print("Program terminated by user")
#finally:
  #  GPIO.cleanup()
