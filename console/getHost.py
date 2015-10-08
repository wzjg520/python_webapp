__author__ = 'John Wang'


#requirement:python2.7
#more functions will be added in next version

import urllib2
import platform
import logging
import re

class hosts(object):
    def __init__(self):
        self.reposUrl = 'https://github.com/racaljk/hosts'

    def getRaw(self, url):
        header ={
                'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'
        }
        request = urllib2.Request(url,headers=header)
        response = urllib2.urlopen(request)
        return response.read()

    def getReadMeFile(self):
        url = 'https://raw.githubusercontent.com/racaljk/hosts/master/README.md'
        content = self.getRaw(url)
        with open('README.MD','wb') as f:
            f.write(content)

    def getHostsFile(self, osType):
        hostsPath = self.__getHostsFilePath(osType)
        logging.info('append in ' + hostsPath)

        url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
        content = '#---append by python script---#\n'
        content += self.getRaw(url) + '#---append by python script---#'

        with open(hostsPath,'a') as f:
            f.write(content)

        print('everything is ok!')

    def cleanLocalHostsFile(self, osType):
        hostsPath = self.__getHostsFilePath(osType)
        readLocalHosts = open(hostsPath, 'r')
        writeLocalHosts = open(hostsPath, 'w')
        try:
            content = readLocalHosts.read()
            partern = re.compile('#---append by python script---#[\s\S]*?#---append by python script---#')
            content = partern.sub('', content)
            print(content)
            exit()

            writeLocalHosts.write(content)
        finally:
            readLocalHosts.close()
            writeLocalHosts.close()

        logging.info('clean ' + hostsPath + ' complete!')

    def __getHostsFilePath(self, osType):
        if osType == 'Windows':
            hostsPath = 'c:/Windows/System32/drivers/etc/hosts'
        elif osType == 'Linux':
            hostsPath = '/etc/hosts'
        else:
            hostsPath = raw_input('please input your hosts path: ')
        return hostsPath


    def printContributors(self):
        l = ['racaljk', 'andytimes', 'smounives', 'smounives',
             'TimothyGu', 'RellyVadd', 'LyricTian']

        c = []
        [c.append({'author': i,
                   'githubpage': 'https://github.com/'+i}) for i in l]

        print(':D thanks for all contributors:')
        for x in xrange(len(c)):
            for (k,v) in c[x].items():
                print(k+':'+v)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    osType = platform.system()
    Hosts = hosts()
    Hosts.cleanLocalHostsFile(osType)
    #Hosts.getHostsFile(osType)
    



