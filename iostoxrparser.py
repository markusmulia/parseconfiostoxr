#class to parsing ios-config style to xr 

from ciscoconfparse import CiscoConfParse
from iosvrfconfparse import IosVrfConfigParser
class IosToXRParser:
 #procedure to convert specific vrf_name in conf_file form ios to ios-xr
 @staticmethod
 def parse_vrf(ios_conf_file,new_conf_file,vrf_name):
  xr_conf =  CiscoConfParse(new_conf_file) 
  vrf_attrib = IosVrfConfigParser.ios_get_vrf_attrib(ios_conf_file,vrf_name)
  
  if vrf_attrib['VRF_NAME']:
   print "create vrf config"
   xr_conf.append_line("vrf "+vrf_attrib['VRF_NAME'])
   xr_conf.append_line(" address-family ipv4 unicast")
  
  if vrf_attrib['EX_MAP']:
   print "create EXPORT Route-policy"
   for ex_map in vrf_attrib['EX_MAP']: 
    xr_conf.append_line(" export route-policy "+ex_map)
  
  if vrf_attrib['IM_MAP']:
   print "create IMPORT Route-policy"
   for im_map in vrf_attrib['IM_MAP']: 
    xr_conf.append_line(" export route-policy "+im_map)
	
  if vrf_attrib['RT_EXPORT']:
     print "create Export Route-Target "
     for rt_export in vrf_attrib['RT_EXPORT']: 
      xr_conf.append_line(" export route-target "+rt_export)

  if vrf_attrib['RT_IMPORT']:
     print "create Import Route-Target "
     for rt_import in vrf_attrib['RT_IMPORT']: 
      xr_conf.append_line(" export route-target "+rt_import)	
  xr_conf.commit()
  xr_conf.save_as(new_conf_file)
 
 @staticmethod
 #procedure to convert all configured vrf in conf_file from ios to ios-xr 
 def parse_all_vrf(ios_conf_file,new_conf_file):
  for vrf_name in IosVrfConfigParser.ios_get_list_vrf(ios_conf_file):
   print "create config for vrf"+vrf_name
   IosToXRParser.parse_vrf(ios_conf_file,new_conf_file,vrf_name)


#IosToXRParser.parse_all_vrf('before.txt','after.txt')