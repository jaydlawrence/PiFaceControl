PiFaceControl
=============

Simple command line interface to toggle PiFace outputs


###Requirements

* [pifacedigitalio](https://github.com/piface/pifacedigitalio)

**Note:** I am using the Python3 version of pifacedigitalio, so my examples will use Python3, but I assume that it will work the same with the Python2 version of pifacedigitalio.

###Manual
```bash
Options:
  -h, --help            show this help message and exit
  -a ACTION, --action=ACTION
                        action to be taken: toggle, on, off. Default = toggle
  -n NUMBER, --number=NUMBER
                        which number output to change: 0 to 7. Default = 0
```

###Usage
```bash
python3 pi_output_control.py -n 7 
#toggle output number 7


python3 pi_output_control.py --number 6 
#toggle output number 6


python3 pi_output_control.py -a on -n 5 
#turn output number 5 On. 
#if output number 5 is already on, nothing will happen.

```

###Suggested Applications

For a simple timer, set up a [cron](http://en.wikipedia.org/wiki/Cron) job that turns an output on or off at a certain time.

```bash
crontab -e
#access cron tab

#add the following to the cron tab to automatically call the sript at certain times

0 6 * * * python3 /path/to/script/pi_output_control.py -a on -n 7
#turn output 7 on at 6 am

0 18 * * * python3 /path/to/script/pi_output_control.py -a off -n 7
#turn output 7 off at 6 pm

```