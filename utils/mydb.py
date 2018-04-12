# coding=utf-8
import utils,os,sys, Queue,thread
from utils import app,fileutils,SmartTypes
import MySQLdb
import utils.db_helper
utils.db_helper.escape_func=MySQLdb.escape_string
from utils.db_helper import *
import sets
from sets import Set
import datetime,time,decimal,types, traceback
#import chardet, difflib
from operator import itemgetter, attrgetter
import re
import subprocess
import random, threading

import collections, itertools
from itertools import chain
from collections import OrderedDict
#print app.CurDir
tmpLoadPrefix=''
##db=None

flFastLoad=1
ScriptModeFile=1
ScriptModeArr=2
ScriptArr=[]
flScriptMode=0
ScriptLogFile=app.AbsPath('script.sql')
#ScriptCommands=[]

if flScriptMode:
    # clear script.sql
    #fileutils.Save2File()
    app.Log('',ScriptLogFile,0,1)

defEnc='utf8'
DefEngine='MyISAM'
dEncSet={
'cp1251':'CHARACTER SET utf8 COLLATE utf8_general_ci',
'utf8':'CHARACTER SET utf8 COLLATE utf8_unicode_ci'
}

s='''
SET group_concat_max_len = 4000000;
#delete from xld_70a39f9a537b4eba94bc291051027b3a where sheet between 0 and 3;
delete from xld_70a39f9a537b4eba94bc291051027b3a; where col_width<10 and col_to=0 and row_to=0;
ALTER TABLE xld_70a39f9a537b4eba94bc291051027b3a ADD UNIQUE (sheet ,col,row, lb, tb, rb, bb);
'''

#mySqlScriptPattern = re.compile(r'''((?:[^;"']|[^\]"[^"]*"|[^\]'[^']*')+)''',re.I | re.M |re.DOTALL)
mySqlScriptPattern = re.compile(r'[;][ ]*$',re.IGNORECASE | re.MULTILINE)
#script=fileutils.GetFileData(r'c:\1.txt')
#for a in mySqlScriptPattern.split(s):
#    print a
#exit(0)

def createTableDef(defs={'table':'','comment':'','fields_def':''}):
    return ('create table %(table)s(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,%(fields_def)s)'%defs)+('ENGINE=%s  DEFAULT CHARSET=%s comment "%s"'%(DefEngine,defEnc,defs['comment']))

sqlCols='select COLUMN_NAME,CHARACTER_MAXIMUM_LENGTH from INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA=database() and TABLE_NAME="%s"'
##sqlColsCurDb='select COLUMN_NAME,CHARACTER_MAXIMUM_LENGTH from INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA="%s" and TABLE_NAME="%s"'
lastDbName=None
#TABLE_CATALOG 	TABLE_SCHEMA 	TABLE_NAME 	COLUMN_NAME 	ORDINAL_POSITION 	COLUMN_DEFAULT 	IS_NULLABLE 	DATA_TYPE 	CHARACTER_MAXIMUM_LENGTH 	CHARACTER_OCTET_LENGTH 	NUMERIC_PRECISION 	NUMERIC_SCALE 	CHARACTER_SET_NAME 	COLLATION_NAME 	COLUMN_TYPE 	COLUMN_KEY 	EXTRA 	PRIVILEGES 	COLUMN_COMMENT
#def	coral	city	id	1	NULL	YES	char	100	300	NULL	NULL	utf8	utf8_general_ci	char(100)	 	 	select,insert,update,references

#db=MySQLdb.connect(db='kvadratour', host='localhost', user='root', passwd='', use_unicode=True)

dbs_on=getattr(app.params,'dbs_on',0)
dbs_lock=threading.Lock()
dbs={}
tAutoCloseDb=0
AutoCloseDbAfter=getattr(app.params,'AutoCloseDbAfter',1000)

def TableColumns(tab_name):
    return map(itemgetter(0),ExecSql(sqlCols%(tab_name,)))

def AutoCloseDb():
    with dbs_lock:
        for k,v in dbs.items():
            cDelta=v.lastAccess-datetime.datetime.now()
            if cDelta.seconds>AutoCloseDbAfter:
                try:
                    dbn=v.dbn
                    v.close()
                    app.Log('autoclosedb '+dbn)
                except:
                    app.LogError('AutoClose.')
                dbs[k]=None
                del dbs[k]
def getdb(raise_err=1):
    threadId=thread.get_ident()
    err=''
    if threadId not in dbs:
        if flScriptMode:
            threadId=dbs.keys()[0]
        else:
            err='ERROR: NO OPEN MYSQL CONNECTION for thread %d'%threadId
    else:
        if len(dbs[threadId])>1:
            err='ERROR: YOU HAVE FEW MYSQL CONNECTION for thread %d'%threadId

    if err<>'':
        app.out(err)
        app.Log(err)
        if raise_err:
            raise Exception(err)
        return None

    return dbs[threadId][0]

def InitDb(dbname,host,user,passwd,UserUniqDbId='', OnInit='', port=3306):
    #global db,
    global dbs,tAutoCloseDb
    global lastDbName
    lastDbName=dbname

    threadId=thread.get_ident()
    if threadId not in dbs:
        dbs[threadId]=[]
##    dbn='%s_%s_%s_%s_%s'%(host,user,dbname,passwd,UserUniqDbId)

##    if dbs_on:
##        with dbs_lock:
##            if tAutoCloseDb==0:
##                tAutoCloseDb=threading.Timer(AutoCloseDbAfter/2,AutoCloseDb)
##            if  dbn in dbs:
##                db=dbs[dbn]
##                db.lastAccess=datetime.datetime.now()
##                if OnInit:
##                    if db.OnInit<>OnInit:
##                        db.OnInit=OnInit
##                        ExecSql(OnInit)
##                return db

##    CloseDb()
    db=MySQLdb.connect(db=dbname, host=host, user=user, passwd=passwd, use_unicode=True, port=port)
    db.set_character_set(defEnc)
    db.host=host
    db.name=dbname
    db.user=user
    db.password=passwd
    db.UserUniqDbId=UserUniqDbId
    db.OnInit=OnInit
    db.lastAccess=datetime.datetime.now()
    dbs[threadId].append(db)

    def localExecSql(self,sql,flRaise=1, flAsDict=0, pars={}):
        return _ExecSql(sql,flRaise, flAsDict, pars, self)

    def localCloseDb(sel):
        return CloseDb(self)

    db.ExecSql=localExecSql
    db.CloseDb=localCloseDb
##    db.dbn=dbn
    ExecSql('SET NAMES '+defEnc)
    ExecSql('SET CHARACTER SET '+defEnc)
    ExecSql('SET character_set_connection='+defEnc)

    if OnInit:
        ExecSql(OnInit)
    # save
    if dbs_on:
        with dbs_lock:
            dbs[dbn]=db
    return db

def CloseDb(db=None):
    if db is None:
        db=getdb()
##    global db
    try:
        if db and db.open:
            try:
                db.close()
            except:
                app.LogError('CloseDb. ')
#        thId=thread.get_ident()
#        dbs[thId]=None
#        del dbs[thId]
    except:
        app.LogError('CloseDb. ')

    db=None

def FlushScript():
    global flScriptMode
    if not flScriptMode:
        return
    #flScriptMode=not flStopScriptMode
    if flScriptMode==1:
        try:
            app.Log(subprocess.check_output(['myexec',lastDbName, ScriptLogFile]))
        except:
            app.LogError()
    elif flScriptMode==2:
        mSave=flScriptMode
        flScriptMode=0
        try:
            ExecSql(ScriptArr)
        finally:
            flScriptMode=mSave

#    ExecSql('source script.sql')
flCloseCur=1
def GetCursor(db, statement, flRecursiveCnt=0, cursor=None):
    ret=None
    try:
        rCur=cursor or db.cursor()
        ret=rCur.execute(statement)
    except (AttributeError, MySQLdb.OperationalError) as e:
#        if flRecursiveCnt:
#            app.Log('Still get mysql Error (programm execution is stopped): '+str(e))
#            raise e
#        else:
        app.Log('exception generated during sql connection: '+str(e))
        raise e
#            InitDb(db.name,db.host,db.user,db.UserUniqDbId,db.OnInit)
#            return GetCursor(statement,flRecursiveCnt+1)
    return [rCur,ret]

def isSql(sql):
#    if not isinstance(sql,(list,tuple)):
#        sql=[sql]
    return any(map(sql.lower().strip().startswith,['select']))

def isDml(sql):
#    if not isinstance(sql,(list,tuple)):
#        sql=[sql]
    return any(map(sql.lower().strip().startswith,['insert','replace','update','delete','call','set']))

##def Commit():
##    global db
##    db.commit()

##def Rollback():
##    global db
##    db.rollback()

##def StartTrans():
##    global db
##    db.start()

#ExecSqlInMainThread=getattr(app.params,'MyDbSingleThread',0)
#execSqlQueue=Queue.Queue()

##def ExecSqlThread():
##    while 1:
##        try:
##            ret=_ExecSql(*execSqlQueue.get())
##        except:
##            pass
##
##def ExecSql(sql,flRaise=1, flAsDict=0, pars={}):
##    args=(sql,flRaise, flAsDict, pars)
##
##    if not flExecSqlThread or isSql(sql):
##        # wait for other sqls
##        execSqlQueue.join()
##      неправильно!! может быть рассинхрон - надо выполнять всё в потоке и ответ синхронизировать и получать с помощью лока и дополнительной очереди ответов
##        return _ExecSql(*args)
##    else:
##        execSqlQueue.put(args)

def ExecSql(sql,flRaise=1, flAsDict=0, pars={},db=None):
    if db is None:
        db=getdb()
    return db.ExecSql(db,sql,flRaise, flAsDict, pars)

def _ExecSql(sql,flRaise=1, flAsDict=0, pars={},db=None, recursive=0):
    if db is None:
        db=getdb()
##    global db
#    print db
    # обрабатываем параметры переданные в качестве диктионари.
    if pars:
#        print 'Before', str(pars)
        for k,v in pars.items():
            if isinstance(v,basestring):
                if isinstance(v,unicode):
                    v=v.encode('utf-8')
                pars[k]=mydb.escape_func(v)

#        print 'After', str(pars)
#        sql=sql%pars

    if isinstance(sql,(unicode,str)) and sql.strip()=='':
        return None
#        if flAsDict:
#            return [{}]
#        else:
#            return []

    if not db:
        raise Exception('NO DB')

    flErrorProcessed=0
    r=None
    try:
        if not isinstance(sql,(list,tuple)):
            sql=[sql]
        sql=['START TRANSACTION']+sql
#        flSelect=(len(sql)==1) and sql[0].lower().startswith('select')
        flDml=0
        flErrorProcessed=0
        cur=None
        for sCmd in sql:
            try:
                if flCloseCur:
                    if cur:
                        cur.close()
                    cur=None
    #            time.sleep(0.05);
                if pars:
                    sCmd=sCmd%pars
                sCmd=app.removeComments(sCmd,1)
                sCmdStrip=sCmd.strip().strip(';')
                sCmdStripLow=sCmdStrip.lower()
                if sCmdStrip<>'START TRANSACTION':
                    app.Log(sCmdStrip)
                if sCmdStrip and sCmd<>'':
                    script=mySqlScriptPattern.split(sCmdStrip)#[1::2]
                    if len(script)>1:
                        flErrorProcessed=1
                        r=ExecSql(script,flRaise,flAsDict,pars)
                        flErrorProcessed=0
                        continue

##                    if not flScriptMode:
##                        if sCmd<>'START TRANSACTION':
##                            app.Log('SQL Command  : '+ sCmd)
                    try:
                        flSelect=sCmdStripLow.startswith('select') or sCmdStripLow.startswith('show')

                        flDml=flDml or isDml(sCmdStripLow)
                        if flScriptMode==1:
                            if not flSelect:
                                app.Log((sCmdStrip.endswith(';') and sCmdStrip) or (sCmdStrip+';'),ScriptLogFile,0)
                            continue
                        elif flScriptMode==2:
                            if not flSelect:
                                ScriptArr.append(sCmdStrip.strip(';'))
                            continue
                        else:
                            ##app.Log('create cursor')
                            cur,ret=GetCursor(db,sCmdStrip,cursor=((not flCloseCur and cur) or None))
                            if isDml(sCmdStrip) and not r:
                                r=ret
    #                    try:
    #                      z=input(sCmd)
    #                    except:
    #                        pass
                        if flSelect:
                            r=cur.fetchall()
                            if not r:
                                return []
                            app.Log('ExecSql.Fields Description ='+str(cur.description))
                            if flAsDict:
                                fields=map(itemgetter(0),cur.description)
                                # make field list unique. Add index to name
                                fldUniq=[]
                                for x in fields:
                                    if x in fldUniq:
                                        # try to find next unique index
                                        for i in xrange(1,100):
                                            if (x+str(i)) not in fldUniq:
                                                break
                                        fldUniq.append(x+str(i))
                                    else:
                                        fldUniq.append(x)

                                fields=fldUniq

                                r1=[]
                                for x in r:
                                    r1.append(SmartTypes.SmartDict(zip(fields,x)))
                                r=r1
                            flSelect=not flSelect
                    except:
                        app.LogError('ExecSql:',0)
                        app.LogError(sCmd,flRaise)
                    #return None
            finally:
                if cur and flCloseCur:
#                    app.Log('close cursor')
                    cur.close()
                    cur=None
        try:
            if not flScriptMode:
                #if flDml:
#                    app.Log('db commit')
                db.commit()
        except:
           app.LogError('ExecSql.Commit',0)
    #        if len(r)==1:
#            if len(r[0])==1:
#                return r[0][0]
    except:
        ##OperationalError: (2006, 'MySQL server has gone away')
        if 'server has gone away' in traceback.format_exc():
            if recursive<3:
                app.LogError('Recconnect. We will try to execute sql again : '+str(sql))
                threadId=thread.get_ident()
                #reconnect
                dbs[threadId]=[]
                db=InitDb(db.name,db.host,db.user,db.password)
                return _ExecSql(sql,flRaise,flAsDict,pars,db,recursive+1)
            return None

        if not flScriptMode:
            db.rollback()

        if not flErrorProcessed:
            app.LogError('ExecSql:',0)
            app.LogError(sCmd,0)

        if flRaise:
            raise
        return None
    return r

##if flExecSqlThread:
##    thread.start_new_thread(ExecSqlThread,())

def ExecScript(sql, flRaise=1):
    """Deprecated. You can use ExecSql directly"""
#    data = """part 1;"this is ; part 2;";'this is ; part 3';part 4;this "is ; part" 5"""
#    ExecSql(mySqlScriptPattern.split(sql)[1::2], flRaise=1)
    ExecSql(sql, flRaise=1)

funcProp=attrgetter('name','content')

def funcPropLowName(nv):
    return (nv[0].lower(),nv[1])

def GetProps(el):
    r={}
#    return dict(map(funcPropLowName,map(funcProp,el.properties)))
    for p in el.xpathEval('@*'):
        r[p.name.lower()]=p.content
    #    r[prop.name.lower()]=prop.content
#            if (prop.type=='attribute'):
    return r

def GetXpathProps(el,path):
    r={}
#    return dict(map(funcPropLowName,map(funcProp,el.properties)))
    for x in el.xpathEval(path+r'/@*'):
        k,v=str(x).strip().replace('"','').split('=',1)
        k=k.lower()
        p=x.parent
        if p in r:
            r[p][k]=v
        else:
            r[p]={k:v}
    return r

#fs,vs=None,None
def CreateTable(TabName, fields, vals=None, flDropTab=0, flOnlyIns=0, flCreateIndexes=1, MinColumnSize=250, flNotNull=1, flExec=1):
#    global fs,vs
    global tmpLoadPrefix
    #check fields names for table creation
    try:
      if vals and not fields:
        fields=['f%d'%i for i in xrange(len(vals[0]))]
      reservedWords=['key','from','to']
      fldTypes={}
      if isinstance(fields,(SmartTypes.SmartDict,dict)):
        fldTypes=fields
        fields=fldTypes.keys()
      fields=map(lambda x: MySqlName((x in reservedWords and x+'1') or x),fields)#.replace('-','_')
      # check for duplicate field name
      # for now simple for id
      if fields.count('id')>1:
          ind=fields.index('id',1)
          fields[ind]='id1'
    #if len({}.fromkeys(fields))!=len(fields):
#        for i in range(len(fields)):
#            fields)
      # get cols info
#      rCols=ExecSql(sqlCols%(lastDbName,TabName)+' and DATA_TYPE="text"',0)
      ret=ExecSql(sqlCols%(TabName,))
      app.Log('COLS sql=%s cols=%s : '%(sqlCols%(TabName),str(ret)))
      dAllCols=dict(ret)
      colsInfo=None
      sqlCreateTab=''
      ret=[]
      GetCharDef=lambda size: ((size>=1000) and 'TEXT') or 'varchar(%d)'%(max(size,1));
      if vals:
        fLens=[[fields[i],max(map(lambda x : len(fsys.ToUtf8(x))+4,map(itemgetter(i),vals)))] for i in xrange(len(fields))]
      else:
        fLens=zip(fields,[0]*len(fields))

      dLens=dict(fLens)

      if dAllCols and not flDropTab:
        colsInfo=dict(dAllCols)
        app.Log('colsInfo='+str(colsInfo))
        for k,v in filter(lambda x: (x[0] in colsInfo) and (int(x[1])>int(colsInfo[x[0]])), dLens.items()):
            if v>=1000:
                ret+=['ALTER TABLE %s CHANGE %s %s TEXT %s NULL DEFAULT NULL'%(TabName,k,k,dEncSet[defEnc])]
            else:
                ret+=['ALTER TABLE %s CHANGE %s %s VARCHAR(%s) %s NULL DEFAULT NULL'%(TabName,k,k,v,dEncSet[defEnc])]
      else:
        defFields=map(lambda (s,maxLen) : ('%s '+((s in fldTypes and fldTypes[s]) or (s.lower()=='id' and 'INT') or GetCharDef(max(maxLen,MinColumnSize)))+' %s')%(s,((s.lower()=='id' or flNotNull) and 'not null') or 'default null'),fLens)
        sqlCreateTab=(not flOnlyIns and 'create table IF NOT EXISTS %s (%s) ENGINE=%s  DEFAULT CHARSET=%s'%(TabName,makeInsStr(defFields),DefEngine,defEnc)) or ''
        ret=[(flDropTab and 'drop table IF EXISTS %s'%TabName) or '',sqlCreateTab]
        if 'id' in fldTypes:
            ret+=['ALTER TABLE %s ADD PRIMARY KEY (id)'%TabName,'ALTER TABLE %s modify id INT(11) NOT NULL AUTO_INCREMENT'%TabName]

#      if not tmpLoadPrefix:
#        tmpLoadPrefix='db_'
      if vals:
          if tmpLoadPrefix:
            fold=tmpLoadPrefix+'temp'
            fileutils.CreateDirs(fold)
            fold+='\\'
            fName=app.AbsPath(fold+'%s.tab'%TabName)
            app.Log('CreateTable '+fName)
#            vals=app.ApplyFunc2Vals(vals,lambda x: ((x is None) and 'Null') or x)
#            for r in vals:
#                for i in xrange(len(r)):
#                    if r[i] is None:
#                        r[i]='Null'
#                    else:
#                        r[i]=r[i].replace('\n','\\n').replace(';','.')
#            import csv
            fileutils.Save2Csv_old(fName,vals,add_repl=lambda x: ((x is not None) and x.replace('\\','\\\\').replace('\n','\\n').replace(';','.')) or '')#,'$^','$\r\n^'#.replace('`','')
#            fileutils.Save2Csv(fName,vals)#,'$^','$\r\n^'
            #mysql wants / slashes
            fName=fName.replace('\\','/')
            # if we create table then we need always
            if sqlCreateTab:
                insFields=fields
            else:
                insFields=map(lambda f : ((f in dAllCols) and f) or '@dummy',fields)

            insFields=fileutils.lineSep(insFields,',')
            LoadSql="""
                LOAD  DATA LOCAL INFILE  '%s'
                IGNORE
                INTO  TABLE  %s
                CHARACTER SET UTF8
                FIELDS
                        TERMINATED  BY  ';'
                        ESCAPED BY '\\\\'
                LINES
                        TERMINATED  BY  '\\r\\n'
                IGNORE  0  LINES (%s)"""%(fName,TabName,insFields)
            retIns=[LoadSql]
          else:
            retIns=map(lambda v: genInsert(TabName,fields,[v]),vals)

          ret+=retIns

      if flCreateIndexes and flDropTab:
        for x in fields:
            if x.lower()<>'id':
                ret.append('ALTER TABLE %s ADD INDEX(%s)'%(TabName,x))

      if flExec:
        fileutils.Save2File('new_script.sql',ret)
        ExecSql(ret,0)

      return ret
    except:
        app.LogError('Table=%s\nFields=%s\nVals=%s'%(str(TabName),str(fields),str((vals and vals[:100]) or '')))
        raise

def Csv2Table(TabName, fname, delim='autodetect', flFistLineFields=1, flDropTab=0, flExec=1):
    l=fileutils.GetFileData(fname,1)
    if len(l)>0:
        l[0]=l[0].strip('\xef\xbb\xbf')

    #l=map(lambda s : s.strip(),l)
    #.decode('utf-8').encode('cp1251','replace')

    if delim=='autodetect':
        DelimDetect=lambda sDelim: (len(l)>1) and (len(l[0].split(sDelim))!=1) and (len(l[0].split(sDelim))==len(l[1].split(sDelim))) and sDelim
        delim=DelimDetect(';') or DelimDetect(',') or DelimDetect('\t')
        if not delim:
            raise 'cannot detect delimeter in csv file. please choose one!'

    if flFistLineFields:
        fields=l[0].strip().split(delim)
    else:
        fields=map(lambda i : 'f'+str(i),range(len(l[0].split(delim))))
        fields=map(lambda i : 'f'+str(i),range(len(l[0].split(delim))))

    ind=(flFistLineFields and 0) or 1
    vals=map(lambda s : s.split(delim),l[ind:])
    fixInsVals=lambda fCnt,v: ((fCnt==len(v)) and v) or v+([None]*(fCnt-len(v)))

    cntFields=len(fields)
    vals=map(lambda v: fixInsVals(cntFields,v),vals)

    return CreateTable(TabName,fields,vals, flDropTab, flExec)

#fname=r'countries.csv'
#ExecSql(Csv2Table('buf_country',fname),0)
#exit(0)
def FixLibXmlXpath(s):
    ret=''
    for x in s.split('/'):
        if x and x<>'.':
            x='*[name()="%s"]'%x
        ret+='/'+x
    return ret[1:]

#print FixLibXmlXpath('.//packet/packetheader')
#print FixLibXmlXpath('.//prices/serviceSet/price/date')
#exit(0)

def StripItems(items):
    return [[k,v.strip()] for k,v in items]

def getSprData(node,path,idKey='key',addParentPropsLevel=0):
    ret={}

    cacheParents={}
    for x in node.findall(path):
        psAll=dict(StripItems(x.items()))
        #app.Log(psAll)
        #if 'fake' in psAll:
        #    continue
        key=psAll[idKey]
        parLevel=addParentPropsLevel
        par=x
        # если надо то обновляем словарь параметрами родительских объектов.
        while parLevel:
            par=par.find('..')
            ps=cacheParents.get(par)
            if not ps:
                ps=dict(StripItems(par.items()))
                cacheParents[par]=ps
            psAll.update(ps)
            parLevel-=1

        ret[key]=psAll
    return ret

"""
def getSprData(node,path,idKey='key',addParentPropsLevel=0):
    ret={}

    cacheParents={}
#    for x in xNodes(node,FixLibXmlXpath(path)):
#        psAll=GetProps(x)
    for x,psAll in GetXpathProps(node,FixLibXmlXpath(path)).items():
        #app.Log(psAll)
        if 'fake' in psAll:
            continue
        key=psAll[idKey]
        parLevel=addParentPropsLevel
        par=x
        # если надо то обновляем словарь параметрами родительских объектов.
        while parLevel:
            par=par.parent
            ps=cacheParents.get(par)
            if not ps:
                ps=GetProps(par)
                cacheParents[par]=ps

            psAll.update(ps)
            parLevel-=1

        ret[key]=psAll
    return ret
"""
def CreateSprFromDict(TabName,data, tabPrefix='', flDropTable=0, fOnlyIns=0, flCreateIndexes=0):
    if not data:
        return
    # update values in case some of dict records contains different fields
    # first of all we wants to update fields list (collect from all dicts)
    fields=OrderedDict().fromkeys(reduce(lambda ret,v : ret.update(v) or ret,data,OrderedDict()).keys(),'')
    fclean=fields.copy()

    # then we need to update values
#    nVals=[[i]+(fields.update(fclean) or fields.update(v) or fields).values() for i,v in data.items()]
    nVals=[[i+1]+(fields.update(fclean) or fields.update(data[i]) or fields).values() for i in xrange(len(data))]

    if tabPrefix:
        tabPrefix+='_'
#    print TabName
    CreateTable(tabPrefix+TabName,['id']+fields.keys(),nVals,flDropTable,0,flCreateIndexes,0,0)
   # data.clear()
##    hName=x.ShortName[(len(o[0])+1):-(len(o[-1])+1)]
##    country=x.Name.split('\\')[-2]
##    res.append(sId+';'+country.lower()+';'+hName.lower()+';'+x.Name+'\n')
##
##fileutils.Save2File(fname,res)
##ExecSql(Csv2Table('buf_kh',fname),0)

def IsTableExists(tName):
    return ExecSql("SHOW TABLES LIKE '%s'"%tName)

def IsDatabaseExists(Name):
    return ExecSql("SHOW DATABASES LIKE '%s'"%Name)

def IsColumnExists(tName,tCol):
    return ExecSql("SHOW COLUMNS FROM %s LIKE '%s'"%(tName,tCol))

def IsColumnIndexExists(tName,tCol):
    return ExecSql("SHOW INDEX FROM %s WHERE column_name = '%s'"%(tName,tCol))

def ImportTable(nodes,fMap,table,ukey):
    try:
#        print '123'
        dNodes=dict([[xValue(n,'@'+fMap[ukey],flEncode=0),GetProps(n)] for n in nodes])
        sql='select %s from %s where %s in (%s)'%(ukey,table,ukey,str(dNodes.keys())[1:-1])
#        print sql
        ret=ExecSql(sql)
#        print ret
        sql=''
        lvals=[]
        keys=fMap.keys()
        for x in Set(dNodes.keys()).difference(Set(ret)):
            ps=dNodes[x]
            lvals.append(map(lambda k: ps.get(fMap[k]),keys))
        app.Log(genInsert(table,keys,lvals))
        ExecSql(genInsert(table,keys,lvals))
    except:
        app.LogError('ImportTable : '+table)


class AnyData2MySql():
    def __init__(self,dbcon,table_name, fields=None, flDrop=1):
        self.dbcon=dbcon
        self.table_name=table_name
        self.fields=fields
        self.flDrop=1

    def __call__(self,data):
        CreateTable(self.table_name,self.fields,data,flDropTab=self.flDrop,flNotNull=0)

#print genInsert('aaa',['aa','mm'],[['1',2,3],['123','33','33']])
#exit(0)
#def main():
 #   pass

#if __name__ == '__main__':
#    main()

#<countries>
#  <country key="6228" name="???????" nameLat="Vietnam" code="VNM" />
#</countries>
#id 	alias 	name 	lname 	phprefix 	stamp 	description

def MySqlName(s):
    if '`' in s:
        return s
        raise Exception('s already have `')
    return '`'+s.strip()+'`'

def MsSqlName(s):
    if '[' in s:
        return s
        raise Exception('s already have [')
    return '['+s+']'

OnMakeTabName=lambda s : s

def MakeTranslitName(tName):
    if not tName:
        raise Exception('MakeTabName. Wrong table/column name : '+tName)

#    fileutils.Save2File(r'c:\cur.txt','13')
    #.decode('utf-8').decode('utf-8').
    #import chardet
#    fileutils.Save2File(app.AbsPath(r'cur.txt'),chardet.detect(tName))
    Name=app.cyr2lat(tName.strip(),lambda x : ((x.isalpha() or x.isalnum()) and x) or '_')#,autoReplace={"'","_"})
    s=Name.replace("'",'_')
#    print tName,Name
#    fileutils.Save2File(app.AbsPath(r'cur.txt'),'123')

#    s=reduce(lambda ret,s : ret.replace(s,'_'),list(' ,.!?/\\|`"\'~!@#$%^&*()=-+'),Name)
    #s=re.sub(re.compile("[]",re.DOTALL ) ,"" ,s) # remove all occurance streamed comments (/*COMMENT */) from string

    if not s:
        raise Exception('Cannot Generate Table/Field name : '+tName)
    return ((not s[0].isalpha() and 'c') or '')+s.lower()

def MakeTabName(tName):
    s=OnMakeTabName(tName)
    return s

#print MakeTabName('Преподаватель')

def MakeFieldName(fName):
    return MakeTabName(fName)

defaultFieldDef={
  'name' : 'f',
  'type' : '',
  'null' : 1,
  'default' : 'null',
  'autoinc' : 0,#AUTO_INCREMENT,
  'unique' : 0,
  'primary' : 0,
  'comment' : '',
  'ref' : ''# reference table name
  }

def PyTypeToMyType(oType):
    if oType=='bool':
        return 'boolean'

    if isinstance(oType,datetime.datetime) or (isinstance(oType,(str,unicode)) and oType=='date'):
        return 'date'

    if isinstance(oType,(str,unicode)) and oType=='datetime':
        return 'datetime'

    if isinstance(oType,int):
        return 'int'

    if isinstance(oType,(str,unicode)):
        return 'varchar(250)'

    if isinstance(oType,float):
        return 'decimal(14,4)'

    if isinstance(oType,(tuple,list)):
        return ('enum (%s)'%(",".join(['"%s"']*len(oType))))%oType

def GetCorrectFieldDefs(defs=defaultFieldDef, TabFormat=0):
#    print 'bububub ',defs
    """
    data_type [NOT NULL | NULL] [DEFAULT default_value]
      [AUTO_INCREMENT] [UNIQUE [KEY] | [PRIMARY] KEY]
      [COMMENT 'string']
      [COLUMN_FORMAT {FIXED|DYNAMIC|DEFAULT}]
      [STORAGE {DISK|MEMORY|DEFAULT}]
      [reference_definition]

reference_definition:
    REFERENCES tbl_name (index_col_name,...)
      [MATCH FULL | MATCH PARTIAL | MATCH SIMPLE]
      [ON DELETE reference_option]
      [ON UPDATE reference_option]

reference_option:
    RESTRICT | CASCADE | SET NULL | NO ACTION
"""
    dDefs=SmartTypes.SmartDict(defaultFieldDef.items())
    dDefs.update(defs)
    """
    if dDefs['table']=='':
        print '13'
    if dDefs['name']=='':
        print '13'
"""
    dDefs['type']=PyTypeToMyType(dDefs['type'])
    dDefs['table']=MakeTabName(dDefs['table'].strip())
    dDefs['name']=MakeFieldName(dDefs['name'].strip())
    dDefs['null']=(dDefs['null'] and 'null') or 'not null'
    dDefs['default']=(dDefs['default'] and 'DEFAULT '+str(dDefs['default'])) or ''
    dDefs['autoinc']=(dDefs['autoinc'] and 'AUTO_INCREMENT') or ''
    dDefs['unique']=(dDefs['unique'] and 'unique') or ''
    dDefs['primary']=(dDefs['primary'] and 'primary key') or ''
    dDefs['comment']=(dDefs['comment'] and "comment '%(comment)s'"%dDefs) or ''
#    if dDefs['ref']:
#        print '123'
    dDefs['ref']=(dDefs['ref'] and MakeTabName(dDefs['ref'])) or ''
    dDefs['ref']=(dDefs['ref'] and (((not TabFormat and ' ,ADD ') or ' , ')+' FOREIGN KEY (%(name)s) REFERENCES %(REF)s(ID) MATCH FULL ON DELETE SET NULL ON UPDATE SET NULL '%dDefs)) or ''
#    dDefs['ref']=(dDefs['ref'] and (((not TabFormat and ' ,ADD ') or ' , ')+' FOREIGN KEY (%(name)s) REFERENCES %(REF)s(ID) MATCH FULL ON DELETE CASCADE ON UPDATE CASCADE'%dDefs)) or ''
#    dDefs['ref']=(dDefs['ref'] and (((not TabFormat and ' ,ADD ') or ' , '))) or ''
    return dDefs

def MakeFieldDef(defs=defaultFieldDef, TabFormat=0):
    #print defs
    return """%(NAME)s %(TYPE)s %(NULL)s %(DEFAULT)s %(autoinc)s %(UNIQUE)s %(PRIMARY)s %(COMMENT)s %(REF)s"""%GetCorrectFieldDefs(defs,TabFormat)

defaultFieldDef['table']=''
defaultFieldDef['mode']='alter' #'script' if script mode then no execute sql
def AlterFieldDef(defs=defaultFieldDef):
    #print defs
    if defs['name'].lower()=='id':
        return ''

    dDefs=GetCorrectFieldDefs(defs)
    s=MakeFieldDef(defs)
    ret='ALTER TABLE %s %s '%(dDefs['table'],((IsColumnExists(dDefs['table'],dDefs['name']) and ('CHANGE '+dDefs['name'])) or 'ADD'))+s
    if dDefs['mode']!='script':
        ExecSql(ret)
    return ret

def AlterFieldIndex(defs=defaultFieldDef):
    #print defs

    if defs['name'].lower()=='id':
        return ''

    dDefs=GetCorrectFieldDefs(defs)
    tabName,colName=dDefs['table'],dDefs['name']
#    index='FULLTEXT '
    indexDef=''
    if any(map(dDefs['type'].startswith,['char','varchar','text','string'])):
        indexDef='(30)'
#        fullText=''

    ret='ALTER TABLE %s ADD INDEX idx_%s(%s%s)'%(tabName,colName,colName,indexDef)
    if dDefs['mode']!='script':
        if not IsColumnIndexExists(tabName,colName):
            ExecSql(ret)
    return ret


fillUniqId=0

def FillRandomValues(count=31):#defs=None,lanf='rus'):

    def MakeRandomRow(cols):
        global fillUniqId
        ret=[]
        for col in cols:
#            if isinstance(col,(str,unicode)):
#                name=col
#                colType=cols[col]['type']
#            else:
            name=col['field']
            colType=col['type']

            val=''
            if 'enum' in colType:
                val=random.choice(colType.strip('enum()').split(',')).strip("'").encode('utf-8')
            elif colType.startswith('varchar') or colType.startswith('char') or colType.startswith('text'):
                val=name+str(fillUniqId)
            elif 'date' in colType:
                val=str(random.randint(2007,2012))+'-0'+str(random.randint(1,9))+'-'+str(random.randint(10,28))
            else:
#                if name.lower()=='id':
#                    val=fillUniqId
#                else:
                val=random.randint(1,3)

            ret.append(val)

        fillUniqId+=1
        return ret

    def MakeRandomRows(cols, count=31):
        global fillUniqId
        fillUniqId=1
        return [MakeRandomRow(cols) for x in xrange(count)]

#    if not defs:
    tabs=ExecSql('SHOW TABLES')
    for rec in tabs:
        tab=OnMakeTabName(rec[0])
        cols=ExecSql("SHOW COLUMNS FROM %s WHERE Field<>'id'"%tab,flAsDict=1)
        vals=list(MakeRandomRows(cols,count))
        ExecSql("SET FOREIGN_KEY_CHECKS = 0")
        sql=genInsert(tab,[x['field'] for x in cols],vals, OnMakeTabName)
        app.Log(str(vals))
        app.Log('FillRandomValues : '+sql)
        ExecSql(sql)
        ExecSql("SET FOREIGN_KEY_CHECKS = 1")
    return None


def InsertedId():
    return ExecSql('select LAST_INSERT_ID()')[0]

##    for tab in defs:
##        tDef=defs[tab]
##        tDefFields=tDef['fields']
##        if 'multyref' in tDef:
##            continue
##            genInsert(tab,tDefFields.keys(),MakeRandomRows(tDefFields))
##        else:
##            genInsert(tab,tDefFields.keys(),MakeRandomRows(tDefFields))

#InitDb('arm','localhost','root','')
#app.UnpickleObj(r'C:\defs.obj')
#FillRandomValues()

import utils.mysqldump
from utils.mysqldump import *