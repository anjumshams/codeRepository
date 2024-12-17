# crackfile.py
# Anjum Shams
# Digital Forensics

import argparse 
import os
import hashlib
import time

pwfile = 'all' 

if __name__ == '__main__':    
    # Process the Command Line Arguments
    parser = argparse.ArgumentParser('Python crackfile')
    parser.add_argument('-f', '--file', required= True, action='store', help="specify the given password file")    
    args = parser.parse_args()
    shadowFile = args.file

    # Mark the start time 
    startTime = time.time()

    #create a dictionary to hold Hash, password pairs for easy lookup
    pwDict = {}
    # Open the pwfile file
    fp = open(pwfile,'r', encoding='cp437')
    for line in fp:
        pairs = line.split()        
        pwDict.update({pairs[0] : pairs[1]})    

    # Open and read the shadowfile and split the pairs.
    SF = open(shadowFile,'r', encoding='cp437')
    for line in SF:
        stripLine = line.strip()
        SFpairs = stripLine.split(':')
            
        # Use the Dictionary to Lookup a password using the hash            
        pw = pwDict.get(SFpairs[1])            
        if pw != None:
            print('Username = '+ SFpairs[0])
            print('Password = '+ pw)
        else:
            print('Hash not found: '+ SFpairs[1])

    #calculate the elapsed time
    elapsedTime = time.time() - startTime
    print('Elapsed Time:', elapsedTime,'Seconds')
    fp.close()
