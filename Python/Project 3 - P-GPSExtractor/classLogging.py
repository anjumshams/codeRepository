# classLogging.py
# Anjum Shams
# Digital Forensics
# Desc: Handles Forensic Logging Operations

import logging

class _ForensicLog:
    def __init__(self, logName):
        try:
            # Turn on Logging
            logging.basicConfig(filename= logName,level= logging.DEBUG,
                                format='%(asctime)s %(message)s')
        except:
            print ("Forensic Log Initialization Failure … Aborting")
            exit(0)

    def writeLog(self, logType, logMessage):
        if logType == "INFO":
            logging.info(logMessage)
        elif logType == "ERROR":
            logging.error(logMessage)
        elif logType == "WARNING":
            logging.warning(logMessage)
        else:
            logging.error(logMessage)
        return

    def __del__(self):
        logging.info("Logging Shutdown")
        logging.shutdown()
