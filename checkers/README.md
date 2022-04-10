#Weclome to Checkers

----
##What should i do to run the game?

----
###step 1) you should install python3 
type this commands in terminal
####$sudo apt-get update
####$sudo apt-get install python3.8 python3-pip
###step 2) now install pip command for python3
type this commands in terminal
####$sudo apt update
####$sudo apt install python3-pip
###step 3) now to build the project you need to insall pygame module
The best way to install pygame is with the pip tool (which is what python uses to install packages). Note, this comes with python in recent versions. We use the --user flag to tell it to install into the home directory, rather than globally.

type commands in terminals
####$python3 -m pip install -U pygame --user
To see if it works, run one of the included examples:

####$python3 -m pygame.examples.aliens
now to run the game do the following steps

----open the checkers directory from tech0Rudolf
then type
####$pip freeze > requirements.txt
that will create the requirements.txt
#.......
or just open checkers directory in pycharm ide and run the checkers.py
export PYTHONPATH=export PYTHONPATH=/home/rudolf:/usr/lib/python38.zip:/usr/lib/python3.8:/usr/lib/python3.8/lib-dynload:/home/rudolf/.local/lib/python3.8/site-packages:/usr/local/lib/python3.8/dist-packages:/usr/lib/python3/dist-packages
