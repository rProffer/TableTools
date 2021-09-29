##This class performs data cleaning. Welcome to your extra hour in the data pit. 
#Author: Robyn Proffer July 2018


## TODO
#I'd like to figure out how to abstract this so that I only ever need one analysis class as opposed to one analysis class built out for each worksheet I pull in.
##

#used libraries and modules
import os
import shutil

class DataPrep:

    '''
    Gets gets and maintains knowledge of which data element resides in which column
    
    '''
    def __init__(self):
        pass
    
    def getHeading(self, headings, data):
        headingtracker = {}
        for item in headings:
            count = -1
            for head in data:
                count+=1
                if head == item:
                    headingtracker[item] = count
        return headingtracker
    
    '''
    DANGEROUS
    '''
    def ClearFolder(self, fold):
        folder = fold
        for file in os.listdir(folder):
            filepath = os.path.join(folder, file)
            try:
                if os.path.isfile(filepath):
                    os.unlink(filepath)
            except Exception as e:
                continue    