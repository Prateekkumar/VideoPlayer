import os
import urllib
import cv
import sys
import cv2

"""
The following program will take the url as input. Separate the file name of the video from the url
and check if the file is present in the current memory location or not. If the same file is present
it will indicate its presence. If the file is not present it will download the file and play it.

urrlib: to download the video file.
cv: For playing the video.
cv2: Including this library to implement full screen display.
"""

#NOTE Configuration of FFMPEG and OpenCV  is required. 
#NOTE Assuming that the given code is execute from the internal memory location.
#NOTE Assuming the URL is of the form <initial part of the url/><filename>.<format>


sys.path.append('/opt/ros/hydro/lib/python2.7/dist-packages')

def myVideo(url):
	flag = 0  #flag for checking if the file in present in the memory.
        search_folder = "." 
        videoFile = url.split('/')[-1].split('#')[0].split('?')[0] #stripping the name of the file.

        for root, dirs, files in os.walk(search_folder): # using the os.walk module to find the files.
                for name in files:
                        """Checking the videofile in the current directory and the sub-directories"""
                        if videoFile == os.path.join(name):  #checking if the file is already present in the internal memory.(Traverse through subdirectories as well)
                        	flag += 1
				print "The file is already present in the internal memory"
                                return -1  # Returning the confirmation that the file is present.

        if flag == 0: # dowiloding only when the flag is zero(i.e the file is not in the internal memory.)
        	print "Downloading the file"
                video = urllib.FancyURLopener() #downloading the file using urllib.
                video.retrieve(url,videoFile)
		curDir = os.getcwd()   # getting the current working directory.
                fullVideoPath = os.path.join(curDir,videoFile)  # Making the full path of the video file.
				
                """For playing the file using openCV first read the file.
                Find the number of frames and the frame rate.
                Finally use these parameters to display each extracted frame on the screen"""

                vidFile = cv.CaptureFromFile(fullVideoPath)  #Video capturing from the file.
                nFrames = int(  cv.GetCaptureProperty( vidFile, cv.CV_CAP_PROP_FRAME_COUNT ) ) #Number of frames in the video.
                fps = cv.GetCaptureProperty( vidFile, cv.CV_CAP_PROP_FPS ) # Frame rate
                waitPerFrame = int( 1/fps * 1000/1 ) # Wait time between frames.

                for f in xrange(nFrames):
                	frameImg = cv.QueryFrame( vidFile ) # decoding and returning the grabbed video frame.
                        cv2.namedWindow("EPIC", cv2.WND_PROP_FULLSCREEN) #Making full size display.
                        cv2.setWindowProperty('EPIC', cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN) # setting the window property to full screen.
                        cv.ShowImage("EPIC",  frameImg) # Showing the frame Image 
                        cv.WaitKey(waitPerFrame) # Waiting between the frames.

                cv.DestroyWindow( "EPIC" ) # Deleting the window once the playing is done.
                return 1 # The file is successfully played.



if __name__ == "__main__":
        url = "http://techslides.com/demos/sample-videos/small.mp4"
        myVideo(url)

