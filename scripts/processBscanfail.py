#!/usr/bin/env python
import rospy
from walabot.msg import signal
import numpy as np
import matplotlib.pyplot as plt
from nav_msgs.msg import Odometry
from std_msgs.msg import String
import message_filters
import math

# y = []
# z = []
# dist = []
# i = 0

# def callback(rawSignaldata, distanceTravelleddata):
def callback(chatter,yo):
    # global y,z,dist,i
    # convert amplitude value into array for computing
    # raw = rawSignaldata.amplitude
    raw = chatter.data
    distraw = yo.data
    # raw = raw[0:2000]
    # updating list for plotting
    # z.append(rawAmp)
    # dist = list(distraw)
    rospy.loginfo(raw)
    rospy.loginfo(distraw)
    # print(type(distraw))
    # inverting amplitude value to get a vertical plot
    # z = zip(*z)
    # y_min, y_max = np.asarray(z).min(), np.asarray(z).max()
    # # Plotting raw signal
    # if i==0:
    #     plt.figure(figsize=(15,8))
    #     i = i + 1
    # plt.clf()
    # plt.ylim(2000,0)
    # plt.xlim(0,50)
    # plt.pcolormesh(z,cmap = 'gist_gray',vmin=y_min, vmax=y_max)
    # plt.title('Bscan')
    # plt.ylabel('Number of sample data')
    # plt.xlabel('Mock distance Travelled')
    # plt.xticks(np.arange(len(dist)),dist,rotation = 45)
    # plt.draw()
    # plt.pause(0.0000001)
    # plt.show()
    # z = zip(*z)
    # print (len(z))
    # if len(z)==50:
    #     shutcommand = "shutdown"
    #     plt.savefig('WalabotBscan.pdf',bbox_inches='tight')
    #     rospy.signal_shutdown(shutcommand)
    # # clear for new list
    # dist = []
        
if __name__ == '__main__':
    rospy.init_node('processBscan', anonymous=True)
    # plt.ion()
    rawSignaldata = message_filters.Subscriber('chatter', String)
    distanceTurtleTravdata = message_filters.Subscriber('yo',String)
    ts = message_filters.ApproximateTimeSynchronizer([rawSignaldata, distanceTurtleTravdata],10,0.1,allow_headerless = True)
    ts.registerCallback(callback)
    # distanceTurtleTravdata = rospy.Subscriber('odom',Odometry,callback)
    rospy.spin()