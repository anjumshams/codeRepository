# csvHandler.py
# Anjum Shams
# Digital Forensics
#Handles all methods related to comma separated value operations.

import csv

# Methods constructor: Initializes the CSV File
# writeCSVRow: Writes a single row to the csv file
# writerClose: Closes the CSV File
class _CSVWriter:
    def __init__(self, fileName, oLog):
        try:
            #Open the file
            self.csvFile = open(fileName, 'w')
            # initialize a csv writer on that file
            self.writer = csv.writer(self.csvFile, delimiter=',',
                                     quoting= csv.QUOTE_ALL, lineterminator='\n')
            #write the header row.
            self.writer.writerow( ('Image Path', 'Make', 'Model', 'UTC Time',
                                   'Lat Ref', 'Latitude', 'Lon Ref','Longitude',
                                   'Alt Ref', 'Altitude', 'Map Link' ) )
        except:
            oLog.writeLog("ERROR","CSV File Failure")            

    def writeCSVRow(self, fileName, cameraMake, cameraModel, utc, latRef,
                    latValue, lonRef, lonValue, altRef, altValue, mapLink):
        
        latStr = '%.8f'%latValue
        lonStr = '%.8f'%lonValue       
        altStr = ' %.8f' % altValue
        locString = latStr + ',' + lonStr
        mapLink = 'https://www.google.com/maps/place/'+locString
        
        self.writer.writerow((fileName, cameraMake, cameraModel, utc,
                             latRef, latStr, lonRef, lonStr, altRef, altStr, mapLink))

    def __del__(self):
        self.csvFile.close()
