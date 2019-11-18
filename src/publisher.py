#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------
#Title: トピックを配布するためのサンプルROSノード
#Author: Issei Iida
#Date: 2019/09/29
#Memo: 数字を1〜10まで配布する
#--------------------------------------------------------------------

#ROS関係ライブラリ
import rospy
from std_msgs.msg import String


class PublishClass():
    def __init__(self):
        #第一引数:トピック名 第二引数:メッセージ型名 第三引数:キューサイズ(1でOK）
        self.pub_message = rospy.Publisher('/sample_topic', String, queue_size = 1)
        self.count = 1

    def publishMessage(self):
        while not rospy.is_shutdown() and self.count <= 10:
            data = str(self.count)
            rospy.loginfo('Publish message: ' + data)
            rospy.sleep(1.0)
            self.pub_message.publish(data)#<----ここでトピックを配布する
            self.count += 1
        return 1


def main():
    #"rospy.loginfo"とはROSオリジナルのprintみたいなもの。時間とか一緒に表示する。
    rospy.loginfo('Start "ex_publisher"')
    #"PublishClass"を"pc"としてインスタンス化
    pc = PublishClass()
    #状態遷移用の変数
    state = 0
    #"rospy.is_shutdown()"とは、Ctrl+Cされた時のこと。（この場合はCtrl+Cされるまでwhileされる仕様）
    while not rospy.is_shutdown():
        state = pc.publishMessage()
        if state == 1:
            rospy.loginfo('Finish "ex_publisher"')
            break
        else:
            pass

if __name__ == '__main__':
    #ノードの初期化をする。第一引数はノード名
    rospy.init_node('ex_publisher')
    main()
