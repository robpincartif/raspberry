##Git commands

Status

```
    $ git status
```

Add files

```
    $ git add <name_repository_or_file>
```
Add commit

```
    $ git commit -m '<comments>'
```    

  Upload files

```
    $ git push origin master
```

##Install LCD TouchScreen



Get the LCD_show_v4

```
sudo wget https://dl.dropboxusercontent.com/u/2183/LCD_show_v4.tar.gz

http://en.kedei.net/raspberry/raspberry.html 
```

Unpack it to the Raspberry pi
```
tar xzvf LCD_show_v4.tar.gz
```

Remove the downloaded file. ( This step saves space)
``` 
sudo rm -r /home/pi/LCD_show_v4.tar.gz
```
Enable the LCD screen with driver.

Go to the map where LCD_show_v4 is located
```
cd LCD_show_v4
```

Run the command to turn on the LCD screen.
```
./LCD35_v4
```

About a minute later the system says that it is going down for a reboot. The LCD screen is now on and you must see the boot up screen!

Back to HDMI:

Go to the map where LCD_show_v4 is located
```
cd LCD_show_v4
```
Run the command to activate the HDMI output.

```
./LCD_hdmi
```
About a minute later the system says that it is going down for a reboot. And... HDMI is back!


##Install WiringPi

```
    $ git clone https://github.com/Gadgetoid/WiringPi2-Python.git
    $cd WiringPi2-Python
    $ sudo python setup.py install

```
```
    git clone git://git.drogon.net/wiringPi
    cd wiringPi
    ./build
```
Add in /etc/rc.local

```
    /etc/set_gpio_pins.sh

```

set_gpio_pins.sh

```
	for pin in 27;do
	echo "$pin" > /sys/class/gpio/export
	chmod 777 -R /sys/class/gpio/gpio$pin
	echo "out" > /sys/class/gpio/gpio$pin/direction
	done

```

##Install servoblaster

```
    $ git clone https://github.com/richardghirst/PiBits.git
    $ cd PiBits/ServoBlaster/kernel
    $ make install
    $ make install_autostart
```

Compile and start

```
    $ cd PiBits/ServoBlaster/user
    $ make
    $ sudo ./servod
```
To configure

```
    $ sudo ./servod <options>
```
options[] = {
	{ "pcm",          no_argument,       0, 'p' },
	{ "idle-timeout", required_argument, 0, 't' },
	{ "help",         no_argument,       0, 'h' },
	{ "p1pins",       required_argument, 0, '1' },
	{ "p5pins",       required_argument, 0, '5' },
	{ "min",          required_argument, 0, 'm' },
	{ "max",          required_argument, 0, 'x' },
	{ "invert",       no_argument,       0, 'i' },
	{ "cycle-time",   required_argument, 0, 'c' },
	{ "step-size",    required_argument, 0, 's' },
	{ "debug",        no_argument,       0, 'f' },
	{ "dma-chan",     required_argument, 0, 'd' },
	{ 0,              0,                 0, 0   }
}

```
    $ sudo ./servod -t 5000 -c 100000 -s 20 --p1pins=11,12,15,16
```

Use:

```
    $ sudo echo 0=120 > /dev/servoblaster
```
Dataplicity

```
curl -s https://www.dataplicity.com/rjjqbyfi.sh | sudo sh

```
Raspberry Pi3
VNC Server

```
sudo apt-get install tightvncserver
```
With you favorite text editor,create a text file "/etc/lightdm/lightdm.conf" with the following contents:
```
[VNCServer]
enabled=true
port=5900
width=1360
height=768
depth=16
```
The value of width and height describes the window resolution when connecting with a VNC client. Other width x height working resolutions are possible with: 800x600, 1024x768, 1152x854, 1280x768, 1280x800, 1280x960, 1280x1024, 1400x1050, 1440x900, 1600x1200, 1680x1050, 1792x1344, 1856x1392, 1920x1200, 1920x1220, 2560x1600.
```
sudo /etc/init.d/lightdm restart

```
