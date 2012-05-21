from HTMLParser import HTMLParser
from urllib2 import urlopen

WHOISHOST = 'http://webwhois.nic.uk/cgi-bin/webwhois.cgi?wvw7yesk=3hryr4hby3&wquery='

# create a subclass and override the handler methods
class MyParser(HTMLParser):

    def __init__(self, url):
        self.stack = []
        HTMLParser.__init__(self)
        req = urlopen(url)
        self.feed(req.read())

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'pre':
            return tag

    def handle_data(self, data): 
        self.stack.append(data) 

class WhoisLookup(object):
    def __init__(self, url):
        self.url = WHOISHOST + url
        p = MyParser(self.url)
        self.raw_data = self.clean_data(p.stack)
        self.domain = self.get_domain(self.raw_data).strip()
        self.registrant = self.get_registrant(self.raw_data).strip()
        self.registrant_type = self.get_registrant_type(self.raw_data).strip()
        """
        self.registrant_address = 
        self.registrar = 
        self.relevent_dates = 
        self.registered_on = 
        self.expiry_date = 
        self.last_updated = 
        self.registration_status = 
        self.nameservers = 
        self.lookup_time = 
        """
    
    def f(self, x):
        if x == '':
            pass
        if x == ' ':
            pass
        else:
            return x

    def clean_data(self, data):
        data1 = ''.join(data)
        data2 = data1.split('\n')
        data3 = [line.replace('\r','') for line in data2]
        data4 = filter(self.f, data3)
        return data4

    def get_domain(self, data):
        iterdata = iter(data)
        for line in iterdata:
            if 'Domain name' in line:
                return iterdata.next()
        return "Domain not found"

    def get_registrant(self, data):
        iterdata = iter(data)
        for line in iterdata:
            if 'Registrant' in line:
                return iterdata.next()
        return "Registrant not found"        

    def get_registrant_type(self, data):
        iterdata = iter(data)
        for line in iterdata:
            if 'Registrant type' in line:
                return iterdata.next()
        return "Registrant type not found"        

