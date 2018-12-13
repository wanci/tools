#!/usr/local/services/python/bin/python
# -*- coding: utf-8 -*-

from op_eni_handle import *

class CAddEniThread(COpEniThread):
    def do_after_init(self):
        self.add_step(self.del_zoo, self.add_zoo)
        self.add_step(self.add_zoo, self.del_zoo)
        self.add_step(self.del_zoo, self.add_zoo)
        self.add_step(self.add_zoo, self.del_zoo)

    def op_zoo(self, b_add):
        zoo_req = { 
                "LEO":{
                    'value': 'vv',
                    'children':{
                        '9.9.9.0|24:8.8.0.0|16':{'value': '111'},
                        '9.8.9.0|24:8.8.0.0|16':{'value': '111'},
                        '10.2.1.0|24:10.24.0.0|16': {}
                        },  
                    'root':"/TVPC/VM/1588/10.2.0.0|24/10.2.0.121",
                    },  
                }   
        if b_add: return self.do_zoo_req(CZoobSetReqOp(), zoo_req)[0]
        else: return self.do_zoo_del_key_by_req(zoo_req)[0]

class CAddEniHandle(COpEniHandle):
    def get_thread(self): return CAddEniThread()
    def b_add(self): return True

if __name__ == '__main__':
    data = {'detail':[
        #{'vpcId':430,'owner':'12345678','subnetId':69,'name':'test','business':'111', 'state':1},
        {'vpcId':1588,'owner':'wanci','subnetId':53,'name':'leohli','business':'leo', 'state':1},
        ]}  
    handle = CAddEniHandle()
    handle.init(data)
    print handle.process()

