import numpy as np
import glob
import csv
import sys

csvList=glob.glob("**/*.csv",recursive=True)

if (len(sys.argv) == 1):
    mean = 0
    std = 1
if (len(sys.argv) == 2):
    mean = sys.argv[1]
    std = 1
if (len(sys.argv) >= 3):
    mean = sys.argv[1]
    std = sys.argv[2]

for filePath in csvList:
    if not (filePath[-10:] == "_noise.csv"):
        with open(filePath, "r") as csvFile:
            print("Reading %s" %filePath)
            csvRead = csv.reader(csvFile, delimiter=',')
            firstRow = next(csvRead)
            time = []
            signal = []
            for row in csvRead:
                time.append(float(row[0]))
                signal.append(float(row[1]))
                
        sampling = int(len(time)/time[-1])
        ptTimeNomWait = 5*sampling+1     
        
        noiseFilePath = filePath[:-4]+"_noise"+filePath[-4:]
        with open(noiseFilePath, "w", newline='', encoding='utf-8') as csvNoiseFile:
            print("Writing %s" %noiseFilePath)
            writer = csv.writer(csvNoiseFile)
            writer.writerow(firstRow)
            for i in range(len(time)):
                if (ptTimeNomWait <= i and i <= len(time)-ptTimeNomWait-1):
                    writer.writerow([time[i],signal[i]+np.random.normal(mean, std)])
                else:
                    writer.writerow([time[i],signal[i]])
print("Done!")