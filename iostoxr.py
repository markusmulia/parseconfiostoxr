#main file to parsing ios config file to new ios-xr config file

#import 
import sys
import os.path
from iostoxrparser import IosToXRParser


#check sys.argv[1] exist

if len(sys.argv) >= 3:
 if os.path.isfile(sys.argv[1]):
  IOS_CONF_FILE = sys.argv[1]
 else:
  #if file not exist force termination from program
  print "use format iostoxr.py <path_to_ios_config_file> <path_to_new_config_file>"
  sys.exit()
 #print sys.argv[2]
 new_file = open(sys.argv[2],"w+")
 new_file.close()
 XR_CONF_FILE = sys.argv[2]
 #convert configuration
 IosToXRParser.parse_all_vrf(IOS_CONF_FILE,XR_CONF_FILE)
else:
 print "use format iostoxr.py <path_to_ios_config_file> <path_to_new_config_file>"
 print "example: iostoxr.py before.txt after.txt"
 sys.exit()