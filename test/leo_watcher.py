#coding=utf8
import constimport config
import state

from config import loggerfrom zkwatcher import ChildWatcher, ValueWatcher, BothWatcher
from state import dict_remove, contain_vservice, diff_set

class LeoWatcher(BothWatcher):
    need_hold = True    node_name = 'remote'
    watcher_flag = True

    @staticmethod
    def build(zkconn):        path = "/TVPC/VM/1588/10.2.0.0|24/10.2.0.121/LEO"
        return LeoWatcher(zkconn, path)

    def do_deleted(self):        logger.info('leo path: %s in do_deleted', self.path)
        self.children_change([])        self.zkconn.remove_path(self.path)
        super(LeoWatcher, self).do_deleted()

        #if not super(LeoWatcher, self).do_deleted():        #    logger.info('%s deleted event received.', self.path)
        #    self.children_change([])        #    self.zkconn.remove_path(self.path)
    def destroy(self):
        self.children_change([])
        self.zkconn.unwatch_path(self.path)        logger.info('leo path: %s destroy', self.path)
    def value_change(self, value):
        logger.info('leo path: %s value change: %s', self.path, value)

    def diff(self, children):
        return diff_set(            children,
            []          )   
    def add_node(self, gw):
        logger.info('leo path: %s add node: %s', self.path, gw) 

    def del_node(self, gw):
        logger.info('leo path: %s del node: %s', self.path, gw) 
