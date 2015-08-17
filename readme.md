Running Instructions:

Install the modeule python-opencv in the directory you are running the code.

command: sudo apt-get install python-opencv

Approach :

	step 1:Stripping the file name from the url
	step 2:Using os module to walk through the directory and sub-directory. Increment the flag when match found.
	step 3:if flag is not equal to zero break from the loop.
	step 4:if flag is equal to zero download the file using urllib from the url and play the video using opencv.
	
NOTE: The code will check all the files in directories and sub-directories.


