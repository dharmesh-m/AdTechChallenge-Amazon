from urlparse import urlparse

class WebsiteAnalyzer:

    def isValidUrl(self, url):
        pr = urlparse(url)
        if len(pr.scheme) > 0 and len(pr.netloc) > 0:
            return True
        else:
            return False
    
    def generateHashCode(self, url):
        return None

    def updatePageList(self, pageUrl):
        pageIndex = self.pageList.index(pageUrl)
        count = self.pageSet[pageUrl]
        self.pageSet[pageUrl] = count + 1
        
        while pageIndex > 0:
            n1 = self.pageSet[self.pageList[pageIndex]]
            n2 = self.pageSet[self.pageList[pageIndex - 1]]

            if n1 > n2:
                self.pageList[pageIndex], self.pageList[pageIndex - 1] = self.pageList[pageIndex - 1], self.pageList[pageIndex]
            else:
                
                break

            pageIndex = pageIndex - 1
            
    def __init__(self):
        self.pageList = []
        self.pageSet = {}

    def reportPageAccess(self, pageUrl):
        #if self.isValidUrl(pageUrl) == False:
        #    return
        
        if pageUrl not in self.pageSet:
            self.pageSet.update({pageUrl:1})
            #print self.pageSet
            self.pageList.append(pageUrl)
            
        else:
            self.updatePageList(pageUrl)

    def getTopNPages(self, N):
        return self.pageList[:N]
        


if __name__ == "__main__":
    wa = WebsiteAnalyzer()
    wa.reportPageAccess("www.abc.com")
    wa.reportPageAccess("www.hello.com")
    wa.reportPageAccess("www.hello.com")
    wa.reportPageAccess("www.hello.com")
    wa.reportPageAccess("www.abc.com")
    wa.reportPageAccess("www.abc.com")
    wa.reportPageAccess("www.awesome.com")
    wa.reportPageAccess("www.awesome.com")
    wa.reportPageAccess("www.awesome.com")
    wa.reportPageAccess("www.awesome.com")
    wa.reportPageAccess("www.abc.com")
    wa.reportPageAccess("www.abc.com")
    print wa.getTopNPages(2)

    
