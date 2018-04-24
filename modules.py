import os
import subprocess
import main

def runCommand(text):
	if "shutdown" in text:
		os.system("shutdown -h now")
		main.speak_to_speaker("Shuting Down the PC.")
	
	elif "list files" in text:
		s = str(subprocess.check_output(['ls']))
		print(s)
		main.speak_to_speaker("All files present in the directory " + str(subprocess.check_output(['pwd'])) + " are displayed on terminal.")
	
	elif "list formated files" in text or "list file permissions" in text:
		s = str(subprocess.check_output(['ls','-l']))
		print(s)
		main.speak_to_speaker("All files present in the directory " + str(subprocess.check_output(['pwd'])) + " are displayed on terminal with permissions.")
	
	elif "list hidden files" in text:
		s = str(subprocess.check_output(['ls','-a']))
		print(s)
		main.speak_to_speaker("All hidden files present in the directory " + str(subprocess.check_output(['pwd'])) + " are displayed on terminal.")
	
	elif "current working directory" in text:
		s = str(subprocess.check_output(['pwd']))
		print(s)
	
	elif "what is the date today" in text:
		s = str(subprocess.check_output(['date','+%c']))
		print(s)
		main.speak_to_speaker(s)
	
	elif "what is the day today" in text:
		s = str(subprocess.check_output(['date','+%A']))
		print(s)
		main.speak_to_speaker(s)
	
	elif "what is the time" in text:
		s = str(subprocess.check_output(['date','+%T']))
		print(s)
		main.speak_to_speaker(s)
	
	elif "calendar" in text:
		s = str(subprocess.check_output(['cal']))
		print(s)
		main.speak_to_speaker("The Calendar for the " + str(subprocess.check_output(['date','+%B'])) + " month and " + str(subprocess.check_output(['date','+%Y'])) + " year is printed on the screen.")		
	
	elif "what is the username" in text:
		s = str(subprocess.check_output(['whoami']))
		print(s)
		main.speak_to_speaker("The user name is "+ s)		
	
	elif "create a random file" in text:
		s = str(subprocess.check_output(['touch','-t']))
		print(s)
		main.speak_to_speaker("A file has been created in " + str(subprocess.check_output(['pwd'])))
	
	elif "go to home directory" in text:
		s = str(subprocess.check_output(['cd','/home']))
		print(s)
		main.speak_to_speaker("Your have moved to home directory.")
	
	elif "go to root directory" in text:
		s = str(subprocess.check_output(['cd','/']))
		print(s)
		main.speak_to_speaker("Your have moved to root directory.")
	
	elif "go to my directory" in text:
		s = str(subprocess.check_output(['cd','~']))
		print(s)
		main.speak_to_speaker("Your have moved to your directory.")
	
	elif "what is the day" in text:
		import datetime
		now = datetime.datetime.now()
		s = now.strftime("%A")
		main.main.speak_to_speaker("Today is " + s)
		print("Today is " + s)

	elif "what is the date" in text:
		import datetime
		now = datetime.datetime.now()
		s = now.strftime("%d %m %Y")
		main.main.speak_to_speaker("Today is " + s)
		print("Today is " + s)

	elif "run ps" in text:
		s = str(subprocess.check_output(['ps','-A']))
		print(s)
		main.main.speak_to_speaker("All processes are shown in the terminal")

	elif "show network status" in text:
		s = str(subprocess.check_output(['ifconfig']))
		print(s)
		main.main.speak_to_speaker("Network configuration is shown in the terminal")