# About Julee - An Intelligent Voice Assisstant
Julee is a voice commanding assistant service in [Python 3.8](https://www.python.org/downloads/release/python-360/).
It can recognize human speech, talk to user and execute basic commands.

## Julee Skills
> Tell the time

> Tell the weather forecast

> Give a joke

> Searching on web

> Open/close application

> Voice keyboard control

> Voice mouse control

> and much more...


## Julee Features
> Virtual Assistant

> Voice control


## Julee common commands list
#### CONTROL MODE COMMANDS:

> Start dictating/ start detecting/ start typing - text typing using voice(must navigate to the text field before running the command)

> Stop dictating/ stop detecting/ stop typing - exit text typing mode

> (*)Start listening/ Start control - Control computer with Speech Recognition

> Stop listening - Stop control the computer

> Exit control mode/ Exit voice control/ Exit smart control - stop control mode and return to virtual assistant mode

#### GRID MODE COMMANDS:
> Number of the square; 1; 7; 9 - Move the pointer to the center of a mousegrid square

> Click number of the square - Select a mousegrid square

> Number of the square where the item appears (followed by) mark; 3 mark; 7 mark; 9 mark - Select an item to drag with the mouse

> Number of the square where you want to drag the item (followed by) click; 4 click; 5 click; 6 click - Select an area in the mousegrid where you want to drag the item

#### OTHER COMMANDS:
> Click Recycle Bin; click Computer; click file name - Select an item or icon

> Double-click Computer; double-click folder name - Double-click an item

> Right-click Computer; right-click Recycle Bin; right-click folder name - Right-click an item

> Show desktop - Minimize all windows to show your desktop

> Show numbers (Numbers will appear on the screen for every item in the active window. Say an item's corresponding number to select it.) - Select something if you don't know what it's called

> 19 OK; 5 OK - Select a numbered item

> Double-click 19; Double-click 5 - Double-click a numbered item

> Right-click 19; Right-click 5 - Right-click a numbered item

> Minimize that; Minimize Paint; Minimize Documents - Minimize

> Maximize that; Maximize Paint; Maximize Documents - Maximize

> Cut that; Cut 

> Copy that; Copy

> Paste

> Delete that; Delete

> Undo that; Scratch that; Undo

> Scroll up; Scroll down; Scroll right; Scroll left - Scroll an exact distance in pages

> Scroll up 5; Scroll down 7 - Scroll an exact distance in other units

> Press keyboard key; press A; press capital B; press Shift plus A; press Ctrl plus A - Press a key or key combination

> Delete; Backspace; Enter; Page Up; Page Down; Home; End; Tab - Press certain keyboard keys without saying "press" first

> Minimize speech recognition - Minimize the microphone bar

> Switch to Paint; Switch to program name; Switch application - Switch to an open app


## Getting Started

#### Requirements
Minimum system requirement: 
Below is the minimum requirement for the machine. Be aware that the better your system hardware, the faster Julee can run with stable performance. In detail:
>   Operating System: Windows 10 64-bit, Version 1903 (19H1) or higher (the older version is supported but not maintained if errors occur).

>   Processor: 1 gigahertz (GHz) or faster processor

>   Memory: 2GB of RAM.

>   Sound Card: Windows-compatible audio device.

>   Display resolution: 800 x 600 pixels

Other hardware requirements: 
>   A built-in microphone on a laptop or external microphone is needed.


#### Installation
> All stable versions of Julee can be found on the Julee releases list or visit: https://github.com/riczfe/SEPM_GROUP6/releases. The latest release will be displayed on top, with full detailed information about the updated patch for each version. 

> To download to your machine, click on the Assets dropdown menu, then click on the Julee-installation.zip file, it will automatically download to your machine.

> If there is a pop-up window appears on your browser, simply choose the location you want to save it, and click Save to download the file.

> After finishing the download, you want to navigate to the folder/location where you save the zip file. Extract the file by Right-click on the zip file and selecting “Extract Here” if you have WinRar installed, or select “7-Zip”, and choose “Extract Here”.

> Inside the folder you just extracted, there will be a file called “julee” or “julee.exe” if you enable the File name extension option on your machine. Right-click on it and select “Run as administrator”.

> Note: Julee must be run as administrator in order to work correctly. If you want to set up the application to run as an administrator everytime, you might want to follow this guide: https://www.windowscentral.com/how-set-apps-always-run-administrator-windows-10

Other software installation:
>   Java Runtime Environment (JRE) 1.8.0 or higher.

>   Python 3 or higher.

>   Python library that must be installed correctly into system environment path:

        Library package     Version
        numpy               1.19.5
        PyAudio             0.2.11
        scikit-image        0.19.2
        scipy               1.8.0
        SpeechRecognition   3.8.1
        wikipedia           1.4.0
        wolframalpha        5.0.0
        pyjokes             0.6.0
        webdriver-manager   3.5.4
        requests            2.27.1
        pyautogui           0.9.53
        gTTS                2.2.4
        nltk                3.6.7
        playsound           1.2.2
        tensorflow          2.6.2
        pygame              2.1.2
        pyttsx3             2.90
        
All of the dependencies is located inside “Julee Voice Assistant/src/main/requirements.txt”. We highly recommend installing it using pip as the following guide: https://intellipaat.com/community/31672/how-to-use-requirements-txt-to-install-all-dependencies-in-a-python-project.

## License
[MIT License](https://github.com/riczfe/SEPM_GROUP6/blob/main/LICENSE). 
