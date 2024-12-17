# _modEXIF.py
# Anjum Shams
# Digital Forensics
# Extract GPS Data from EXIF supported Images (jpg, tiff)

import os 
from classLogging import _ForensicLog
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def ExtractGPSDictionary(fileName):    
    pilImage = Image.open(fileName)
    EXIFData = pilImage._getexif()
    
    # Iterate through the EXIFData
    # Searching for GPS Tags
    imageTimeStamp = ""
    cameraModel = ""
    cameraMake = ""
    gpsDictionary = {}

    if EXIFData:
        for tag, theValue in EXIFData.items():
            # obtain the tag
            tagValue = TAGS.get(tag, tag)            

            # Collect basic image data if available
            if tagValue == 'DateTimeOriginal':
                imageTimeStamp = EXIFData.get(tag)                
            if tagValue == "Make":
                cameraMake = EXIFData.get(tag)
            if tagValue == 'Model':
                cameraModel = EXIFData.get(tag)                 

            # check the tag for GPS
            if tagValue == "GPSInfo":                
                # Found it !
                # Now create a Dictionary to hold the GPS Data
                #gpsDictionary = {}
                # Loop through the GPS Information
                for curTag in theValue:
                    gpsTag = GPSTAGS.get(curTag, curTag)
                    gpsDictionary[gpsTag] = theValue[curTag]

        basicEXIFData = [imageTimeStamp, cameraMake, cameraModel]                
        return gpsDictionary, basicEXIFData
       
    else:
        return None, None
            

# Extract the Latitude, Longitude and altitude Values from the gpsDictionary
def ExtractLatLon(gps):    
    # to perform the calculation we need at least
    # lat, lon, latRef and lonRef
    if ("GPSLatitude" in gps and "GPSLongitude" in gps        
        and "GPSLatitudeRef" in gps and "GPSLongiitudeRef" in gps
        or "GPSAltitudeRef" in gps or "GPSAltitude" in gps ):
        latitudeRef = gps["GPSLatitudeRef"]
        latitude = gps["GPSLatitude"]
        longitudeRef = gps["GPSLongitudeRef"]
        longitude = gps["GPSLongitude"]
        longitudeRef = gps["GPSLongitudeRef"]
        altitudeRef = gps["GPSAltitudeRef"]
        altitude = gps["GPSAltitude"]

        lat = ConvertToDegrees(latitude)
        lon = ConvertToDegrees(longitude)
        
        # Check Latitude Reference
        # If South of the Equator then lat value is negative
        if latitudeRef == "S":
            lat = 0 - lat

        # Check Longitude Reference
        # If West of the Prime Meridian in
        # Greenwich then the Longitude value is negative
        if longitudeRef == "W":
            lon = 0 - lon

        gpsCoor = {"LatRef":latitudeRef, "Lat": lat, "LonRef": longitudeRef, "Lon": lon,
                   "AltRef": altitudeRef,  "Alt": altitude}
        return gpsCoor
    else:
        return None

# Convert GPSCoordinates to Degrees
# Input gpsCoordinates value from in EXIF Format
def ConvertToDegrees(gpsCoordinate):
    floatCoordinate = (gpsCoordinate[0] + gpsCoordinate[1]/60.0 + gpsCoordinate[2]/3600.0)
    return floatCoordinate
   
