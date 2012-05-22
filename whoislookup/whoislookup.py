from HTMLParser import HTMLParser
from urllib2 import urlopen, URLError
import socket

WHOISHOST = 'http://webwhois.nic.uk/cgi-bin/webwhois.cgi?wvw7yesk=3hryr4hby3&wquery='

# create a subclass and override the handler methods
class MyParser(HTMLParser):

    def __init__(self, url):
        self.stack = []
        HTMLParser.__init__(self)
        try:
            req = urlopen(url)
            self.feed(req.read())
        except URLError:
            print "No Internet Connection"

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'pre':
            return tag

    def handle_data(self, data): 
        self.stack.append(data) 

class WhoisLookup(object):
    def __init__(self, url):
        self.__url = WHOISHOST + url
        p = MyParser(self.__url)
        self.raw_output = ''
        if p.stack:
            self.data = self.__clean_data(p.stack)
            self.domain = self.__get_domain()
            self.registrant = self.__get_registrant()
            self.registrant_type = self.__get_registrant_type()
            self.registrant_address = self.__get_registrant_address()
            self.registrar = self.__get_registrar()
            self.relevent_dates = self.__get_relevent_dates()
            self.registered_on = self.__get_registered_on()
            self.expiry_date = self.__get_expiry_date()
            self.last_updated = self.__get_last_updated()
            self.registration_status = self.__get_registration_status()
            self.nameservers = self.__get_nameservers()
            self.lookup_time = self.__get_lookup_time()
        else:
            print 'Raw output is empty'
    
    def __f(self, x):
        if x == '':
            pass
        if x == ' ':
            pass
        else:
            return x

    def __slice_boundary(self, value):
        for k, v in enumerate(self.data):
            if value in v:
                return k

    def __clean_data(self, data):
        data1 = ''.join(data)
        data2 = data1.split('\n')
        data3 = [line.replace('\r','') for line in data2]
        data4 = filter(self.__f, data3)
        self.raw_output = data4
        data = [line.strip() for line in data4]
        return data

    def __get_domain(self):
        return self.data[self.__slice_boundary('Domain name:') + 1 : self.__slice_boundary('Registrant:')]

    def __get_registrant(self):
        return self.data[self.__slice_boundary('Registrant:') + 1 : self.__slice_boundary('Registrant type:')]
        
    def __get_registrant_type(self):
        return self.data[self.__slice_boundary('Registrant type:') + 1 : self.__slice_boundary("Registrant's address:")]

    def __get_registrant_address(self):
        return self.data[self.__slice_boundary("Registrant's address:") + 1 : self.__slice_boundary('Registrar:')]

    def __get_registrar(self):
        return self.data[self.__slice_boundary("Registrar") + 1 : self.__slice_boundary('Relevant dates:')]

    def __get_relevent_dates(self):
        return self.data[self.__slice_boundary("Relevant dates:") + 1 : self.__slice_boundary('Registration status:')]

    def __get_registered_on(self):
        r = self.data[self.__slice_boundary("Registered on:") : self.__slice_boundary("Registered on:") + 1]
        return r[0].split(':')[1].strip()

    def __get_expiry_date(self):
        r = self.data[self.__slice_boundary("Expiry date:") : self.__slice_boundary("Expiry date:") + 1]
        return r[0].split(':')[1].strip()

    def __get_last_updated(self):
        r = self.data[self.__slice_boundary("Last updated:") : self.__slice_boundary("Last updated:") + 1]
        return r[0].split(':')[1].strip()

    def __get_registration_status(self):
        return self.data[self.__slice_boundary("Registration status:") + 1 : self.__slice_boundary('Name servers:')]

    def __get_nameservers(self):
        return self.data[self.__slice_boundary("Name servers:") + 1 : self.__slice_boundary('WHOIS lookup made at')]

    def __get_lookup_time(self):
        r = self.data[self.__slice_boundary("WHOIS lookup made at") : self.__slice_boundary("WHOIS lookup made at") + 1]
        return r[0].split('at')[1].strip()
