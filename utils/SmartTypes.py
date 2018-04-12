#import UserDict
import string
import locale
import itertools, operator
from itertools import groupby
from operator import itemgetter,isMappingType as is_dict

locale.setlocale(locale.LC_ALL, '')

flSmartDictUseHash=1

class MySmartDictExcept(Exception):
    pass

mySDExc=MySmartDictExcept('')

class SmartDict(object):
    def __get_key(_,key):
        return (isinstance(key,(str,unicode)) and ((flSmartDictUseHash and hash(_.__LowFunc(key))) or _.__LowFunc(key))) or key

    def get_base_key(_,key):
        k = _.__get_key(key)
        return _.__dict[k][0]

    def __init__(_,inData=None, CaseLowFunc=string.lower, flSortKeys=None):
        """Constructor: takes conventional dictionary or (tuple or list in format [[key,value],[key1,value1]]
           as input (or nothing)"""
        if flSortKeys is None:
            if inData is None:
                flSortKeys=1

        _.__dict = {}
        _.__LowFunc=CaseLowFunc
        _.__keyList=[]
        _.__keyListIdx={}
        if isinstance(inData,dict):
            inData=inData.items()
        # fill dict
        if isinstance(inData,(tuple,list)):
            for key, val in inData :
                _[key]=val

        if flSortKeys:
            _.__keyList.sort()

    def setdefault(_,k,d):
        if _.has_key(k):
            return _[k]
        else:
            _[k]=d
            return d

    def update(_,d):
        for k,v in d.items():
            _[k]=v

    @classmethod
    def fromseq(_,*args):
        ret=SmartDict()
        if not isinstance(args,(list,tuple)) or len(args)%2==1:
            raise TypeError("SmartDict.fromlist : Arguments must be a sequence of (key,value,key1,value1,...)!!!")

        for i in xrange(0,len(args),2):
            ret[args[i]]=args[i+1]
        return ret
        ##        zip(args[::2],args[1::2])

    def __iter__(_):
        _.__iterPosition = 0
        return(_)

    def get(_, key, failobj=None):
        if not _.has_key(key):
            return failobj
        return _[key]

    def next(_):
        if _.__iterPosition >= len(_.__keyList):
            raise StopIteration
        x = _.__dict[_.__keyList[_.__iterPosition]][0]
        _.__iterPosition += 1
        return x

    def __getitem__(_, key):
        k = _.__get_key(key)
        ret=_.__dict.get(k,mySDExc)
        if ret==mySDExc:
            raise MySmartDictExcept('Key : %s not found in %s'%(key,str(_.__dict)))
        return _.__dict[k][1]

    def __setitem__(_, key, value):
        k=_.__get_key(key)

        if k not in _.__keyListIdx:
            _.__keyList.append(k)
            _.__keyListIdx[k]=None

        _.__dict[k] = (key, value)

## cPickle - load dump
    def __setstate__(_, s): # loads
        ## for compability with Pickle
        if 'dict' in s:
            _.__LowFunc=s.get('LowFunc',None)
            _.__dict.update(s.get('dict',{}))
            _.__keyList.extend(s.get('keyList',[]))
            _.__keyListIdx.update(s.get('keyListIdx',[]))
        else:
            ## cPickle
            _.__dict__.update(s)
##        _.__LowFunc=s.get('LowFunc',None)
##        _.__dict=_.__dict__.get('__dict',{}).update(s.get('dict',{}))
##        _.__keyList=_.__dict__.get('__keyList',[]).extend(s.get('keyList',[]))
##        _.__keyListIdx=_.__dict__.get('__keyListIdx',{}).update(s.get('keyListIdx',[]))
##    def __getstate__(_): # loads
##        return _.__dict__
##        d=_.__dict__
##        d1={}
##        for k,v in d.items():
##            d1[k.replace('_SmartDict','')]=v
##        return d1#_.__dict__

    def has_key(_, key):
        k=_.__get_key(key)
        return k in _.__keyListIdx

    def __len__(_):
        return len(_.__keyList)

    def keys(_):
        return [_.__dict[k][0] for k in _.__keyList]

    def values(_):
        return [_.__dict[k][1] for k in _.__keyList]

    def items(_):
        return [_.__dict[k] for k in _.__keyList]

    def __contains__(_, item):
        return _.has_key(item)

    def __repr__(_):
        items = ", ".join([("%r: %r" % (k,v)) for k,v in _.items()])
        return "{%s}" % items

    def __str__(_):
        return repr(_)

    def __get__( _, instance, owner):
        print instance, owner

    def __set__( _, instance, value):
        print instance, owner

    def __delete__( _, instance):
        print instance, owner

    def __delitem__( _, key):
        k = _.__get_key(key)
        del _.__keyList[_.__keyList.index(k)]
        del _.__keyListIdx[k]
        del _.__dict[k]

    def __setattr__(_, k, v):
        if k.startswith('_SmartDict__'):
            return object.__setattr__(_,k,v)
        if k in _.__keyList:
            _[k] = v
        elif not hasattr(_, k):
            _[k] = v
        else:
            _[k] = v
#            raise AttributeError, "Cannot set '%s', cls attribute already exists" % ( k, )
#        print k, v

    def __getattr__(_, k):
        if k.startswith('_SmartDict__'):
            return object.__getattribute__(_,k)
        if k in _.__dict__:
            return _.__dict__[k]
        if k in _:
            return _[k]
#        print 'Attribute Not found : '+k
#        print _.__dict
        raise AttributeError

    @classmethod
    def test(_):
        test=SmartDict()
        test['Jkjasd']=123
        test['JkjAsd']=666
        if test.has_key('jkjAsd'):
            print 'Ura'

class SimpleObj():
    def __init__(_,*args,**kwargs):
        for i in xrange(len(args)):
            arg=args[i]
            if is_dict(arg):
                #update from arg dict
                _.__dict__.update(arg)
            else:
                # add as i item
                _.__dict__['i'+str(i)]=arg
        _.__dict__.update(kwargs)

def UniqList(lst):
    #return [key for key,_ in groupby(sorted(lst))]
    ret=SmartDict(zip(lst,[None]*len(lst)))
    return ret.keys()

#print UniqList([4,2,3,1,3])

class AttrDict(object):
    """
      simple class to help works with named dicts and tuples
    """
    @classmethod
    def __recursive(_,vals):
        if isinstance(vals,AttrDict):
            return vals
        elif is_dict(vals):
            o=AttrDict()
            o.__dict__.update(vals.__class__([[k,_.__recursive(v)] for k,v in vals.items()]))
            return o
        elif isinstance(vals,(list,tuple)):
            return vals.__class__(map(lambda x : _.__recursive(x),vals))
        else:
            return vals

    def __init__(_,*args,**kwargs):
        ##_.__keys=[]
        if args:
            for x in args:
                if isinstance(x,AttrDict):
                    _.__dict__.update(x.__dict__)
                else:
                    if not is_dict(x):
                        raise Exception("AttrDict(dict) accept only dicts params (or AttrDict) and named arguments on TopLevel. You can use any types inside dicts")
                    else:
                        _.__dict__.update(_.__recursive(x).__dict__)

        if kwargs:
            _.__dict__.update(AttrDict(kwargs).__dict__)

    def items(_):
        return _.__dict__.items()

    def keys(_):
        return _.__dict__.keys()

    def values(_):
        return _.__dict__.values()

    def __contains__(_, item):
        return item in _.__dict__

    def __setitem__(_, key, value):
        _.__dict__.update({key:_.__recursive(value)})

    def __getitem__(_, key):
        return _.__dict__[key]

    @classmethod
    def test(_):
        testObj=AttrDict({'id':5,'vals':{'aaa':3},'a2':[{'a':[0]},2,3]},b=134)
        testObj['b']=23
        testObj['c']=23
        print testObj['b']
        if 'b' in testObj:
            print 'b in dict'
        testObj=AttrDict(testObj)
        for k,v in testObj.items():
            print k,v
##exit(0)

if __name__ == '__main__':
    SmartDict.test()
    AttrDict.test()
