#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------
#Title: トピックを購読するためのサンプルROSノード
#Author: Issei Iida
#Date: 2019/09/29
#Memo: トピック"/sample_topic"を購読して、数字が5の時ノード終了
#--------------------------------------------------------------------

# ROS関連ライブラリ
import rospy
from std_msgs.msg import String


class SubscriberClass():
    def __init__(self):
        # Subscriber
        # 第一引数:トピック名 第二引数:メッセージ形名 第三引数:コールバック関数名（受け取る関数のこと）
        self.sub_message = rospy.Subscriber('/sample_topic', String, self.messageCB)
        self.data = 'none'

    def messageCB(self, receive_msg):# <--- このメソッド（関数）でトピックを受け取る
        # .dataとはトピック'/sample_topic'のメッセージの階層のこと。
        self.data = receive_msg.data

    def printMessage(self):
        while not rospy.is_shutdown():
            if self.data == '5':
                rospy.loginfo('Subscribe 5')
                return 1 
            else:
                pass


def main():
    rospy.loginfo('Start "ex_subscriber"')
    sc = SubscriberClass()
    state = 0
    while not rospy.is_shutdown():
        state = sc.printMessage()
        if state == 1:
            rospy.loginfo('Finish "ex_subscriber"')
            break
        else:
            pass

if __name__ == '__main__':
    rospy.init_node('ex_subscriber')
    main()
