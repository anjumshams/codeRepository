# twocore.py
# Anjum Shams
# Digital Forensics
#Two-Core Password Table Generator

import hashlib 
import time 
import itertools 
import multiprocessing

# Create a list of lower case, upper case, numbers
# and special characters to include in the password table
lowerCase = ['a','b','c','d','e','f','g','h']
upperCase = ['G','H','I','J','K','L']
numbers = ['0','1','2','3']
special = ['!','@','#','$']

# combine to create a final list
allCharacters = []
allCharacters = lowerCase + upperCase + numbers + special

# Define Directory Path for the password files
DIR = 'C:\\PW\\'

# Define a hypothetical SALT value
SALT = '&45Bvx9'

# Define the allowable range of password length
PW_LOW = 2
PW_HIGH = 6

def pwGenerator(size):
    pwList = []
    # create a loop to include all passwords with a length of 3-5 characters
    for r in range(size, size+1):
        for s in itertools.product(allCharacters, repeat=r):
            pwList.append(''.join(s))
        
    # For each password in the list generate an associated md5 hash and utilize the
    # hash as the key 
    #try:
    # Open the output file
    fp = open(DIR+str(size),'w')
    for pw in pwList:
        sha256Hash = hashlib.sha256()
        sha256Hash.update((SALT+pw).encode())        
        sha256Digest = sha256Hash.hexdigest()
        fp.write(sha256Digest +' '+ pw +'\n')
        del sha256Hash
    #except:
    #print'File Processing Error'
    #finally:
    #fp.close()

# Create Main Function
if __name__ =='__main__':    
    startTime = time.time()

    corePool = multiprocessing.Pool(processes=2)
    results = corePool.map(pwGenerator, (2, 5))    
    results = corePool.map(pwGenerator, (3, 4))

    #Create a dictionary for easy lookups
    pwDict = {}

    # For each file
    for i in range(PW_LOW, PW_HIGH):
        #try:
        # Open each of the output files
        fp = open(DIR+str(i),'r', encoding='cp437')
        for line in fp:
            pairs = line.split()
            pwDict.update({pairs[0] : pairs[1]})            
        #except:
            #print'File Handling Error'
            #fp.close()
    
    #calculate the elapsed time
    elapsedTime = time.time() - startTime
    print('Elapsed Time:', elapsedTime,'Seconds')
    print('Passwords Generated:', len(pwDict))
    print()

    #print out a few of the dictionary entries as an example
    cnt = 0
    for key,value in (pwDict.items()):
        print (key, value)
        cnt += 1
        if cnt > 10:
            break;
    print()
    
    #Demonstrate the use of the Dictionary to Lookup a password using a known hash value
    pw = pwDict.get('1dbdfd6de15b28f247ec7e1ec571b9f49098b82a6be400baa0fe0e44aedc4e1c')
    print('Hash Value Tested = 1dbdfd6de15b28f247ec7e1ec571b9f49098b82a6be400baa0fe0e44aedc4e1c')
    print('Associated Password='+ pw)
    fp.close()
