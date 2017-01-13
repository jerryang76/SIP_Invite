# coding=utf-8
import socket

target_address = '05058945926'
target_host ='10.10.1.223'
target_port = 5060
source_address = 'test'
source_host = '10.10.1.123'
source_port = '5060'
#raw_input
sip_invite = ('INVITE sip:'+target_address+'@'+target_host+';user=phone SIP/2.0\r\n'
'Allow: INVITE,ACK,OPTIONS,BYE,CANCEL,INFO,PRACK,REFER,SUBSCRIBE,NOTIFY,UPDATE,SERVICE\r\n'
'Via: SIP/2.0/UDP '+source_host+':'+source_port+';branch=z9hG4bKd7436e21d8650617\r\n'
'From: ''"'+source_address+'"'' <sip:'+source_address+'@'+source_host+'>;tag=e5c7825d-828\r\n'
'To: <sip:'+target_address+'@'+target_host+';user=phone>\r\n'
'Call-ID: 1B1B-1269-000008288D21D2C1F16A-002@SipHost\r\n'
'CSeq: 2 INVITE\r\n'
'Contact: <sip:'+source_address+'@'+source_host+':'+source_port+'>\r\n'
'Expires:300\r\n'
'Max-Forwards:70\r\n'
'Remote-Party-ID: <sip:'+source_address+'@'+source_host+'>;party=calling;privacy=off;screen=yes\r\n'
'Supported: replaces\r\n'
'User-Agent: 122 12-3898-13074-1.4.2.252-OGC200W\r\n'
'Content-Type: application/sdp\r\n'
'Content-Length: 0\r\n\r\n'
)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(5.0)
client.bind (('0.0.0.0', 5060))
client.sendto(sip_invite,(target_host,target_port))
data, addr = client.recvfrom(4096)
# print data
if data.find('180') > 0:
	print '1Ringing'
	print data
else:
	client.sendto(sip_invite,(target_host,target_port))
	data, addr = client.recvfrom(4096)
	if data.find('180') > 0:
		print '2Ringing'
		print data
	else:
		print 'Invite fail'
		print data
# print 'END'
# print data