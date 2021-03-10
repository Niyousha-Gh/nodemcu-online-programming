# nodemcu-online-programming
This project uploads .ino files from BlocklyDuino to NodeMcu via Wi-Fi. 


Table of Contents
-----------------

  * [Requirements](#requirements)
  * [Usage](#usage)
  * [How does it work?](#how-does-it-work?)

Requirements
------------

The script requires the following to run:

  * [python] 3.7+
  * [flask] framework
  * [arduino-cli]
  * [espota.py]


[python]: https://www.python.org/downloads/
[flask]: https://flask.palletsprojects.com/en/1.0.x/installation/#installation
[arduino-cli]: https://arduino.github.io/arduino-cli/installation/
[espota.py]: https://github.com/esp8266/Arduino/blob/master/tools/espota.py

Also check [here](https://pypi.org/project/Flask-Cors/) for the Cors Installation on Flask and  [here](https://create.arduino.cc/projecthub/B45i/getting-started-with-arduino-cli-7652a5) for neccessary ESP8266 packages for arduino-cli.

Usage
-----

In Order to upload your first code, download this repository then costomize all the paths inside the nodemcu.py and server.py file. Dont forget to turn the nodemcu.py to an exe file again(you can use [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/installation.html) package to do so). It's better to put all the files like arduino-cli, espota.py, nodemcu exe file and online-connection.txt in one directory for example mine is 'C:/Users/Ice/Downloads/NodeMcu'.
Extract the BlocklyDuino exe then Run it with a localhost port (you can use python -m http.server 8000 command) Then activate the server.py file which will run on port number 5000 by default follow [flask tutorial](https://flask.palletsprojects.com/en/1.1.x/cli/) for more information. Now Connect to 'ESP8266 Access Point' access point, the password is 'thereisnospoon'.

If everything goes well hit the 'Upload to NodeMcu' button and it's done, the code is uploaded.

For further information on how to program your board via wi-fi follow this [video tutorial](https://youtu.be/rau1Ow9f_Z0
) (in persian)

How does it work?
-----

When user hits the 'Upload to NodeMcu' button:
1. BlockyDuino sends the users code to the local server.
2. server saves it as an ino file on the decided directory (here its 'C:/Users/Ice/Downloads/NodeMcu') then runs the nodemcu exe file.
3. nodemcu exe file transfers the code in a folder with the same name, adds some neccessary scripts online_connection.txt file to the users code      in order to make online connection, compile's the code with arduino-cli then uploads it using espota.py through Wi-Fi connection.



