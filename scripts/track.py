#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseArray, Twist

time_last_pose = 0
accumulator = 0
last_offset = 0

def pose_callback(data):
    if len(data.poses) > 0:
        print(data.poses[0])
	turn_towards(data.poses[0].position.x)

def turn_control(offset_x):
    global t
    global time_last_pose
    global last_offset
    global accumulator
    time_last_pose = rospy.get_time()
    k_p = -1
    k_i = 0
    k_d = 0
    t.angular.z = k_p * offset_x + k_i * accumulator + k_d * (offset_x - last_offset)
    #print(t)

def clear_twist():
    global t
    print('clearing twist')
    t = Twist()

    
def main():
    global t
    global time_last_pose
    t = Twist()
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
    rospy.init_node('tag_tracker', anonymous=True)
    rospy.Subscriber("/tag_detections_pose", PoseArray, pose_callback)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        if rospy.get_time() - time_last_pose > 2:
            clear_twist()
        pub.publish(t)
        rate.sleep()
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
