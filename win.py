from tkinter import Tk, Label
from threading import Thread
import cv2

def tkinter_win_window():
	# create and config window
	window = Tk()
	window.columnconfigure(0, weight=1)
	window.columnconfigure(1, weight=2)
	window.columnconfigure(2, weight=1)

	# create winning label and place it
	win_label = Label(window, font=("Courier New", 18), text="You Win!")
	win_label.grid(row=2, column=1, pady=40)

	window.mainloop()

# via gfg
def play_video_window():
	# Create a VideoCapture object and read from input file
	cap = cv2.VideoCapture('./assets/win.mp4')

	# Check if camera opened successfully
	if (cap.isOpened() == False):
		print("Error opening video file")

	# Read until video is completed
	while (cap.isOpened()):

		# Capture frame-by-frame
		ret, frame = cap.read()
		if ret == True:
			# Display the resulting frame
			cv2.imshow('Frame', frame)

			# Press Q on keyboard to exit
			if cv2.waitKey(25) & 0xFF == ord('q'):
				break

		# Break the loop
		else:
			break

	# When everything done, release
	# the video capture object
	cap.release()

	# Closes all the frames
	cv2.destroyAllWindows()

def win_screen():
	tk_task = Thread(target=tkinter_win_window)
	video_task = Thread(target=play_video_window)

	video_task.start()
	tk_task.start()

	video_task.join()
	tk_task.join()
