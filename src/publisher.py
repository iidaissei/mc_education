#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------
#Title: トピックを配布するサンプルROSノード
#Author: Issei Iida
#Date: 2019/09/29
#Memo: 数字を1〜100まで配布する
#--------------------------------------------------------------------

# ROS関係ライブラリ
import rospy
from std_msgs.msg import String


class PublishClass():
    def __init__(self):
        # 第一引数:トピック名 第二引数:メッセージ型名 第三引数:キューサイズ(1でOK）
        self.pub_message = rospy.Publisher('/sample_topic', String, queue_size = 1)
        self.count = 1

    def publishMessage(self):
        while not rospy.is_shutdown() and self.count <= 100:
            data = str(self.count)# <--- str型に変換
            rospy.loginfo('Publish message: ' + data)
            rospy.sleep(1.0)
            self.pub_message.publish(data)# <--- ここでトピックを配布している
            self.count += 1
        return 1


def main():
    # "rospy.loginfo"とはROSオリジナルのprintみたいなもの。
    rospy.loginfo('Start "ex_publisher"')
    pc = PublishClass()
    state = 0
    while not rospy.is_shutdown():
        state = pc.publishMessage()
        if state == 1:
            rospy.loginfo('Finish ex_publisher')
            break
        else:
            pass

if __name__ == '__main__':
    # ノードの初期化をする。第一引数はノード名
    rospy.init_node('ex_publisher')
    main()
