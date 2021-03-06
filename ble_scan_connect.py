from bluepy.btle import Peripheral, UUID                                     
from bluepy.btle import Scanner, DefaultDelegate                             
                                                                             
class ScanDelegate(DefaultDelegate):                                         
        def __init__(self):                                                  
                DefaultDelegate.__init__(self)                               
        def handleDiscovery(self, dev, isNewDev, isNewData):                 
                if isNewDev:                                                 
                        print ("Discovered device", dev.addr)                
                elif isNewData:                                              
                        print ("Received new data from", dev.addr)
        def handleNotification(self, cHandle, data):
                print(data)
scanner = Scanner().withDelegate(ScanDelegate())                             
devices = scanner.scan(10.0)                                                 
n=0                                                                          
addr = []                                                                    
for dev in devices:                                                          
        print ("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi))
        addr.append(dev.addr)                                                
        n += 1                                                               
        for (adtype, desc, value) in dev.getScanData():                      
                print (" %s = %s" % (desc, value))                           
number = input('Enter your device number: ')                                 
print ('Device', number)                                                     
num = int(number)                                                            
print (addr[num])                                                            
#                                                                            
print ("Connecting...")                                                      
while True:
    try:
        dev = Peripheral(addr[num], 'random')    
        break
    except:
        pass
dev.setDelegate(ScanDelegate())
#for ch in testService.getCharacteristics():
#                                                                            
print ("Services...")                                                        
for svc in dev.services:                                                     
    print (str(svc))

#                                                                            
#try:

#testService = dev.getServiceByUUID(UUID(0xfff0))
#for ch in testService.getCharacteristics():
#    print (str(ch))
                                                       
#ch = dev.getCharacteristics(uuid=UUID(0xfff4))[0]
'''
handle = ch.getHandle() + 2
res = dev.writeCharacteristic(handle, b'\x02\x00', withResponse=True)
print('res: ', res)
#print(ch.read())
#ch.write(b'\x02')

while True:
    if dev.waitForNotifications(10.0):
        print('yay')
        break
'''
descriptors = dev.getDescriptors()
print(descriptors)


for i in descriptors:
    print('UUID: ', i.uuid)
    if i.uuid == UUID(0x2902):
        try:
            i.write(b'\x02\x00', withResponse=True)
            #print(res)
            value = i.read()
            print('value: ', value)
        
        except:
            pass

while True:
    if dev.waitForNotifications(10.0):
        pass

dev.disconnect()
