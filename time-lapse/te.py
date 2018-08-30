from time import sleep
import picamera
import timer
import datetime
WAIT_TIME=60
start = datetime.time(20,30)
end = datetime.time(8,30)
with picamera.PiCamera() as camera:
    camera.resolution = (1024,768)
    for i, filename in enumerate(camera.capture_continuous('/home/pi/time-lapse/data/img{timestamp:%H-%M-%S-%f}.jpg')):
        timer.sleep_in_time_range(start, end)
        if i % 3:
            sleep(WAIT_TIME)
        else:
            sleep(WAIT_TIME/20)
