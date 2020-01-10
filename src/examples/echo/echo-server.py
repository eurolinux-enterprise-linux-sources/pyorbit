#! /usr/bin/env python

import ORBit
import CORBA
import sys, os

import CORBA
try:
    if CORBA.ORB_ID == "omniORB4": # don't forget omniidl -bpython echo.idl
        pass #print "using omniORB"
except AttributeError:
    # ORBit's CORBA has no ORB_ID
    import ORBit
    #print "using ORBit"
    #ORBit.load_file("./echo.idl")
    ORBit.load_typelib("echo")

import Test__POA

class EchoServant(Test__POA.Echo):

    def echo(self, message):
	print "Received message: '%s'" % message
        return message

    def quit(self):
	print "Quitting..."
	global orb
	orb.shutdown(0)


orb = CORBA.ORB_init(sys.argv)
	
servant = EchoServant()
objref = servant._this()
file('iorfile', 'w').write(orb.object_to_string(objref))

#servant._default_POA().the_POAManager.activate()
poa = orb.resolve_initial_references("RootPOA")
poa._get_the_POAManager().activate()

orb.run()

os.unlink("iorfile")

