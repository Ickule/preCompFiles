import csv
import numpy as np
import os

# Setting all the diferent cases that need to be taken into account for file genreration
cases=['P_class','M_class']

# Initialisong fundamental related and fixed variables
omega0 = 50*2*np.pi
Xm = 230
freq = 50.
ramp = 1
samplingRate = 44100

# Initialisong time related variables
timeNomWait = 5
ptTimeNomWait = timeNomWait*samplingRate+1
timeNomWaitArray = np.linspace(0,timeNomWait,ptTimeNomWait)
timeTest = 30
ptTimeTest = timeTest*samplingRate+1
timeTestArray = np.linspace(0,timeTest,ptTimeTest)

# Computing nominal signal
nomSig = Xm*np.sin(omega0*timeNomWaitArray)

# Creating the root path and directory for the files
cwd = os.getcwd()
rootPath = os.path.join(cwd,'Ramp in frequency')
if not os.path.exists(rootPath):
    os.mkdir(rootPath)

for case in cases:

    print("Working on %s" %case)
    
    # initialising a time counter to reuse nominal signal value and test signal value at diferent time offsets
    timeCounter = 0
    
    #initialising the test signal array
    testSig = []
  
    # Initialisong case dependent variables
    if (case == 'P_class'):
        val_min = 48
        val_max = 52
        
    if (case == 'M_class'):
        val_min = 45
        val_max = 55
 
    # Calculation the current frequency with respect to the ramp and calculating the test signal
    for i in range(ptTimeTest):
        if((ramp == 1 and (freq+ramp/samplingRate) > val_max) or (ramp == -1 and (freq+ramp/samplingRate) < val_min)):
            ramp *= -1
        freq += ramp/samplingRate
        print(freq,timeTestArray[i])
        testSig.append(Xm*np.sin(omega0*timeTestArray[i]+np.pi*freq*timeTestArray[i]))
   
    # Creating the final path for the file
    path = os.path.join(rootPath,case)
    if not os.path.exists(path):
        os.mkdir(path)
    path = os.path.join(path,'%s_RiF.csv' %case)

    with open(path, 'w', newline='', encoding='utf-8') as file:

        # Writing data in the final file
        writer = csv.writer(file)
        writer.writerow(("Time (s)","Voltage (V)"))
        
        for i in range(ptTimeNomWait):
            writer.writerow([timeNomWaitArray[i],0])
        timeCounter += timeNomWait

        for i in range(ptTimeNomWait):
            writer.writerow([timeNomWaitArray[i]+timeCounter,nomSig[i]])
        timeCounter += timeNomWait
        
        for i in range(ptTimeTest):
            writer.writerow([timeTestArray[i]+timeCounter,testSig[i]])
        timeCounter += timeTest

        for i in range(ptTimeNomWait):
            writer.writerow([timeNomWaitArray[i]+timeCounter,nomSig[i]])
        timeCounter += timeNomWait

        for i in range(ptTimeTest):
            writer.writerow([timeTestArray[i]+timeCounter,testSig[i]])
        timeCounter += timeTest

        for i in range(ptTimeNomWait):
            writer.writerow([timeNomWaitArray[i]+timeCounter,nomSig[i]])
        timeCounter+=timeNomWait

        for i in range(ptTimeTest):
            writer.writerow([timeTestArray[i]+timeCounter,testSig[i]])
        timeCounter += timeTest

        for i in range(timeNomWait):
            writer.writerow([timeNomWaitArray[i]+timeCounter,nomSig[i]])
        timeCounter+=timeNomWait

        for i in range(ptTimeTest):
            writer.writerow([timeTestArray[i]+timeCounter,testSig[i]])
        timeCounter += timeTest

        for i in range(timeNomWait):
            writer.writerow([timeNomWaitArray[i]+timeCounter,nomSig[i]])
        timeCounter += timeNomWait

        for i in range(timeTest):
            writer.writerow([timeTestArray[i]+timeCounter,testSig[i]])
        timeCounter += timeTest

        for i in range(ptTimeNomWait):
            writer.writerow([timeNomWaitArray[i]+timeCounter,nomSig[i]])
        timeCounter += timeNomWait

        for i in range(ptTimeNomWait):
            writer.writerow([timeNomWaitArray[i]+timeCounter,0])