# -*- coding: utf-8 -*-
# @Author: huangnan
# @Date:   2016-10-30 13:08:26
# @Last Modified by:   HUANG NAN
# @Last Modified time: 2016-11-17 01:28:20
# @E-mail: foxstarx@gmail.com


#!/usr/bin/env python  
# -*- encoding: utf-8 -*-  
# Created on 2015-03-12  
''''' 
pyspider结果保存到数据库简单样例。 
使用方法： 
    1, 把本文件放到pyspider/pyspider/database/mysql/目录下命名为mysqldb.py; 
    2, 建立相应的表和库; 
    3, 在脚本文件里使用from pyspider.database.mysql.mysqldb import ToMysql引用本代码; 
    4, 重写on_result方法. 
'''  
from six import itervalues  
import MySQLdb  
  
class ToMysql():  
      
    def __init__(self,kwargs):  
        ''''' 
        kwargs = {  'host':'localhost', 
                    'user':'root', 
                    'passwd':'root', 
                    'db':'others', 
                    'charset':'utf8'} 
        '''  
        hosts    = kwargs['host']     
        username = kwargs['user']  
        password = kwargs['passwd']  
        database = kwargs['db']  
        charsets = kwargs['charset'] 
        port = kwargs.has_key('port') and int(kwargs['port']) or 3306
          
        self.connection = False 
        try:  
            self.conn = MySQLdb.connect(host = hosts,user = username,passwd = password,db = database,charset = charsets, port = port)  
            self.cursor = self.conn.cursor()  
            self.cursor.execute("set names "+charsets)  
            self.connection = True  
        except Exception,e:  
            print "Cannot Connect To Mysql!/n",e  
              
    def escape(self,string):  
        return '%s' % string  
          
    def into(self,tablename=None,**values): 
    	print tablename
    	print values
        if self.connection:   
            tablename = self.escape(tablename)    
            if values:  
                _keys = ",".join(self.escape(k) for k in values)  
                _values = ",".join(['%s',]*len(values))  
                sql_query = "insert into %s (%s) values (%s)" % (tablename,_keys,_values)  
            else:  
                sql_query = "replace into %s default values" % tablename  
            print(sql_query)
            print(values)
            try:  
                if values:  
                    self.cursor.execute(sql_query,list(itervalues(values)))  
                else:         
                    self.cursor.execute(sql_query)  
                self.conn.commit()  
                return True  
            except Exception,e:  
                print "An Error Occured1: ",e  
                return False  