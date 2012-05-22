py-whois-lookup
===============
A simple whois lookup script. This is still in beta so only UK domains works.

###[install]###
pip install whoislookup

###[allowed methods]###
-w.data                 w.last_updated         w.raw_output           w.registrant_address   w.registration_status
-w.domain               w.lookup_time          w.registered_on        w.registrant_type      w.relevent_dates
-w.expiry_date          w.nameservers          w.registrant           w.registrar 

###[usage]###
  In [1]: from whoislookup import WhoisLookup

  In [2]: w = WhoisLookup('facebook.co.uk')
  
  In [3]: w.domain
    
    Out[3]: ['facebook.co.uk']
  
  In [4]: w.nameservers
    
    Out[4]: 
    ['dns091.b.register.com',
    'dns209.c.register.com',
    'dns225.a.register.com',
    'dns249.d.register.com']
  
  In [5]: w.relevent_dates
    
    Out[5]: 
    ['Registered on: 30-Dec-2004',
    'Expiry date:  30-Dec-2012',
    'Last updated:  08-Feb-2011']
  
  In [6]: w.expiry_date
    
    Out[6]: '30-Dec-2012'