## Git commands

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


  Install LCD TouchScreen

```
    $ http://uncle-muddy.me.uk/adafruit-pitft-2-8-on-ubuntu/
```

  Install WiringPi

```
    $ git clone https://github.com/Gadgetoid/WiringPi2-Python.git
    $cd WiringPi2-Python
    $ sudo python setup.py install

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

## Install servoblaster

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
