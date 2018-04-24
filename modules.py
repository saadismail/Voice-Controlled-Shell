import os

def runCommand(text):
	if "shutdown" in text:
		os.system("shutdown -h now")

	elif "list all files" in text:
		os.system("ls")