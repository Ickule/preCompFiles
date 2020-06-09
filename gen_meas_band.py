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

# Initialisong fundamental related variables 
omega0 = 50*2*np.pi
Xm = 230

# Computing nominal signal
nomSig=Xm*np.sin(omega0*timeNomWaitArray)


# Creating the root path and directory for the files
cwd = os.getcwd()
rootPath = os.path.join(cwd,'Measurment Bandwidth')
if not os.path.exists(rootPath):
    os.mkdir(rootPath)
 
for case in cases:

    print('Working on %s'%(case))
    
    # Initialisong case dependent variables
    if (case == 'P_class'):
        freq = np.linspace(48,52,41)
        
    if (case == 'M_class'):
        freq = np.linspace(45,55,101)

    for mod in mods:
    
        print("Working on %s for %s" %(mod,case))
        
        # Initialisong mode dependent variables
        if (mod == 'amplitude'):
            ka = 0
            kx = 0.1
        
        if (mod == 'phase'):
            ka = 0.1
            kx = 0
        
        for f in freq:
        
            print("Working on %s modulation at %0.1fHz for %s" %(mod,f,case))

            # Computing test signal 
            omega = f*2*np.pi
            testSig = Xm*(1+kx*np.sin(omega*timeTestArray))*np.sin(omega0*timeTestArray+ka*np.sin(omega*timeTestArray-np.pi))
            
            # initialising a time counter to reuse nominal signal value and test signal value at diferent time offsets
            timeCounter = 0
            
            # Creating the final path for the file
            path = os.path.join(rootPath,case)
            if not os.path.exists(path):
                os.mkdir(path)
            path = os.path.join(path,'%s_MB_%s_%0.1fHz.csv' %(case,mod,f))

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