import csv
import os
import sys
import matplotlib.pyplot as plt

cwd = os.getcwd()
cwd = os.path.join(cwd,sys.argv[1])
with open(cwd, "r") as csvFile:
    csv_read = csv.reader(csvFile, delimiter=',')

    line_count = 0

    time = []
    twelve = []

    for row in csv_read:
        if line_count == 0:
            line_count += 1
        else:
            time.append(float(row[0]))
            twelve.append(float(row[1]))
            line_count += 1
    plt.title('Example signal')
    plt.plot(time[0:50001],twelve[0:50001],'r')
 
    i = 1
    start = 0
    stop = 50001
    while stop < 1850012:
        if i == 1:
            start = stop
            stop += 50001
            plt.plot(time[start:stop],twelve[start:stop],'g')
            i = 0
        else:
            start = stop
            stop += 300001
            plt.plot(time[start:stop],twelve[start:stop],'b')
            i = 1
    plt.plot(time[1850014:1900015],twelve[1850014:1900015],'r')
    
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
plt.show()

# for k in range(11):
    # with open("Harmonic_%i.csv" %k) as csv_file: 
        # csv_reader = csv.reader(csv_file, delimiter=',')
        
        # line_count = 0
        
        # time = []
        # twelve = []
        # #five = []
        # #tree = []

        # #time_12=2
        # #time_5=2
        # #time_3=2

        # for row in csv_reader:
            # if line_count == 0 or line_count == 1:
                # line_count += 1
            # else:
                # time.append(float(row[0]))
                # twelve.append(float(row[1]))
                # #five.append(float(row[2]))
                # #tree.append(float(row[3]))
                # line_count += 1

        # #while time_12 < len(twelve) and (twelve[time_12-1] >= thres12 or twelve[time_12-2] >= thres12 or twelve[time_12] >= thres12):
        # #    time_12+=1
        # #time_12-=2

        # #while time_5 < len(five) and (five[time_5-1] >= thres5 or five[time_5-2] >= thres5 or five[time_5] >= thres5):
        # #    time_5+=1
        # #time_5-=2

        # #while time_3 < len(tree) and (tree[time_3] >= thres3 or tree[time_3-2] >= thres3 or tree[time_3-1] >= thres3):
        # #    time_3+=1
        # #time_3-=2

        # #time_32=time_3
        # #while time_32 < len(tree) and (tree[time_32] >= thres32 or tree[time_32-2] >= thres32 or tree[time_32-1] >= thres32):
        # #    time_32+=1
        # #time_32-=2
        
        # #avg125.append(time[time_5]-time[time_12])
        # #delay125 = 'Delay 12/5 = %0.1fms' %(time[time_5]-time[time_12])
        # #avg123.append(time[time_3]-time[time_12])
        # #delay123 = 'Delay 12/3 = %0.2fms' %(time[time_3]-time[time_12])
        # #avg53.append(time[time_3]-time[time_5])
        # #delay53  = 'Delay 5/3   = %0.1fms' %(time[time_3]-time[time_5])
        # #avg32.append(time[time_32]-time[time_3])
        # #delay32  = 'threshold=%0.2fV' %thres3

        # #xy12='%0.1fms, %0.2fV' %((time[time_12]),(twelve[time_12]))
        # #xy5='%0.1fms, %0.2fV' %((time[time_5]),(five[time_5]))
        # #xy3='%0.1fms, %0.2fV' %((time[time_3]),(tree[time_3]))
        # #xy32='%0.1fms, %0.2fV' %((time[time_32]),(tree[time_32]))

        # plt.figure(k)

        # plt.plot(time,twelve)#,'r',label='12V,  threshold = %0.1fV' %thres12)
        # #plt.plot(time,five,'y',label='5V,    threshold = %0.1fV' %thres5)
        # #plt.plot(time,tree,'b',label='3.3V, threshold = %0.2fV' %thres3)

        # #plt.axvline(time[time_12],c='black',ls='--')#,label=delay125)
        # #plt.axvline(time[time_5],c='black',ls='--',label=delay123)
        # #plt.axvline(time[time_3],c='green',ls='--',label=delay123)
        # #plt.axvline(time[time_32],c='green',ls='--')#,label='threshold=%0.2fV' %thres32)
        
        # #plt.annotate(xy12,xy =(time[time_12],twelve[time_12]), xytext=(20,8),arrowprops=dict(arrowstyle="->",facecolor='black')) 
        # #plt.annotate(xy5,xy =(time[time_5],five[time_5]), xytext=(25,6),arrowprops=dict(arrowstyle="->",facecolor='black'))
        # #plt.annotate(xy3,xy =(time[time_3],tree[time_3]), xytext=(20,2.5),arrowprops=dict(arrowstyle="->",facecolor='black'))
        # #plt.annotate(xy32,xy =(time[time_32],tree[time_32]), xytext=(25,2),arrowprops=dict(arrowstyle="->",facecolor='black')) 
        # #plt.legend()
        # plt.xlabel('Time (s)')
        # plt.ylabel('Voltage (V)')
        # #plt.xlim(-10,50)
# #print('Average 12V to 5V delay = %0.1fms' %(sum(avg125)/len(avg125)))
# #print('Average 12V to 3V delay = %0.1fms' %(sum(avg123)/len(avg123)))
# #print('Average 5V to 3V delay = %0.1fms' %(sum(avg53)/len(avg53)))
# #print('Average %0.1fV to %0.2fV decay delay = %0.1fms' %(thres12, thres3, (sum(avg123)/len(avg123))))
# #print("Average %0.1fV to %0.2fV decay delay with -25 margin = %0.1fms" %(thres12, thres3, (sum(avg123)/len(avg123)*0.75)))
# plt.show()

        




    
