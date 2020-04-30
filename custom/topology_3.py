"""
A complex containing 3 routers, 5 switches, 5 subnets and 15 hosts.
"""

from mininet.topo import Topo
from mininet.util import irange

class MyTopo(Topo):
	"Simple topology example."

	def __init__(self):
		"Create custom topology."
		#Initialize the topology
		Topo.__init__(self)
	
	"""
	[555 Comments]
	Your topology file for scenario 3. Define all the required devices here.
	"""
	def build(self):
		# routers
		rone = self.addSwitch('r1')
		rtwo = self.addSwitch('r2')
		rthree = self.addSwitch('r3')

		# switches
		sfour = self.addSwitch('s4')
		sfive = self.addSwitch('s5')
		ssix = self.addSwitch('s6')
		sseven = self.addSwitch('s7')
		seight = self.addSwitch('s8')

		# hosts
		for h in irange( 9, 11):
				host = self.addHost( 'h%s' % h, ip = "172.17.16.%s/24" % str(h-7), defaultRoute = "via 172.17.16.1")
				self.addLink( host, sfour )
		for h in irange( 12, 14):
				host = self.addHost( 'h%s' % h, ip = "10.0.0.%s/25" % str(h-10), defaultRoute = "via 10.0.0.1")
				self.addLink( host, sfive )
		for h in irange( 15, 17):
				host = self.addHost( 'h%s' % h, ip = "10.0.0.%s/25" % str(h+115), defaultRoute = "via 10.0.0.129")
				self.addLink( host, ssix )
		for h in irange( 18, 20):
				host = self.addHost( 'h%s' % h, ip = "20.0.0.%s/25" % str(h-16), defaultRoute = "via 20.0.0.1")
				self.addLink( host, sseven )
		for h in irange( 21, 23):
				host = self.addHost( 'h%s' % h, ip = "20.0.0.%s/25" % str(h+109), defaultRoute = "via 20.0.0.129")
				self.addLink( host, seight )

		# links
		self.addLink( rone, sfour, 1 )
		self.addLink( rone, rtwo, 2, 3 )
		self.addLink( rone, rthree, 3, 3 )
		self.addLink( rtwo, sfive, 1 )
		self.addLink( rtwo, ssix, 2 )
		self.addLink( rthree, sseven, 1 )
		self.addLink( rthree, seight, 2 )

topos = { 'mytopo':(lambda:MyTopo())}