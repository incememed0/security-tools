# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
# mitm işlemine başlamadan önce terminal ekranında;
# " echo 1 > /proc/sys/net/ipv4/ip_forward " bu komutu çalıştırmanız gerekmektedir.

import scapy.all as scapy



arp_response=scapy.ARP()

