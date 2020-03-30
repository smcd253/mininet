"""
Three devices on different networks and all connected by a single router

	host --- router ---- host
		   		|
		   		|
		   		|
		  	   host

"""

from mininet.topo import Topo

class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
	"Create custom topology."

	#Initialize the topology
	Topo.__init__(self)
	
	"""
	[555 Comments]
	Your topology file for scenario 2. Define all the required devices here.
	"""

topos = { 'mytopo':(lambda:MyTopo())}