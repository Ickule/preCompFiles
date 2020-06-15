import csv
import numpy as np
import os

# Setting all the diferent cases that need to be taken into account for file genreration
cases=['P_class','M_class']

# Initialisong fundamental related variables and fixed variables
omega0 = 50*2*np.pi
Xm = 230
harmAmp = 0.1
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
rootPath = os.path.join(cwd,'Harmonics')
if not os.path.exists(rootPath):
    os.mkdir(rootPath)

for case in cases:
   
    for n in range(1,11):

        print('Working on %iHz for %s'%(n*50,case))
        
        # initialising a time counter to reuse nominal signal value and test signal value at diferent time offsets
        timeCounter = 0
 
        # Computing test signal
        testSig = Xm*(np.sin(omega0*timeTestArray)+harmAmp*np.sin(n*omega0*timeTestArray))
   
        # Creating the final path for the file
        path = os.path.join(rootPath,case)
        if not os.path.exists(path):
            os.mkdir(path)
        path = os.path.join(path,'%s_Harmonics_%iHz.csv' %(case,n*50))
        
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