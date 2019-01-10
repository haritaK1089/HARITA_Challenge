###############################################################################################
##Title: Python program to check whether given https server is up and running
##Author: Harita.K
##Python Version: 3.6.2
#################################################################################################
import argparse  #This module helps to take command line arguments efficiently
import sys #This module can fetch all the arguments entered in the command line
import getopt # This module helps to accept command line arguments in unix format
import http.client # The module used to connect to http server

def http_service(ip,pn):
    try:
        conn = http.client.HTTPConnection(ip,pn,timeout=15)
        conn.request("GET","/")
        r1 = conn.getresponse()
        print(r1.status, r1.reason)
        if((r1.status == 200) and (r1.reason == "OK")):
            print("connected to",ip)
            conn.close()
            return(r1.status, r1.reason)
        else:
            print("cannot connect to",ip)
            conn.close()
            return(r1.status, r1.reason)

    except (http.client.HTTPException) as http_err:
        print("Error in http address or port number")
        print(http_err)
        conn.close()
        return (http_err)
def https_service(ip,pn):
    try:
        conn = http.client.HTTPSConnection(ip,pn,timeout=10)
        conn.request("GET","/")
        r1 = conn.getresponse()
        print(r1.status, r1.reason)
        if((r1.status == 200) and (r1.reason == "OK")):
            print("connected to",ip)
            conn.close()
            return(r1.status, r1.reason)
        else:
            print("cannot connect to",ip)
            conn.close()
            return(r1.status, r1.reason)

    except (http.client.HTTPException) as https_err:
        print("Error in http address or port number")
        conn.close()
        return (https_err)

def arg1_check(serv_type):
    if((serv_type=='http') or (serv_type=='https')):
        print("http service")
        parser=argparse.ArgumentParser()
        parser.add_argument("service_type", help="Enter valid service type. Ex http or https")
        parser.add_argument("IPaddress", help="give the complete server address, Ex www.abc.com")
        parser.add_argument("PortNumber", type=int, help="Enter valid port number http:80, https:443")
        args= parser.parse_args()
        ip = args.IPaddress
        pn = args.PortNumber
        if(args.PortNumber==80):
            http_service(ip,pn)
        elif(args.PortNumber==443):
            https_service(ip,pn)
        return serv_type
    
    else:
        print("This program only verifies http, https request")
        return serv_type
