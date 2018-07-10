#!/usr/bin/python
# -*- coding:utf-8 -*-

import tool.My_Option
import tool.My_Mysql_Application
import tool.My_Log,tool.logic.My_Tool
import tool.My_Config as My_Config
import os,sys



if __name__ == '__main__':
    my_args=tool.My_Option.my_parser(prog='Myprogram')
    confile=os.path.dirname(sys.argv[0])
    logconfile=os.path.join(confile,"config","logging.ini")
    mysqlconfile=os.path.join(confile,"config","data.ini")
    logger=tool.My_Log.mylog(logconfile)
    try:
        if my_args.datasource == 'mysql':                  
            myconfig=mysqlconfile
            dbhost=My_Config.getConfig(myconfig,"my_mysql","dbhost")
            dbport=int(My_Config.getConfig(myconfig,"my_mysql","dbport"))
            dbname=My_Config.getConfig(myconfig,"my_mysql","dbname")
            dbuser=My_Config.getConfig(myconfig,"my_mysql","dbuser")
            dbpassword=My_Config.getConfig(myconfig,"my_mysql","dbpassword")
            dbcharset=My_Config.getConfig(myconfig,"my_mysql","dbcharset")
            my_secret = tool.logic.My_Tool.prpcrypt('fansfansfansfans')
            dbpassword = my_secret.decrypt(dbpassword)
            aa=tool.My_Mysql_Application.my_Mysql_status(dbhost,dbport,dbname,dbuser,dbpassword)           
            try:
                aa.the_sql_ping()
                if my_args.dbdata:
                    print aa.dbname_db_data(my_args.dbdata)
                else:
                    mylist_filter=tool.logic.My_Tool.mylist_filter('Database')
                    mylist_filter.manylist_filter(aa.dbname_db_all())
#                    print aa.sql_processlist()
#                    print aa.dbname_global_status('Com_commit')                   
                aa.close()
                logger.info("%s is close" % (dbhost))                  
#            bb=aa.cache_read()
#            print json.dumps(bb)
#            aa.cache_close()
            except Exception,e:
                logger.exception('remote mysql have something wrong %s' % e)
                aa=tool.My_Mysql_Application.my_Mysql_status(dbhost,dbport,dbname,dbuser,dbpassword)
        elif my_args.datasource == 'redis':
            print "now not support"
        else:
            pass
    except Exception,e:
        logger.exception('something wrong %s' % e)