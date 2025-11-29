def ola(s,d):
    print('booked ola from:',s,' to ',d)
def uber(s,d):
    print('booked ola from: ',s,' to ',d)
def maps(s,d,app):
    app(s,d)
s,d = input('enter source, destination[space seperated]: ').split()
service = input('enter taxi service')
if 'ola' in service:
    maps(s,d,ola)
elif 'uber' in service:
    maps(s,d,uber)
    