
# Voice-Controlled-Shell

## Introduction
Voice-Controlled Shell is a python based personal assistant to execute bash commands/scripts from voice.

## Pre-Requisites

 - Python 2.x/3.x
 - Google TTS
 - Speech_Recognition (Google STT)
 - PyAudio

## Installation
### For Debian-based systems:
Update system packages

    sudo apt-get update
    sudo apt-get upgrade

Install pip

    sudo apt-get install python-setuptools python-dev build-essential
    sudo easy_install pip
Install required libraries

    sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
    sudo apt-get install ffmpeg libav-tools
    sudo pip install pyaudio
    sudo pip install SpeechRecognition
    sudo pip install gTTS

## Usage
    git clone https://github.com/saadismail/Voice-Controlled-Shell
    cd Voice-Controlled-Shell
    python main.py OR python2.7 main.py

This is how a sample coversation goes:

-   _You_: “hello”
-   _Assistant_:  _high beep_
-   _You_:  _speak your command_
-   _Assistant_:  _low beep_
-   _Assistant_:  _speaks the response_

### Valid commands

|Commands|Description|
|--|--|
| shutdown | shutdown the PC immediately |
| list files | List all files |
| list formated files | List all files in long format with permission |
| list file permissions | List all files in long format with permission |
| list hidden files | list hidden files |
| current working directory | Present Working Directory |
| where I am standing | Present Working Directory |
| what is the date today | Tells the date |
| what is the day | today   Tells the day |
| what is the time | Tells the time |
| calendar | Displays the calendar |
| what is the username | tells the user name |
| create a random file | create a file with timestamp name |
| go to home directory | go to home directory |
| go to root directory | go to root directory |
| go to my directory | go to home directory for the current user |
| run ps | snapshot of current processes |
| show network status | network configuration |
| create a link | create a shortcut |
| delete a file | delete a file |
| remove a file | delete a file |
| create a file | create a new file |
| just open nano editor | open nano |
| just open gedit editor | open gedit |
| just open sublime editor | open sublime (subl) |
| open nano editor | open nano with specified name |
| open gedit editor | open gedit with specifed name |
| open sublime editor | open sublime (subl) with specifed name |
| tell me the file type | displays a file type of specifed name |
| maunal | manual of any command |
| what is the status and configuration of network | Displays status and configuration of network |
| make a new directory | make a new directory |
| login as root user | login as root user |
| list users | list all users |
| list all users | list all users |
| list user | list all users |
| add user for login | add users for login |
| delete user | delete user |
| permanent delete user | delete user with its home directory |
| remove user from home | delete user home directory if it is previously deleted |
| who created you | tells the description of Awesome Group |
|  |  |

