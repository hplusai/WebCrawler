# coding=utf-8
import utils
from utils import web_crawler

def WikiTest():
    url,pars=r'https://en.wikipedia.org/wiki/Freedom',['.//*[@id="firstHeading" and contains(.//text(),"Freedom")]','//*[@id="bodyContent"]']
    print('LXml',web_crawler.ParseAndSaveXDoc(url,pars))
    print('Done : Web Crawler Test')

def Tests():
    WikiTest()

if __name__=='__main__':
    #more tests will be added - need to collect them
    # threads,
    #different web getters (download mechanics),
    #gFile (auto download file links
    #Store to any db and datastructure.
    # will be added step by step. with Clean websites =)
    print(Tests())
