from scapy.all import IP, sniff
from scapy.layers import http
from termcolor import colored
import sys
def banner():
    print("""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmdddhhhhhhhhhdddmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNmdhyyyyyyyyyyyyyyyyyyyyyyyhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNdhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNdhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMmhyyyyyyyyyyyyyyyyyyyyyyyyyhhddddddddddhhyyyyyyhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMNdyyyyyyyyyyyyyyyyyyyyyyhdmmNMMMMMMMMMMMMMMMMNmmdhyyydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMdyyyyyyyyyyyyyyyyyyyyydmNMMMMMMMMMMMMMMMMMMMMMMMMMMNmdyydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMmhyyyyyyyyyyyyyyyyyyydmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMdyyyyyyyyyyyyyyyyyyydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNddMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMNhyyyyyyyyyyyyyyyyyydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMNhyyyyyyyyyyyyyyyyyhNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMNhyyyyyyyyyyyyyyyyydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmMMMMMMMMMMMMMMMMMMM
MMMhyyyyyyyyyyyyyyyyymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdhNMMMMMMMMMMMMMMMMM
MMdyyyyyyyyyyyyyyyyymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdyhmMMMMMMMMMMMMMMMM
MNyyyyyyyyyyyyyyyyymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdyyydMMMMMMMMMMMMMNN
MhyyyyyyyyyyyyyyyyhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdyyyyhNMMMMMMNmdhhdM
NyyyyyyyyyyyyyyyyyNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdyyyyyymmdhhyyyyhNMM
myyyyyyyyyyyyyyyyhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdyyyyyyyyyyyyyydMMMM
dyyyyyyyyyyyyyyyydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmddhyyyyyyyyyyyyyymMMMMM
hyyyyyyyyyyyyyyyydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdhhyyyyyyyyyyyyyyyyyyhNMMMMMM
hyyyyyyyyyyyyyyyydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmdhyyyyyyyyyyyyyyyyyyhNMMMMMM
dyyyyyyyyyyyyyyyydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmdhyyyyyyyyyyyyyymMMMMM
myyyyyyyyyyyyyyyyhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdyyyyyyyyyyyyyydMMMM
NyyyyyyyyyyyyyyyyyNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdyyyyyhmmddhyyyyhNMM
MhyyyyyyyyyyyyyyyyhMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdyyyyhNMMMMMMNmdhydM
MNyyyyyyyyyyyyyyyyydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMhyyymMMMMMMMMMMMMMNN
MMdyyyyyyyyyyyyyyyyymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMhyhNMMMMMMMMMMMMMMMM
MMMhyyyyyyyyyyyyyyyyymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMhdMMMMMMMMMMMMMMMMMM
MMMNhyyyyyyyyyyyyyyyyydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMM
MMMMNhyyyyyyyyyyyyyyyyyhNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMNhyyyyyyyyyyyyyyyyyydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMdyyyyyyyyyyyyyyyyyyydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNddMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMmhyyyyyyyyyyyyyyyyyyyhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMdyyyyyyyyyyyyyyyyyyyyyhmNMMMMMMMMMMMMMMMMMMMMMMMMMMNmhyydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMNdyyyyyyyyyyyyyyyyyyyyyyyhdmNMMMMMMMMMMMMMMMMNmdhyyyydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMmhyyyyyyyyyyyyyyyyyyyyyyyyyyhhddddddddhhyyyyyyyhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNdyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNdhyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMmddhyyyyyyyyyyyyyyyyyyyyyyyhhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmddhhhhhhhhhhhddmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    
====================================================================================================
                                    Coder By : Axroix
                                    Program name : Ayy??ld??z
    """)
def tcp_ayikla(paket):
    if not paket.haslayer(http.HTTPRequest):
        return
    http_katmani = paket.getlayer(http.HTTPRequest)
    ip_katmani = paket.getlayer(IP)
    print(('\n{0[src]} IP adresinden {1[Method]} Methoduyla {1[Host]}{1[Path]} sitesine ziyaret').format(ip_katmani.fields, http_katmani.fields))
    devam = input()
    if (devam == "q"):
        for i in range(1,100,1):
            print(i)
        sys.exit()
    else:
        print("#")
banner()
sniff(filter='tcp', prn=tcp_ayikla)
