# Bluetooth Simple Denial Of Service (DoS)

## Legal Note
*This project is made only for educational purposes and for helping in Proofs of Concept. The author does not encourage anyone to use it illegally or without permission of your noisy neighbours ;).*

## Description
This is a simple script for looping a Denial Of Service attack over one single mac address in range. If Mac address is down or not in range, it will keep trying to attack the target until user press CTRL+C.

  **WARNING: It only works on Linux systems because it depends on *l2ping* tool**

## Dependencies

  - [BlueZ package](http://www.bluez.org/)
  - [L2Ping](https://linux.die.net/man/1/l2ping)
  - [Python3](https://www.python.org/downloads/)
  - A Bluetooth Dongle/Card

## Installation
```
$ sudo apt update
$ sudo apt install -y python3 bluez* hcitool
$ git clone https://github.com/w1s3m4n/BluetoothSimpleDoS.git
$ cd BluetoothSimpleDoS/
```

## Execution
1. Scan for mac address using **bluetoothctl** (better than hcitool)
```
$ bluetoothctl
$ [bluetoothctl] scan on
$ [bluetoothctl] scan off (when found)
$ [bluetoothctl] exit
```

Copy the **device MAC Address**

2. Execute script

For modern devices it is recommended to use a huge number of threads: (ex: 900)
```
$ sudo python3 BluetoothSimpleDoS.py -h
usage: BluetoothSimpleDoS.py [-h] [-t THREADS] [-p PACKETSIZE] [-v] MAC

Simple script for create a continuos denial of service attack over one bluetooth target

positional arguments:
  MAC                   Target's MAC Address

optional arguments:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        Number of threads
  -p PACKETSIZE, --packetsize PACKETSIZE
                        Packet size (default: 650)
  -v, --verbose         Verbose

```
## Tools and conditions

- Attacker OS: [Kali Linux 2021 ARM](https://www.kali.org/get-kali/)
- Target Device: [Marshall Bluetooth Speaker](https://www.marshallheadphones.com/gb/en/stanmore-ii-bluetooth.html)
- Bluetooth Card: [SENA UD100](http://www.senanetworks.com/ud100-g03.html)


## Expected behaviour 
When performing proof of concept attack, the speaker started to be interfered and the listening of music turned impossible.

Other devices may turn off or block or don't be interfered at all.

##### Credits: W1s3m4n