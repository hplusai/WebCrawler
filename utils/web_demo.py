import os, httplib, mimetypes, mimetools
from utils import fsys

body=''
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

def post_multipart(url, fields, files=[]):
    """
    Post fields and files to an http host as multipart/form-data.
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return the server's response page.
    """
    content_type, body = encode_multipart_formdata(fields, files)
#    print content_type, body
    headers = {'Content-Type': content_type,
               'Content-Length': str(len(body))}
    r = urllib2.Request(url, body, headers)
    return urllib2.urlopen(r).read()

def encode_multipart_formdata(fields, files):
    global body
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return (content_type, body) ready for httplib.HTTP instance
    """
    BOUNDARY = mimetools.choose_boundary()
    
##   buf = StringIO()
    CRLF = '\r\n'
    L = []
    for (key, value) in fields:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for fLst in files:
        key,filename=fLst[:2]
        if len(fLst)==3:
            data=fLst[2]
        else:
            data=fsys.GetFileData(filename,Mode='rb')
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, os.path.basename(filename)))
        L.append('Content-Type: %s' % (mimetypes.guess_type(filename)[0] or 'application/octet-stream'))
        L.append('Content-Transfer-Encoding: binary')
        L.append('')
        L.append('%s')
        #sio=StringIO()
        #f=open(filename,'rb')
        #mimetools.encode(f,sio,'base64')
        #f.close()
        #L.append(sio.getvalue())
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body=CRLF.join(L)
    if files:
        body = body%data

    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    fsys.Save2File(r'c:\test1.dat',body, Mode='wb',flSmartSaving=0)
    return content_type, body

#post_multipart('http://www.slil.ru/upload/',[['submit','Sending']],[['file',r'C:\sendme.jpg']])

#encode_multipart_formdata([],[['xml','','']])