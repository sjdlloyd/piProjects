from time import sleep
import picamera
import main

service = main.main()
WAIT_TIME=2
with picamera.PiCamera() as camera:
	camera.resolution = (1024,768)
	for i, filename in enumerate(camera.capture_continuous('/home/pi/time-lapse/img{timestamp:%H-%M-%S-%f}.jpg')):
		main.upload(filename,i, service)
		sleep(WAIT_TIME)
