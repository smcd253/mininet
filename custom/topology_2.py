"""
Three devices on different networks and all connected by a single router

	host --- router ---- host
		   		|
		   		|
		   		|
		  	   host

"""

from mininet.topo import Topo
from mininet.util import irange

class MyTopo(Topo):
	"Simple topology example."

	def __init__(self):
		#Initialize the topology
		Topo.__init__(self)
	
	"""
	[555 Comments]
	Your topology file for scenario 2. Define all the required devices here.
	"""
	def build(self, k = 3):
		"k: number of hosts"
		self.k = k
		switch = self.addSwitch( 'r1', interfaces = {"10.0.0.1", "20.0.0.1", "30.0.0.1"})
		for h in irange( 1, k ):
			host = self.addHost( 'h%s' % h, ip = "%s0.0.0.2/24" % str(h), defaultRoute = "via %s0.0.0.1" % str(h) )
			self.addLink( host, switch )

topos = { 'mytopo':(lambda:MyTopo())}