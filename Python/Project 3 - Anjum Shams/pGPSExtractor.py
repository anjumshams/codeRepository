# pGPSExtractor.py
# Anjum Shams
# Digital Forensics
# Top level script for GPS data extraction.

import os
import _modEXIF
import _csvHandler
import _commandParser
from classLogging import _ForensicLog

# Offsets into the return EXIFData for
# TimeStamp, Camera Make and Model
TS = 0
MAKE = 1
MODEL = 2

# Process the Command Line Arguments
userArgs = _commandParser.ParseCommandLine()

# create a log object
logPath = userArgs.logPath+"ForensicLog.txt"
oLog = _ForensicLog(logPath)
oLog.writeLog("INFO", "Scan Started")
csvPath = userArgs.csvPath+"imageResults.csv"
oCSV = _csvHandler._CSVWriter(csvPath, oLog)

# define a directory to scan
scanDir = userArgs.scanPath
try:
    picts = os.listdir(scanDir)
except:
    oLog.writeLog("ERROR", "Invalid Directory "+ scanDir)
    exit(0)
    
print ("Program Start")
print()

for aFile in picts:
    targetFile = scanDir+ aFile
    if os.path.isfile(targetFile):
        gpsDictionary, EXIFList = _modEXIF.ExtractGPSDictionary (targetFile)        
        if (gpsDictionary):

            # Obtain Lat Lon values from gpsDictionary
            # Converted to degrees
            # The return value is a dictionary key value pairs
            dCoor = _modEXIF.ExtractLatLon(gpsDictionary)
            if dCoor:
                
                latRef = dCoor.get("LatRef")
                lat = dCoor.get("Lat")
                lonRef = dCoor.get("LonRef")
                lon = dCoor.get("Lon")
                altRef = dCoor.get("AltRef")
                alt = dCoor.get("Alt")
                mapLink = ""
            
                if ( lat and lon and latRef and lonRef):                
                    print (str(lat)+','+ str(lon))         

                # write one row to the output file
                oCSV.writeCSVRow(targetFile, EXIFList[MAKE], EXIFList[MODEL],                                 
                                 EXIFList[TS], latRef, lat, lonRef, lon,                                 
                                 altRef, alt, mapLink)                
                oLog.writeLog("INFO", "GPS Data Calculated for :" +
                              targetFile)
            else:
                oLog.writeLog("WARNING", "No GPS EXIF Data for "+
                              targetFile)
        else:
            oLog.writeLog("WARNING", "No GPS EXIF Data for "+
                          targetFile)
    else:
        oLog.writeLog("WARNING", targetFile + " not a valid file")

# Clean up and Close Log and CSV File
del oLog
del oCSV
