'''
Created on 8/31/2016

@author: ghou
'''


class Properties:
    
    fileName = ''
    
    def __init__(self, fileName):
        self.fileName = fileName
        
    def getProperties(self):   
        try:
            pro_file = open(self.fileName, 'r')
            properties = {}
            for line in pro_file:
                if line.find('=') > 0:
                    strs = line.replace('\n', '').split('=')
                    properties[strs[0]] = strs[1]
        except Exception, e:
            raise e
        else:
            pro_file.close()
        return properties
    
    
if __name__ == "__main__":
    import sys
    sys.path.insert(0, 'D:\\java\\')
    fileName = sys.path[0] + '\\'+ 'webui_fr.properties'
    p = Properties(fileName)
    properties = p.getProperties()
    print properties