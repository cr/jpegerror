#!/usr/bin/env python

#import easygui
import Image
import sys

#filename = easygui.fileopenbox()

try:
	fileA = sys.argv[1]
	imgA = Image.open( fileA ).convert( 'RGBA' )
except:
	print >>sys.stderr, "ERROR:", sys.exc_info()
        sys.exit(1)

try:
	fileB = '/tmp/xxx_tmp.jpg'
	imgA.save( fileB, 'JPEG', quality=95 )
	imgB = Image.open( fileB ).convert( 'RGBA' )
except:
	print >>sys.stderr, "ERROR:", sys.exc_info()
	sys.exit(1)

(xSize, ySize) = imgA.size
imgC = Image.new( 'RGBA', (xSize, ySize) )

mul = 10

for y in range( 0, ySize ):
	for x in range( 0, xSize ):
		colorA = (rA, gA, bA, aA) = imgA.getpixel( (x,y) )
		colorB = (rB, gB, bB, aB) = imgB.getpixel( (x,y) )
		colorC = ( abs(rA-rB)*mul, abs(gA-gB)*mul, abs(bA-bB)*mul, 255 )
		imgC.putpixel( (x,y), colorC )

#imgC.save( sys.stdout, "PNG" )
imgC.show()

