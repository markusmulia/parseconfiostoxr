# parseconfiostoxr
Parsing IOS-style configuration to XR-style configuration

- project convert configuration ini menggunakan lib CiscoConfParse http://www.pennington.net/py/ciscoconfparse/index.html
- install CiscoConfParse library dengan pip: pip install --upgrade ciscoconfparse *detail install: http://www.pennington.net/py/ciscoconfparse/installation.html#
- simpan semua file python (.py) dalam satu folder & file iosconfig yang akan diconvert
- untuk sementara script hanya dapat melakukan convert configurasi vrf dari ios ke ios-xr configurasi
- RUN dengan format:
   iostoxr.py <path_to_ios_config_file> <path_to_new_config_file>
   contoh: iosxr.py before.txt after.txt
- deskripsi file:
 - iostoxr : sebagai main file yg menjadi driver class iostoxrparser
 - iostoxrparser: berisi static method untuk parsing configuration ios ke ios-xr (sementara masih hanya dapat convert config vrf)
 - iosvrfconfparse: function library untuk parsing vrf 
 
***next to do***
create Class:
- iosintconfparse: function library untuk parsing interface
- iosospfconfparse: function library untuk parsing router ospf
- iosbgpconfparse: function library untuk parsing router bgp
- iosstaticconfparse: function library untuk parsing router static

create Class:
 - iosconftocsv: function library untuk parsing ios config ke csv
 - xrconftoscv: function library untuk parsing xr config ke csv

add function di class iostoxrparser:
-tambah fungsi untuk parsing config interface > call function dari iosintconfparse
-tambah fungsi untuk parsing config router ospf > call function dari iosospfconfparse
-tambah fungsi untuk parsing config router bgp > call function dari iosbgpconfparse
-tambah fungsi untuk parsing config router static > call function dari iosstaticconfparse

