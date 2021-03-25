# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
import scapy.all as scapy
import optparse

# arp: Mac adresleri ile IP adreslerini eşleştirmede kullanılır
# 1)arp_request : arp paketi oluşturmak
# 2)broadcast : yayın yapma aşaması
# 3)response : Gelen cevabı alıp işlemek

def get_user_input():
	parse_object=optparse.OptionParser()
	parse_object.add_option("-i","--ipaddress",dest="ip_address",help="enter ip adres")
	(user_input,arguments)=parse_object.parse_args()

	if not user_input.ip_address:
		print("enter ip adddreessss!")
	return user_input

def scan_network(ip):
	arp_request_packet=scapy.ARP(pdst=ip)
	# scapy.ls(scapy.ARP()) Döküman hakkında bilgi alabilmek için kullanırız.

	broadcast_packet=scapy.Ether() # parantez içerisine ff:ff:ff:ff:ff:ff ekleyebilirsin. default olarak bu kayıtlı
	# scapy.ls(scapy.Ether()) Ether dökümanı hakkında bilgi

	combined_packet= broadcast_packet/arp_request_packet # 2 paket ifadesini teke indirgedik.
	(answered_list,unanswered_list)=scapy.srp(combined_packet,timeout=1) # srp() : sisteme paket yollanacak karşılığında bir cevap gelicek. eğer gelmezse onu yok sayıcak. 
	# sr() : sisteme paket yollanacak sistem cevap versede vermesede çıktı olarak vericek.
	answered_list.summary()

user_ip_address=get_user_input()
scan_network(user_ip_address.ip_address)
