# coding=utf-8
import xlrd
import utils
#from utils import CustomDlg
from utils import app,fileutils
from utils import SmartTypes
#from utils.CustomDlg import *
from utils import mydb
mydb.tmpLoadPrefix='db_'
from utils.mydb import *
import difflib
import math
#import metiz_util
#from metiz_util import *

def GetExcelSheetColsValues(inFname):
    doc=xlrd.open_workbook(inFname, formatting_info=True)
    for sh in doc.sheets():
        merged={}
        for crange in sh.merged_cells:
            rlo, rhi, clo, chi = crange
            merged[(rlo,clo)]=(rhi, chi)

        for col in xrange(sh.ncols):
            for row in xrange(sh.nrows):
                sh.cell_value(row,col)

def ExcelSheets2Db(inFname=None, tab_name='xld', UidOnVal=None):
#    r=ExecSql('select * from xld')
    RefColor=lambda lst : (lst and reduce(lambda ret,i: ret+lst[-1-i]*(256**i),range(len(lst)),0)) or 0
    ind=1
    ex=[]

    if not inFname:
        inFname=fileutils.OpendFileDlg('xls')
        inFname=inFname[0]
        if not inFname:
          return 0

    doc=xlrd.open_workbook(inFname, formatting_info=True)
    for sh in doc.sheets():
        merged={}
        for crange in sh.merged_cells:
            rlo, rhi, clo, chi = crange
#            if rlo==10 and sh.name=='22353':
#                print '123'
            merged[(rlo,clo)]=(rhi, chi)

        for col in xrange(sh.ncols):
            for row in xrange(sh.nrows):
                try:
                    xf_ind=sh.cell_xf_index(row,col)
                except:
                    continue
#                    print row,col
                xf=doc.xf_list[xf_ind]
                xf_border=xf.border
                font=doc.font_list[xf.font_index]
                #if not (sh.number==21 and col==0 and row>=46):
                #    continue
    #            borders=[xf_border.left_line_style,xf_border.right_line_style,xf_border.top_line_style,xf_border.bottom_line_style]
                color=RefColor(doc.colour_map[font.colour_index])
                bgcolor=RefColor(doc.colour_map[xf.background.background_colour_index])
                rhi,chi=0,0
                if (row,col) in merged:
                    rhi,chi=merged[(row,col)]
                val=sh.cell_value(row,col)

                uid=(UidOnVal and UidOnVal(val)) or ''
#заменили на 10 ибо падает -> math.trunc(sum([sh.colinfo_map[i].width for i in xrange(chi,col+1)])/100)
                vals=[ind,sh.number,sh.name,col,chi,row,rhi,'10',font.name,font.bold,font.height/20,color,bgcolor,xf_border.left_line_style,xf_border.right_line_style,xf_border.top_line_style,xf_border.bottom_line_style,val,uid]
                ex+=[vals]
                ind+=1

    #            borders_count=filter(None,borders)
    #            if borders_count>:
    #return 1
    names=['id','sheet','sheet_name','col','col_to','row','row_to','col_width','font','font_bold','fontsize','color','bgcolor','lb','rb','tb','bb','val','uid']
    fldTypes=['int']*len(names)
    fields=SmartTypes.SmartDict(zip(names,fldTypes),flSortKeys=0)
    fields['sheet_name']='varchar(100)'
    fields['font']='varchar(50)'
    fields['val']='varchar(500)'
    fields['uid']='varchar(500)'
    CreateTable(tab_name,fields,ex,1,0,0,10,1)
    return 1
