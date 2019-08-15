#!/usr/bin/env python 
import Tkinter as tk

import rospy
from std_srvs.srv import Empty

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        rospy.wait_for_service('open')
        self.s_open = rospy.ServiceProxy('open', Empty)
        rospy.wait_for_service('close')
        self.s_close = rospy.ServiceProxy('close', Empty)
        rospy.wait_for_service('start')
        self.s_start = rospy.ServiceProxy('start', Empty)
        rospy.wait_for_service('stop')
        self.s_stop = rospy.ServiceProxy('stop', Empty)
        rospy.wait_for_service('fire_ball')
        self.s_fire = rospy.ServiceProxy('fire_ball', Empty)
        rospy.wait_for_service('fire_adv')
        self.s_adv_fire = rospy.ServiceProxy('fire_adv', Empty)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.closeButton = tk.Button(self, text='Close Launcher', command=self.close_launcher)
        self.closeButton.grid()
        self.openButton = tk.Button(self, text='Open Launcher', command=self.open_launcher)
        self.openButton.grid()
        self.startButton = tk.Button(self, text='Startup', command=self.startup)
        self.startButton.grid()
        self.stopButton = tk.Button(self, text='Stop', command=self.stop_all)
        self.stopButton.grid()
        self.fireButton = tk.Button(self, text='Fire', command=self.fire)
        self.fireButton.grid()
        self.fireButton = tk.Button(self, text='Fire (Adversarial)', command=self.adversarial_fire)
        self.fireButton.grid()

    def close_launcher(self):
        self.s_close()

    def open_launcher(self):
        self.s_open()

    def startup(self):
        self.s_start()

    def stop_all(self):
        self.s_stop()

    def fire(self):
        self.s_fire()

    def adversarial_fire(self):
        self.s_adv_fire()

if __name__ == "__main__":
    app = Application()
    app.master.title('Teleop Interface')
    app.mainloop()

