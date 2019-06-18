#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np
import matplotlib.pyplot as plt
from walabot.msg import distanceTravelled
import message_filters

y = []
z = []
dist = []
i = 0


# def callback(rawSignaldata, distanceTravelleddata):
def callback(data):
    global y,z,dist,i
    # convert amplitude value into array for computing
    raw = data.amplitude
    # dist = distanceTravelleddata.distance
    # print raw
    # print dist
    rawAmp = raw[0:2000]
    # updating list for plotting
    # y.append(xdistance()) 
    z.append(rawAmp)
    dist.append(i)
    # inverting amplitude value to get a vertical plot
    z = zip(*z)
    y_min, y_max = np.asarray(z).min(), np.asarray(z).max()
    # Plotting raw signal
    if i==0:
        plt.figure(figsize=(15,15))
    plt.clf()
    plt.ylim(2000,0)
    plt.xlim(0,50)
    plt.pcolormesh(z,cmap = 'gist_gray',vmin=y_min, vmax=y_max) #xticklabels = y)
    plt.title('Bscan')
    plt.ylabel('Number of sample data')
    plt.xlabel('Mock distance Travelled')
    plt.xticks(np.arange(len(dist)),dist)#rotation = 90)
    # plt.autoscale(enable=True,axis='both',tight=True)
    plt.draw()
    plt.pause(0.0000001)
    plt.show()
    z = zip(*z)
    print (len(z))
    i = i + 0.01
    if len(z)==50:
        i = "shutdown"
        plt.savefig('WalabotBscan.pdf',bbox_inches='tight')
        rospy.signal_shutdown(i)
        
if __name__ == '__main__':
    rospy.init_node('processBscan', anonymous=True)
    plt.ion()
    # rawSignaldata = message_filters.Subscriber("rawSignal", signal)
    # distanceTurtleTravdata = message_filters.Subscriber('distanceTravelled',distanceTravelled)
    # ts = message_filters.ApproximateTimeSynchronizer([rawSignaldata, distanceTurtleTravdata],10,0.1)
    # ts.registerCallback(callback)
    rospy.Subscriber("rawSignal",signal,callback)
    rospy.spin()