__author__ = 'John Wang'


#requirement:python2.7

import urllib2
import platform
import logging
import re
import time

class hosts(object):

    hostsPathDict = {
        'windows' : 'c:/Windows/System32/drivers/etc/hosts',
        'linux' : '/etc/hosts'
    }

    def __init__(self):
        self.reposUrl = 'https://github.com/racaljk/hosts'

    def getRaw(self, url):
        header ={
                'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'
        }
        request = urllib2.Request(url,headers=header)
        response = urllib2.urlopen(request)
        return response.read()


    def getHostsFile(self, osType):
        hostsPath = self.__getHostsFilePath(osType)
        logging.info('append in ' + hostsPath + '...')

        url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
        content = '#---append by python script---#\n'
        content += self.getRaw(url) + '#---append by python script---#'

        with open(hostsPath,'a+') as f:
            f.write(content)
        f.close()
        print('everything is ok!')

    def cleanLocalHostsFile(self, osType):
        hostsPath = self.__getHostsFilePath(osType)
        readLocalHosts = open(hostsPath, 'a+')

        #get file content
        content = readLocalHosts.read()
        readLocalHosts.close()
        pattern = re.compile('#---append by python script---#[\s\S]*?#---append by python script---#')
        content = pattern.sub('', content)

        writeLocalHosts = open(hostsPath, 'w')
        writeLocalHosts.write(content)
        writeLocalHosts.close()
        logging.info('clean ' + hostsPath + ' complete!')

    def __getHostsFilePath(self, osType):
        if osType == 'Windows':
            hostsPath = self.hostsPathDict['windows']
        elif osType == 'Linux':
            hostsPath = self.hostsPathDict['linux']
        else:
            hostsPath = raw_input('please input your hosts path: ')
        return hostsPath



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    osType = platform.system()
    Hosts = hosts()
    try:
        Hosts.cleanLocalHostsFile(osType)
        Hosts.getHostsFile(osType)
    except:
        logging.error('no permission to modify the hosts file.')
        exit()

    logging.info('this window will be closed after 5s.')
    time.sleep(5)



