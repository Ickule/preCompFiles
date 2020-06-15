import csv
import os
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk()
root.withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(initialdir=os.getcwd(), title="Please select a file",filetypes=[("CSV files", "*.csv")]) # show an "Open" dialog box and return the path to the selected file
root.destroy()

time = []
signal = []

with open(filename, "r") as csvFile:
    csvRead = csv.reader(csvFile, delimiter=',')
    next(csvRead)
    
    for row in csvRead:
        time.append(float(row[0]))
        signal.append(float(row[1]))
            
sampling = int(len(time)/time[-1])
ptTimeTest = 30*sampling+1
ptTimeNomWait = 5*sampling+1     
lim = ptTimeNomWait*7+5*ptTimeTest
i = 1
start = 0
stop = ptTimeNomWait

plt.title('Example signal')
plt.plot(time[:ptTimeNomWait],signal[:ptTimeNomWait],'r')
while stop < lim:
    if i == 1:
        start = stop
        stop += ptTimeNomWait
        plt.plot(time[start:stop],signal[start:stop],'g')
        i = 0
    else:
        start = stop
        stop += ptTimeTest
        plt.plot(time[start:stop],signal[start:stop],'b')
        i = 1
plt.plot(time[stop:],signal[stop:],'r')
sampling = int(len(time)/time[-1])

plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')

plt.show()