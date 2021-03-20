#!/bin/bash
# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
ifconfig wlan0 down
ifconfig wlan0 hw ether 00:11:22:33:44:55
ifconfig wlan0 up
