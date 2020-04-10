"""
Three devices on same network and all connected by a switch

	host --- switch ---- host
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
	Your topology file for scenario 1. Define all the required devices here.
	"""
	
	def build(self, k = 3):
		"k: number of hosts"
		self.k = k
		switch = self.addSwitch( 's1' )
		for h in irange( 1, k ):
			host = self.addHost( 'h%s' % h, ip = "10.0.0.%s/24" % h + 1, defaultRoute = "via 10.0.0.1" )
			self.addLink( host, switch )

topos = { 'mytopo':(lambda:MyTopo())}
