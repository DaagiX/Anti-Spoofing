from python_arptable import get_arp_table
from scapy.all import Ether,ARP,srp
import time

try:  
	ip_target =input("\nEnter Target IP>> ")
	mac_addr = ''
	
	while True:
		thisset = get_arp_table()
		for x in thisset:
			if x['IP address'] == ip_target:
				#print("This is Target MAC  : ",x['HW address'])
				print("\n")
				mac_addr = x['HW address']
		
			
		if mac_addr == '':
			print("IP Not Found")
			break
		else:
			print("Let Check ..")
			print("*.*.*.*.*.*.")

			ether_header = Ether(dst="FF:FF:FF:FF:FF:FF")
			
			arp_option = ARP(pdst=ip_target)

			arp_packet = ether_header / arp_option

			result , noresult = srp(arp_packet,timeout=2)

			for send , recive in result:
			    
			    new_mac_addr = recive[Ether].hwsrc
			
			if mac_addr == new_mac_addr:
				print("\n\t\t\t-- -- -- -- -- -- ")
				print("\t\t\t--+--You Safe--+--")
				print("\t\t\t-Next Check  Soon-")
				print("\t\t\t-- -- -- -- -- -- \n")
				time.sleep(10)
				continue
				
			else:
				print("\n----+++--+--ATTENTION--+--+++------")
				print("\nWARNING !! Someone .. Attack You !!\n")
				print("----+++--+--ATTENTION--+--+++------\n")
				break

except Exception:
	print("\n+++try again +++")
	