# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
import subprocess # bu modül ile linux komutları çalıştırabilirsin.

subprocess.call(["ifconfig","wlan0","down"])
subprocess.call(["ifconfig","wlan0","hw","ether","00:55:44:33:22:11"])
subprocess.call(["ifconfig","wlan0","up"])
