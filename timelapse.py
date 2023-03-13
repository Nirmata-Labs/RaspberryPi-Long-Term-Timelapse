# Created by @GitHub: RaccoonAI
# 2023-03
# V1.7

import time
from fractions import Fraction
import picamera
import datetime
from astral.sun import sun
from astral import LocationInfo

____________Edit your parameters here:___________

# Location information
city = LocationInfo("<ENTER YOUR LOCATION HERE")

# Enable debug mode for testing
debug_mode = True


# Create a camera object
camera = picamera.PiCamera()

# Set the camera resolution
camera.resolution = (2592, 1944)
camera.rotation = 180

________________________________________________

debug_counter_day = 0
debug_counter_night = 0

# Current year
year = datetime.datetime.now().year
month = datetime.datetime.now().month

# Get sunrise and sunset times for the month 
s = sun(city.observer, date=datetime.date(year, month, 1))
sunrise = s["sunrise"].strftime("%H")
sunset = s["sunset"].strftime("%H")

if debug_mode:
    print("Sunrise",sunrise,"Sunset",sunset,"Month",month) 

# Loop for the duration of the time-lapse
#start_time = time.time()
#while (time.time() - start_time) <= total_time:
#while True: 
   # Determine if it's daytime or nighttime
hour = time.localtime().tm_hour

is_daytime = int(sunrise) <= hour <= int(sunset)  # Assume day hours between 6am and 6pm
#is_daytime = False
# Adjust camera settings based on time of day
if is_daytime:

        camera.sensor_mode = 0
        camera.shutter_speed = 0
        camera.iso = 0
        camera.exposure_mode = 'auto'
        if debug_mode:
            print("\n")
            print("---Day Mode---")
            print(datetime.datetime.now())
            if debug_counter_day == 0:
                print("\n")
                print("SETTINGS:")
                print("Sensor Mode:",camera.sensor_mode)
                print("Shutter Speed:",camera.shutter_speed)
                print("ISO:", camera.iso)
                print("Exposure Mode:", camera.exposure_mode)
                print("\n")
                debug_counter_day = 1
else:

        camera.framerate=Fraction(1, 6) 
        camera.sensor_mode=0
        camera.shutter_speed = 6000000
        camera.iso = 800

        # Give the camera a good long time to set gains and measure AWB
        # (you may wish to use fixed AWB instead)
        time.sleep(30)
        camera.exposure_mode = 'off'

        if debug_mode:
            print("\n")
            print("---Night Mode---")
            print(datetime.datetime.now())
            if debug_counter_night == 0:
                print("\n")
                print("SETTINGS:")
                print("Framrate:",camera.framerate)
                print("Sensor Mode:",camera.sensor_mode)
                print("Shutter Speed:",camera.shutter_speed)
                print("ISO:", camera.iso)
                print("Exposure Mode:", camera.exposure_mode)
                print("\n")
                debug_counter_night = 1

filename = time.strftime("/home/pi/images/img%d-%m-%Y-%H.jpg", time.localtime())
picamera.PiCamera.CAPTURE_TIMEOUT = 60
camera.capture(filename)

if debug_mode:
       print("Safed image", filename)


# Close the camera
camera.close()
