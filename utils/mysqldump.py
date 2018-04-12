# coding=utf-8
import utils,os
from utils import app,consts,fileutils
import subprocess

s="""
exec Set_ObjectAccess 'Президент', 'руководство', 'INSERT'
GO
"""
#for x in ['INSERT','UPDATE','DELETE']:
#    for [t] in ExecSql()

urlToProcess=r'http://dev.mysql.com/doc/refman/5.6/en/mysqldump.html'

def RegenerateMySqlDumpConsts():
    from utils import web_crawler
    def GenerateConsts(d):
        d=[[(v[1] and v[1].lstrip('-').split('=')[0].split('[')[0].replace('-','_')),v[1],v[1]+'\n'+v[2]] for v in d]
        consts.GenPyConstants(d,'mysqldump_const.py','dump_options')

    web_crawler.ParseAndSaveXDoc(urlToProcess,{'.//table[@summary="mysqldump Options"]//tr':['./td[2]','./td[1]','./td[3]',]},GenerateConsts)

#RegenerateMySqlDumpConsts()

#exit(0)

import mysqldump_const
from mysqldump_const import *

def Import(filename='', flRepeatTimes=5):
#    import mydb
    if flRepeatTimes:
        Import(filename,flRepeatTimes-1)
    """
      Execute script and import data to DB
      flRepeatTimes - for referential constraints. (sometimes we have wrong order of tables in script file)
    """
    #app.Log(subprocess.check_output(['mysql','-u'+mydb.db.user,'-p'+mydb.db.password,'-D'+mydb.db.name,'-B','-f','<','%s'%app.AbsPath(filename)]))
    filename=app.AbsPath(filename)
    if os.path.exists(filename):
        app.Log('Import:')
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        app.Log(subprocess.check_output(['myexec.bat',mydb.db.name, filename],startupinfo=startupinfo))

def Export(options=[],filename=''):
    """
      Export current db (active) to filename (if not empty)
      and return Export Sql as text
      options #: array of dump_options
    """
    params=['mysqldump',dump_options.user.replace('user_name',mydb.db.user),
    '--password='+mydb.db.password,
    dump_options.complete_insert,
    dump_options.no_create_db,
    dump_options.no_create_info,
    dump_options.no_tablespaces,
    dump_options.skip_add_locks,
#    dump_options.disable_keys,
    dump_options.skip_extended_insert,
    mydb.db.name
    ]

    #cmdL1 = ["mysqldump", "--user=" + db_user, "--password=" + db_pass, domaindb]
    app.Log('Export:')
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#    app.Log(' '.join(params))
    dump_output=subprocess.check_output(params,startupinfo=startupinfo)
#    p1 = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#    dump_output = p1.communicate()[0]
    fileutils.Save2File(filename,dump_output,'wb')
    #print dump_output

def main():
#    import mydb
#    from mydb import *
    db_settings=['localhost','root','']
    dbName='?'
    mydb.InitDb(dbName,*db_settings)
    Export([],r'test.sql')
    Import(r'test.sql')

#if __name__ == '__main__':
#    main()

import mydb
