#coding=utf-8
__author__ = 'John Wang'

import platform
import logging
import re
import time
try:
    import urllib2
except ImportError:
    import urllib.request

class hosts(object):

    hostsPathDict = {
        'windows' : 'c:/Windows/System32/drivers/etc/hosts',
        'linux' : '/etc/hosts'
    }

    def __init__(self):
        self.website = 'https://www.wzjg520.com/'

    def getRaw(self, url):
        header ={
                'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'
        }

        try:
            request = urllib2.Request(url,headers=header)
            response = urllib2.urlopen(request)
        except:
            request = urllib.request.Request(url, headers=header)
            response = urllib.request.urlopen(request)
        return response.read().decode()


    def getHostsFile(self, osType):
        hostsPath = self.__getHostsFilePath(osType)
        url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
        content = '#---append by python script---#\n'
        content += self.getRaw(url) + '#---append by python script---#'
        logging.info('get hosts data ok!')
        with open(hostsPath,'a+') as f:
            logging.info('append in ' + hostsPath + '...')
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
            try:
                hostsPath = raw_input('please input your hosts path: ')
            except:
                hostsPath = input('please input your hosts path: ')
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

    logging.info('this window will be closed after 5s.')
    time.sleep(5)



