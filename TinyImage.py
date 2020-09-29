import os
import tinify
import pathlib

'''Stick this in the directory with files to optimize'''

class Program:
    def __init__(self):
        self.createVars()
        self.getListOfFiles(self.dirName)
        if len(self.imageList) > 0:
            self.optimizeFiles()
    
    def createVars(self):
        tinify.key = '*********' #Get a key from TinyPNG
        self.dirName = os.getcwd()
        self.imageList = []
        
    def getListOfFiles(self, dirName):
        fileList = os.listdir(dirName)
        suffixList = ['.jpg', '.jpeg', '.png']
        for file in fileList:
            suffix = pathlib.Path(file).suffix
            if suffix in suffixList:
                self.imageList.append(file)

    def optimizeFiles(self):
        for imageFile in self.imageList:
            source = tinify.from_file(imageFile)
            suffix = pathlib.Path(imageFile).suffix
            prefix = imageFile.strip(suffix)
            source.to_file(prefix+'_Optimized'+suffix)        
        
prog = Program()
