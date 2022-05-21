import time

def convert(seconds):
	hours = seconds // 3600
	seconds %= 3600
	mins = seconds // 60
	seconds %= 60
	return hours, mins, seconds

def timer(seconds):
	count = 0
	while count < seconds:
		hours, mins, secs = convert(count)
		timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
		print(timer, end='\r')
		time.sleep(1)
		count += 1

t = int(input('Quantos segundos para dormir: '))
timer(t)