import rospy
import message_filters
from sensor_msgs.msg import Image, CameraInfo

def sync(image, camera_info):
    global pub_im
    global pub_info
    pub_im.publish(image)
    pub_info.publish(camera_info)

if __name__ == '__main__':
    try:
        pub_im = rospy.Publisher('/camera_sync/image', Image, queue_size=1)
        pub_info = rospy.Publisher('/camera_sync/camera_info', CameraInfo, queue_size=1)
        image_sub = message_filters.Subscriber('/camera/image', Image)
        info_sub = message_filters.Subscriber('/camera/camera_info', CameraInfo)
        rospy.init_node('camera_sync')
        ts = message_filters.TimeSynchronizer([image_sub, info_sub], 10)
        ts.registerCallback(sync)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass


