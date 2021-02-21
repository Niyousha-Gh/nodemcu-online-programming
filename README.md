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

  * [python][python] 3.7+
  * flask framework 
  * Cors
  * arduino-cli
  * ESP8266 library on arduino-cli
  * espota.py 


[python]: https://www.python.org/downloads/

Usage
-----

First install python and flask and download arduino-cli exe and espota.py file to your system. Make sure to install Cors on flask and needed

ESP8266 libraries too.

In Order to upload your first code, It's better to put all the files like arduino-cli, espota, nodemcu exe file and online-connection.txt in one directory for example 'C:/Users/NodeMcu', make sure to customize the directories in nodemcu.py file and turn it to an exe file again if your are not using this directory path (you can use PyInstaller package to do so). You should change the servers directory too.

Run Blocklys index.html on a localhost port (you can use python -m http.server 8000 command). Then activate the server.py file which will run on the port 5000 by default. Now Connect to 'ESP8266 Access Point' access point with your PC, the password is 'thereisnospoon'.

If everything goes well hit the 'Upload to NodeMcu' button and it's done. 


example:
```sh
C:\>python pair_generator.py --index C:\Users\Niyousha\dataset\index --others C:\Users\Niyousha\dataset\others
--output C:\Users\Niyousha

```
Note : There is a space between each directory above.

The Script has the following inputs.

`index` is the path of index folder, where the main pictures exist.

`others` is the path of others folder, where the copies of index pictures exist.

`output` is the path of output, where the two folders of "same" & "different" are created.


Contributing
-----

Not yet

Support and Migration
-----

Not yet

License
-----

Not yet  


