# nodemcu-online-programming
This project uploads .ino files from BlocklyDuino to NodeMcu via Wi-Fi. 


Table of Contents
-----------------

  * [Requirements](#requirements)
  * [Usage](#usage)
  * [Contributing](#contributing)
  * [Support and Migration](#support-and-migration)
  * [License](#license)

Requirements
------------

The script requires the following to run:

  * [python]python 3.7+
  * [flask]Flask framework 
  * Cors
  * [arduino-cli]arduino-cli
  * ESP8266 library on arduino-cli
  * [espota.py]espota.py 


[python]: https://www.python.org/downloads/
[flask]: https://flask.palletsprojects.com/en/1.0.x/installation/#installation
[arduino-cli]: https://arduino.github.io/arduino-cli/installation/
[espota.py]: https://github.com/esp8266/Arduino/blob/master/tools/espota.py

Usage
-----

First install python and flask and download arduino-cli exe and espota.py file to your system. Make sure to install Cors on flask and needed
ESP8266 libraries too.

In Order to upload your first code, It's better to put all the files like arduino-cli, espota, nodemcu exe file and online-connection.txt in one directory for example 'C:/Users/NodeMcu', make sure to customize the directories in nodemcu.py file and turn it to an exe file again if your are not using this directory path (you can use PyInstaller package to do so). You should change the servers directory too.

Run Blocklys index.html on a localhost port (you can use python -m http.server 8000 command). Then activate the server.py file which will run on the port 5000 by default. Now Connect to 'ESP8266 Access Point' access point with your PC, the password is 'thereisnospoon'.

If everything goes well hit the 'Upload to NodeMcu' button and it's done. 


Contributing
-----

Not yet

Support and Migration
-----

Not yet

License
-----

Not yet  


