from pifacedigitalio import PiFaceDigital
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-a","--action", dest="action", default="toggle", help="action to be taken: toggle, on, off. Default = toggle")

parser.add_option("-n","--number", dest="number", type="int", default=0, help="which number output to change: 0 to 7. Default = 0")

(opts, args) = parser.parse_args()

if opts.action not in ["toggle", "on", "off"]:
	print('Action can only be "toggle", "on" or "off"')
	exit(-1)

if opts.number > 7 or opts.number < 0:
	print('Number can only be an interger between 0 and 7')
	exit(-1)


pi = PiFaceDigital(init_board=False)

if opts.action == "on":
	pi.output_pins[opts.number].turn_on()	
elif opts.action == "off":
	pi.output_pins[opts.number].turn_off()
else:
	pi.output_pins[opts.number].toggle()
