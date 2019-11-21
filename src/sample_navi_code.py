######################################################################
#アクションクライアントの例
######################################################################

#必要なインポート君たち
import actionlib
from  move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_srvs.srv import Empty

#コード例
def navigationAC(coord_list):
    try:
        rospy.loginfo("Start Navigation")
        ac = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        ac.wait_for_server()
        #CostmapService
        clear_costmaps = rospy.ServiceProxy('move_base/clear_costmaps', Empty)
        #Set Goal
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = coord_list[0]
        goal.target_pose.pose.position.y = coord_list[1]
        goal.target_pose.pose.orientation.z = coord_list[2]
        goal.target_pose.pose.orientation.w = coord_list[3]
        #Costmapを消去
        rospy.wait_for_service('move_base/clear_costmaps')
        clear_costmaps()
        rospy.sleep(1.0)
        #Goalを送信
        ac.send_goal(goal)
        state = ac.get_state()
        count = 0#<---clear_costmapsの実行回数をカウントするための変数
        while not rospy.is_shutdown():
            state = ac.get_state()
            if state == 1:
                rospy.loginfo('Got out of the obstacle')
                rospy.sleep(1.0)
            elif state == 3:
                rospy.loginfo('Navigation success!!')
                return 'success'
                state = 0
            elif state == 4:
                if count == 100:
                    count = 0
                    rospy.loginfo('Navigation Failed')
                    return 'failed'
                else:
                    rospy.loginfo('Buried in obstacle')
                    clear_costmaps()
                    rospy.loginfo('Clear Costmaps')
                    ac.send_goal(goal)
                    rospy.loginfo('Send Goal')
                    rospy.sleep(1.0)
                    count += 1
    except rospy.ROSInterruptException:
        pass


######################################################################
#場所の座標をパラメータから読み込む部分
######################################################################

#必要なインポート君たち
import sys
from yaml import load

#コード例
#文字列をパラメータの/location_dictから検索して位置座標を返す
def searchLocationName(target_name):
    rospy.loginfo("Search LocationName")
    #location_dictのyamlファイルを読み込む
    f = open('/home/issei/catkin_ws/src/mimi_common_pkg/config/location_dict.yaml')
    location_dict = load(f)
    f.close()
    if target_name in location_dict:
        print location_dict[target_name]
        rospy.loginfo("Retrun location_dict")
        return location_dict[target_name]
    else:
        rospy.loginfo("Not found <" + target_name + "> in location_dict")
        return 'faild'
