# coding=utf-8
import utils
from utils import app, fsys
from app import utf8
import datetime
import decimal
import types

escape_func=None

def quote(s):
    if isinstance(s,unicode):
        s=s.encode('utf-8')

    if escape_func:
        s=escape_func(s)

    s="'" + s + "'"

#    s="'" + s.replace("\\","\\\\") + "'"
#    s="'" + s.replace("\\","\\\\").replace("'","\\'") + "'"
#    s="'" + s.replace("\\","\\\\").replace("'","''") + "'"

    return s

def nulificar(s): return "NULL"
procesadores = { str : quote ,
                     unicode : quote,
					 int : str,
					 float : str,
                     long : str,
					 datetime.datetime : lambda s: quote(str(s)),
					 bool : str,
					 decimal.Decimal : str,
					 types.NoneType : nulificar,
                     tuple:str
					}
def format(v):
    #if isinstance(v,(tuple,)):
#        print '13'
    ret=procesadores[type(v)](v)

    return ret


def makeInsStr(lstValues,proc=None):
    return reduce(lambda ret,s: ret+','+((s and ((proc and proc(s)) or s)) or 'Null'),lstValues,'')[1:]

def makeUpdStr(KeyVal,proc=None):
    return reduce(lambda ret,(k,v): ret+',%s='%k+((v and ((proc and proc(v)) or v)) or 'Null'),KeyVal,'')[1:]

"""
def genInsert(table,keys,listofvalues,flAsArray=0):
#    if not isinstance(listofvalues,(tuple,list)):
#        listofvalues=[listofvalues]
    ret=''
    if flAsArray:
        ret=[]

    sql='insert into %s'%table
    sIns=sql+((keys and '('+makeInsStr(keys)+')') or '')+' values '
    for vals in listofvalues:
        sVals='('+makeInsStr(vals,format)+')'
        if flAsArray:
            ret.append(sIns+sVals)
        else:
            ret+=sVals
    if not flAsArray:
        ret='('+ret[:-1]+')'

    return ret
"""

def genInsert(table,keys,listofvalues, OnMakeTabName=None, insStatement='insert'):#, fInsertIgnore=1
    """ Generate Insert DML"""
    if not listofvalues:
        raise Exception('genInsert : empty listofvalues')

    ins=''

    table=utf8(table)

    keys=utf8(keys)

    if OnMakeTabName:
        table=OnMakeTabName(table)
        keys=map(OnMakeTabName,keys)

    if not isinstance(listofvalues,(tuple,list)):
        listofvalues=[[listofvalues]]

    if not isinstance(listofvalues[0],(tuple,list)):
        listofvalues=[listofvalues]

    listofvalues=app.utf8(listofvalues)

    try:
        sql=(insStatement+' into %s'%table)#.encode('utf-8')
        vals=reduce(lambda ret,vals : ret+'(%s),'%makeInsStr(vals,format),listofvalues,'')
        ins=sql+((keys and '('+makeInsStr(keys)+')') or '')
        ins=ins+' values '+vals[:-1]+';'
    except:
        print 'genInsert-Error:',table,keys,listofvalues
        app.LogError('',1)
    #for vals in listofvalues:
#        vals
    return ins

def genReplace(table,keys,listofvalues):
    return 'replace '+genInsert(table,keys,listofvalues)[len('insert'):]

def genUpdate(table,IdKey,dKeyVal):
    table=utf8(table)
    dKeyVal=utf8(dKeyVal)
    sql=''
    try:
        sql='update %s set '%table
        sql+=makeUpdStr(dKeyVal,format)
        sql+=' where id=%s'%str(IdKey)
    except:
        print 'genUpdate-Error:',table,IdKey,dKeyVal
        app.LogError('',1)
    #for vals in listofvalues:
#        vals
    return sql

class basedb(object):

    def __init__(self, connectionParams={}):
        self.connectionParams={}
        self.flScript=0
        self.connectionsHistory=[]
        if connectionParams:
            self.connect(connectionParams)

    def connect(self,connectionParams):
        self.connectionsHistory.append(connectionParams)
        self.connectionParams.update(connectionParams)

    def new(self,params):#params={}
        pass

    def new(self,params):#params={'path'}
        pass

    def tables(self):#params={}
        pass

    def indexes(self,TableName):#params={'path'}
        pass

    def values(self,sql):
        pass

    def columns(TableName):
        pass

    def execsql(self,sqlOrArr):
        pass

    def execute(self,sqlOrArr):
        pass

    def script(self,IncludeData=1):
        self.flScript=1
        self.flIncludeData=IncludeData
