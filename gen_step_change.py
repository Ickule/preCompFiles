import csv
import numpy as np
import os

# Setting all the diferent cases that need to be taken into account for file genreration
cases=['P_class','M_class']
mods=['amplitude','phase']

# Initialisong time related variables
timeNomWait = 5
ptTimeNomWait = timeNomWait*10000+1
timeNomWaitArray = np.linspace(0,timeNomWait,ptTimeNomWait)
timeTest = 30
ptTimeTest = timeTest*10000+1
timeTestArray = np.linspace(0,timeTest,ptTimeTest)

# Initialisong fundamental related and fixed variables
omega0 = 50*2*np.pi
Xm = 230
stepMax = 1
stepMin = -1

# Computing nominal signal
nomSig = Xm*np.sin(omega0*timeNomWaitArray)

# Creating the root path and directory for the files
cwd = os.getcwd()
rootPath = os.path.join(cwd,'Step change')
if not os.path.exists(rootPath):
    os.mkdir(rootPath)

for case in cases:

    for mod in mods:
    
        print("Working on %s for %s" %(mod,case))
        
        # initialising a time counter to reuse nominal signal value and test signal value at diferent time offsets
        timeCounter = 0
        
        # initialising test signal related variables
        ramp = 1
        valMin = 0
        step = 1
        testSig = []

        # Initialisong mode dependent variables
        if (mod == 'amplitude'):
            ka = 0
            kx = 0.1
        
        if (mod == 'phase'):
            ka = np.pi/18
            kx = 0
            
        # Calculation the current step with respect to the ramp and calculating the test signal
        for i in range(ptTimeTest):
            if(timeTestArray[i]-valMin >= 2):
                valMin = timeTestArray[i]
                if(step == stepMax or step == stepMin):
                    ramp *= -1
                step += ramp
            testSig.append(Xm*(1+kx*step)*np.sin(omega0*timeTestArray[i]+ka*step))
        
        # Creating the final path for the file        
        path = os.path.join(rootPath,case)
        if not os.path.exists(path):
            os.mkdir(path)
        path = os.path.join(path,'%s_SC_%s.csv' %(case,mod))
        
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
            timeCounter += timeNomWait

            for i in range(ptTimeTest):
                writer.writerow([timeTestArray[i]+timeCounter,testSig[i]])
            timeCounter += timeTest

            for i in range(ptTimeNomWait):
                writer.writerow([timeNomWaitArray[i]+timeCounter,nomSig[i]])
            timeCounter += timeNomWait

            for i in range(ptTimeNomWait):
                writer.writerow([timeNomWaitArray[i]+timeCounter,0])