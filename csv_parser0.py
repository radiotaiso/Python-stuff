# Libraries needed to install
# pip install python-dateutil
# pip install argparse

from dateutil import tz
import csv
import datetime
import struct
import pickle
import socket
import argparse
import sys


class LineParser:
    def __init__(self):
        # Arg parser use csc_parser.py -f /path/to/filename.csv
        self.parser = argparse.ArgumentParser(description="CSV to Graphite importer")
        self.parser.add_argument("-v", help="Individual column to extract",action="store", dest='value')
        self.parser.add_argument("-f", "--file", help="Path of the file to parse", action="store", dest='file', required=True)
        self.parser.add_argument("-we", help="Aserkate we",action="store_true")
        self.args = self.parser.parse_args()

        if len(sys.argv[1:])==0:
            self.parser.print_help()
            sys.exit(0)
        #e we, aserkate we
        if self.args.we:
            print ""
            print "imayin toda la pipol we xd"
            print ""

class ResultsParser:
    #Initialize connection to graphite server
    def __init__(self, csv_name):
        self._CARBON_SERVER = '172.20.90.23' #This is temporary hardcoded to aim Tchaikovsky
        self._CARBON_PORT = 2004
        self.f = open(csv_name,"rb")
        self.csv_reader = csv.reader(self.f)
        self.set_time()
        self.sock = socket.socket()
        try:
            self.sock.connect((self._CARBON_SERVER,self._CARBON_PORT))
        except:
            raise SystemExit("Couldn't connect to %(server)s on port %(port)d, is carbon-cache.py running?" % { 'server':self._CARBON_SERVER, 'port':self._CARBON_PORT })

    def parse_file(self):
        #All your headers are belong to us
        #Save each column title
        self.headers = self.csv_reader.next()
        self.list_dict = []
        for row in self.csv_reader:
	           self.list_dict.append(dict(zip(self.headers,row)))

    # Get all the dates and turn them into a date variable rather than string
    # This should be changed to something else before 03:14:07 UTC on Tuesday, 19 January 2038 when an epoch integer overflow will happen
    def get_values(self, key):
        self.payload = ([])
        for i in self.list_dict:
            loc_time = datetime.datetime.strptime(i['DateTime'], '%Y-%m-%d %H:%M:%S')
            self.payload.append(('ngrinder.run.{}'.format(key),
               ((self.time_conv(loc_time) - self.epoch).total_seconds(),
               i[key])))

    # Nice and neat packaging with pickle
    def package_data(self):
        self.package = pickle.dumps(self.payload, 1)
        self.header = struct.pack('!L', len(self.package))

    # Send package header and package body
    def send(self):
        self.sock.sendall(self.header)
        self.sock.sendall(self.package)

    # Converting time from America/Mexico_City to epoch
    def set_time(self):
        self.from_zone = tz.gettz('UTC')
        self.to_zone = tz.gettz('America/Mexico_City')
        self.epoch = datetime.datetime.utcfromtimestamp(0)
        self.epoch = self.epoch.replace(tzinfo=self.from_zone)

    # converting time from UTC to America/Mexico_City
    def time_conv(self, loc_time):
        loc_time = loc_time.replace(tzinfo=self.from_zone)
        return loc_time.astimezone(self.to_zone)


if __name__ == "__main__":
    arg = LineParser()
    pars = ResultsParser(arg.args.file)
    pars.parse_file()
    for i in pars.headers:
        pars.get_values(i)
        pars.package_data()
        pars.send()
