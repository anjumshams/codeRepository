# pGPSFalsifier.py
# Anjum Shams
# Digital Forensics
# This program modifies the latitude, longitude, and timestamp values of an
# existing image file. If the image has EXIF data but no GPS info tag, it creates
# the GPS dictionary “from scratch” with the false information. If the image
# already has a GPS info tag, it replaces its latitude, longitude and time
# values with the falsified ones, leaving the other entries as-is.

import argparse 
import os
import shutil
import piexif
import random
    
# Function to generate fake information using random generator.
def genRandomGPS():
    year = random.randint(2003, 2020)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hr = random.randint(0, 23)
    mins = random.randint(0, 59)
    secs = random.randint(0, 59)
    newTimeStamp = bytes((str(year)+ ':'+ str(month)+ ':'+ str(day)+ ' '+
                    str(hr)+ ':'+ str(mins)+ ':'+ str(secs)), 'ascii') 
    
    latRef = random.randint(0, 1)
    if (latRef == 1):
        newLatRef = bytes('N', 'ascii')
    else:        
        newLatRef = bytes('S', 'ascii')
   
    latDeg = random.randint(0, 89)
    latMin = random.randint(0, 59)
    latSec = random.randint(0, 59)
    newLat = ((latDeg, 1), (latMin, 1), (latSec, 1))   
    
    lonRef = random.randint(0, 1)
    if (lonRef == 1):
        newLonRef = bytes('E', 'ascii')
    else:
        newLonRef = bytes('W', 'ascii')
        
    lonDeg = random.randint(0, 179)
    lonMin = random.randint(0, 59)
    lonSec = random.randint(0, 59)
    newLon = ((lonDeg, 1), (lonMin, 1), (lonSec, 1))     
    
    newGPS = (newLatRef, newLat, newLonRef, newLon)    
    return newTimeStamp, newLatRef, newLat, newLonRef, newLon
    

# Process the Command Line Arguments
if __name__ == '__main__':
    parser = argparse.ArgumentParser('Python gpsFalsifier')
    parser.add_argument('-f', '--file', required= True, action='store', help="specify the original file" )
    parser.add_argument('-n', '--newFile', required= True, action='store', help="name for the fake file")
    args = parser.parse_args()
    file = args.file
    fakeFile = args.newFile

    # Copy the original file to the new filename.
    shutil.copy(file, fakeFile)

    # Load the EXIF data from the input file    
    exifDict = piexif.load(fakeFile)
    Exif = exifDict['Exif']
    GPS = exifDict['GPS']
    
    if Exif:
        print ('Original data:')
        print(exifDict['Exif'][36867], exifDict['Exif'][36868], exifDict['GPS'][1],
              exifDict['GPS'][2], exifDict['GPS'][3], exifDict['GPS'][4])
        print('')       
        
    # Call genRandomGPS to get new falsified dictionary items.
    newTimeStamp, newLatRef, newLat, newLonRef, newLon = genRandomGPS()

    # Add the new GPS dictionary to the EXIF data: exifdata['GPS'] = …
    if Exif:        
        exifDict['Exif'][36867] = newTimeStamp
        exifDict['Exif'][36868] = newTimeStamp
        if GPS:            
            exifDict['GPS'][1] = newLatRef
            exifDict['GPS'][2] = newLat
            exifDict['GPS'][3] = newLonRef
            exifDict['GPS'][4] = newLon
            print('Modified data:')
            print(exifDict['Exif'][36867], exifDict['Exif'][36868],exifDict['GPS'][1],
                  exifDict['GPS'][2], exifDict['GPS'][3], exifDict['GPS'][4])            
        else:
            exifDict['GPS'] = {0: (2, 2, 0, 0), 1: newLatRef, 2: newLat,
                               3: newLonRef, 4: newLon, 5: 0, 6: (81, 1)}
            print(exifDict['GPS'])
            print('GPS dictionary added.')            
    else:
        print('No EXIF data on the image.')

    # Convert the EXIF data to bytes with dump()
    exifBytes = piexif.dump(exifDict)    

    # Insert the false EXIF data bytes in the file.
    piexif.insert(exifBytes, fakeFile)
    



    
