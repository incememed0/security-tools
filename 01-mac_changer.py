# author: Ercan Atar
# linkedin.com/in/ercanatar/
#######################################################
import subprocess # bu modül ile linux komutları çalıştırabilirsin.
import optparse # help dökümanlarını oluşturmanı sağlıyor.
import re # çıktı içerisinde aradığımız ifadeyi çekip almamızı sağlıyor

def get_user_input():
	parse_object=optparse.OptionParser()
	parse_object.add_option("-i","--interface",dest="interface",help="interface to change")
	parse_object.add_option("-m","--mac",dest="mac_address",help="new mac adres")
	return parse_object.parse_args()

def change_mac_address(interface,mac_address):
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
	subprocess.call(["ifconfig",interface,"up"])

def control_new_mac(interface):
	ifconfig=subprocess.check_output(["ifconfig",interface]) # aldığımız çıktıyı ifconfig adındaki değişkene eşitliyoruz.
	new_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig)) # r"bu ifadeleri regex101.com'dan öğreniyoruz"
	if new_mac:
		return new_mac.group(0)
	else:
		return None


print("program running...")
(user_input,arguments)=get_user_input()
change_mac_address(user_input.interface,user_input.mac_address)
finalized_mac=control_new_mac(str(user_input.interface))

if finalized_mac == user_input.mac_address:
	print("başarılı")
else:
	print("hata!")


#-------2.kod-----------#
#import subprocess # bu modül ile linux komutları çalıştırabilirsin.
#import optparse # help dökümanlarını oluşturmanı sağlıyor.

#def get_user_input():
#	parse_object=optparse.OptionParser()
#	parse_object.add_option("-i","--interface",dest="interface",help="interface to change")
#	parse_object.add_option("-m","--mac",dest="mac_address",help="new mac adres")
#	return parse_object.parse_args()

#def change_mac_address(interface,mac_address):
#	subprocess.call(["ifconfig",interface,"down"])
#	subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
#	subprocess.call(["ifconfig",interface,"up"])

#print("program running...")
#(user_input,arguments)=get_user_input()
#change_mac_address(user_input.interface,user_input.mac_address)



#------- ilk kod --------#
#import subprocess
#import optparse

#parse_object=optparse.OptionParser()
#parse_object.add_option("-i","--interface",dest="interface",help="interface to change")
#parse_object.add_option("-m","--mac",dest="mac_adress",help="new mac adres")

#(user_inputs,arguments)=parse_object.parse_args()
#interface=user_inputs.interface
#mac_address=user_inputs.mac_adress

#subprocess.call(["ifconfig",interface,"down"])
#subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
#subprocess.call(["ifconfig",interface,"up"])

#-------------------------#
