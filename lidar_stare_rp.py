#This code reads and plots stare data from the University of
#Alabama in Huntsville's LIDAR
#Written by Christopher Phillips
#
#License:
#This code may be used and distributed freely, provided
#proper attribution is given.
#
#
#Requirements:
#Python3
#Numpy
#Matplotlib
#TKinter
#
#History:
#June 10, 2016 - First Write
#June 11, 2016 - Completed Vertical Velocity
#June 12, 2016 - Added Intensity Plot
#June 17, 2016 - Changed method of file input
#June 18, 2016 - Added support for tkinter and created file dialog
#
#
#Planned Features:
#Check Elevation to ensure Lidar is in Stare mode
#
#
#How to Use:
#Run with "python lidar_rp.py"
#User will be prompted for the input file (this is a dialog box)
#User will be prompted for the bounds on vertical velocity. These are symmetric.
#What the user inputs will be used for both upward and downward motions. Default is 5m/s.
#User will also be prompted for intensity limit (SNR+1). This limits the maximum plotted intensity.
#Default intensity limit is 2.0.
#
#
#Example header from my files
#Filename:	"file path at creation"
#System ID:	58
#Number of gates:	200
#Range gate length (m):	30.0
#Gate length (pts):	10
#Pulses/ray:	7500
#No. of rays in file:	1
#Scan type:	Stare
#Focus range:	65535
#Start time:	20131216 01:00:20.56
#Resolution (m/s):	0.0382
#Altitude of measurement (center of gate) = (range gate + 0.5) * Gate length
#Data line 1: Decimal time (hours)  Azimuth (degrees)  Elevation (degrees)
#f9.6,1x,f6.2,1x,f6.2
#Data line 2: Range Gate  Doppler (m/s)  Intensity (SNR + 1)  Beta (m-1 sr-1)
#i3,1x,f6.4,1x,f8.6,1x,e12.6 - repeat for no. gates
#****
#End Example Header


#Importing Modules
import matplotlib.pyplot as pp
import numpy
import tkinter as tk
from tkinter import filedialog as fd

#Driver Function
def lidar_read_plot():
	
	#Requesting file from user
	root = tk.Tk() #Creating tkinter instance
	root.withdraw()
	lun = fd.askopenfile(initialdir=".") #creating file object
	root.destroy() #destroying tkinter instance

	#Prompting user for vertical velocity limit
	vlim = input("Please give a bound for vertical velocity in m/s\nLeave blank for default\n")
	if vlim == "":
		vlim = 5.0
	else:
		vlim = numpy.float(vlim)

	snrlim = input("Please give upper bound for intensity (SNR+1)\nLeave blank for default\n")
	if snrlim == "":
		snrlim = 2.0
	else:
		snrlim = numpy.float(snrlim)

	#Initializing necessarry lists
	header = list()
	time = list() #In decimal hour UTC
	elevation = list() #These are made available to check that Lidar is in stare mode
	gate = list() #Vertical point at which measurement is taken
	vert_vel = list() #In m/s
	snr = list() #Signal-to-Noise + 1
		
	#File line bookkeeping
	head = True #Telling read that file starts with file header
	last_head = "****\n" #Last line in header
	i = 0 #Counts the number of data lines
	
	#Reading file
	for line in lun:
		if head:
			if line == last_head:
				head = False
			header.append(((line.strip("\n").split(":"))[-1]).strip())
		else:
			temp_line = (line.strip("\n").split())
			if len(temp_line)==3:
				ctime = temp_line[0]
			else:
				time.append(ctime)
				gate.append(temp_line[0])
				vert_vel.append(temp_line[1])
				snr.append(temp_line[2])
		i += 1 #Incrementing line counter
	print(i, "lines read")			
	lun.close()

	#Convert lists to numpy arrays for processing
	time = numpy.array(time, dtype=float)
	gate = numpy.array(gate, dtype=float)
	vert_vel = numpy.array(vert_vel, dtype=float)
	snr = numpy.array(snr, dtype=float)

	#Calculating height of each measurement
	height = (gate + 0.5)*numpy.float(header[3])

	#Clipping data to user-defined bounds
	numpy.clip(vert_vel, -vlim, vlim, out=vert_vel)
	numpy.clip(snr, min(snr), snrlim, out=snr)

	#Plotting
	pp.subplot(2,1,1)
	pp.scatter(time, height ,c=vert_vel, s=4, marker='s',lw=0)
	pp.xlabel("Time (UTC)")
	pp.ylabel("Height (m)")
	pp.axis([min(time),max(time),0.0,max(height)])
	cbar = pp.colorbar()
	cbar.set_label("Vertical Velocity (m/s)", rotation=90)
	
	pp.subplot(2,1,2)
	pp.scatter(time, height ,c=snr, s=4, marker='s',lw=0)
	pp.xlabel("Time (UTC)")
	pp.ylabel("Height (m)")
	pp.axis([min(time),max(time),0.0,max(height)])
	cbar = pp.colorbar()
	cbar.set_label("Intensitiy (SNR+1)")

	pp.show()

#Calling main function
lidar_read_plot()
