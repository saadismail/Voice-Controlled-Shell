import os
import subprocess
import main

def runCommand(text):
	if "shutdown" in text:
		main.speak_to_speaker("Shuting Down the PC.")
		os.system("shutdown -h now")
		
	elif "list all the files in long format" in text or "list all the files with permissions." in text:
		s = str(subprocess.check_output(['ls','-l']))
		print(s)
		main.speak_to_speaker("All files present in the directory " + str(subprocess.check_output(['pwd'])) + " are displayed on terminal with permissions.")
	
	elif "list all the files" in text:
		s = str(subprocess.check_output(['ls']))
		print(s)
		main.speak_to_speaker("All files present in the directory " + str(subprocess.check_output(['pwd'])) + " are displayed on terminal.")
	
	elif "list all the hidden files" in text:
		os.system("ls -a")
		main.speak_to_speaker("All hidden files present in the directory " + str(subprocess.check_output(['pwd'])) + " are displayed on terminal.")

	elif "what is the current working directory" in text:
		s = str(subprocess.check_output(['pwd']))
		print(s)

#s = str(subprocess.check_output(['date','+%a']))
#recognize_speech_from_mic(recognizer, microphone)
