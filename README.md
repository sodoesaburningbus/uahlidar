# uahlidar
This repository contains the code to read data from the UAH lidar

This code reads and plots stare data from the University of
Alabama in Huntsville's LIDAR
Written by Christopher Phillips

License:
This code may be used and distributed freely, provided
proper attribution is given.


Requirements:
Python3
Numpy
Matplotlib
TKinter

History:
June 10, 2016 - First Write
June 11, 2016 - Completed Vertical Velocity
June 12, 2016 - Added Intensity Plot
June 17, 2016 - Changed method of file input
June 18, 2016 - Added support for tkinter and created file dialog


Planned Features:
Check Elevation to ensure Lidar is in Stare mode


How to Use:
Run with "python lidar_rp.py"
User will be prompted for the input file (this is a dialog box)
User will be prompted for the bounds on vertical velocity. These are symmetric.
What the user inputs will be used for both upward and downward motions. Default is 5m/s.
User will also be prompted for intensity limit (SNR+1). This limits the maximum plotted intensity.
Default intensity limit is 2.0.


Example header from my files
Filename:	"file path at creation"
System ID:	58
Number of gates:	200
Range gate length (m):	30.0
Gate length (pts):	10
Pulses/ray:	7500
No. of rays in file:	1
Scan type:	Stare
Focus range:	65535
Start time:	20131216 01:00:20.56
Resolution (m/s):	0.0382
Altitude of measurement (center of gate) = (range gate + 0.5) * Gate length
Data line 1: Decimal time (hours)  Azimuth (degrees)  Elevation (degrees)
f9.6,1x,f6.2,1x,f6.2
Data line 2: Range Gate  Doppler (m/s)  Intensity (SNR + 1)  Beta (m-1 sr-1)
i3,1x,f6.4,1x,f8.6,1x,e12.6 - repeat for no. gates
****
End Example Header
