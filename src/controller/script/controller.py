#!/usr/bin/python
#stestftf
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction,FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint

def main() :
    rospy.init_node("controller_node")
    action_client = actionlib.SimpleActionClient("/arm_controller/follow_joint_trajectory",FollowJointTrajectoryAction)
    rospy.loginfo("menunggu server") #test koneksi ke server
    action_client.wait_for_server()
    rospy.loginfo("Terkoneksi ke server") #test koneksi ke server
    list_point =[]
    pt_1 = JointTrajectoryPoint ()
    pt_1.positions = [1.0] #posisi point
    pt_1.time_from_start = rospy.Duration(1) #waktu dari start satuan detik
    list_point.append(pt_1)
    pt_2 = JointTrajectoryPoint()
    pt_2.positions = [-1.0]
    pt_2.time_from_start = rospy.Duration(2)
    list_point.append(pt_2)
    traj  = FollowJointTrajectoryGoal () #membuat trajectory goal
    traj.trajectory.joint_names = ['wrist_2_joint'] #mendefinisikan trajectory nama point
    traj.trajectory.points = list_point #memanggil posisi yang sudah kita buat tadi
    action_client.send_goal(traj) #mengirimkan action client ke server
    rospy.loginfo("Menunggu result") #jika  belum mendapatkan hasil(masih mengunggu)
    action_client.wait_for_result()
    rospy.loginfo("%s",action_client.wait_for_result()) #jika sudah mendapatkan hasil diambil dari fungsi wait for result dan berupa string
    rospy.loginfo("Selesai mengeksekusi")

if __name__ == "__main__" :
    main()