#import the necessary libraries
import ftplib
import os
import shutil
import time
import schedule
import logging


def Auto_File_Transfer():

    # Create an object instance of ftplib and connect to the server using hostname, username and password
    ftp_server = ftplib.FTP('hostname', 'username','password')

    # list the files in the server directory
    filenames=ftp_server.nlst()

    # check for the existence of the local directory and if it doesn't exist, create one 
    # specify the path of your local directory
    local_dir_path=r'C:\input your dir path'

    # use a for loop to run through the server files, download and write each file to your local directory
    for file in filenames:

        # Add the files in the server directory to your local file path using os.path.join
        local_file=os.path.join(local_dir_path, file)

        try:
            # Download the files in the server directory and write them to your local directory
            # The 'with','as' is a quick way to open, perform operations and close the local file/directory
            with open(local_file, 'wb') as File:
                ftp_server.retrbinary(f'RETR {file}', File.write)
                print('Operation successful')
            
            # Create a log file to keep records of the script excecutions
            logging.basicConfig(filename="logfilename.log", level=logging.DEBUG,format="%(asctime)s %(message)s")
            logging.info("Operation successful")
        except:
            print('An error occured during operation')
            logging.basicConfig(filename="logfilename.log", level=logging.DEBUG,format="%(asctime)s %(message)s")
            logging.warning("An error occurred during operation")
    
    # Close connection to the server
    ftp_server.quit()

Auto_File_Transfer()

# Use the shutil library to move the downloaded and stored files (source) into an internal network (destination) 
source_path=r'C:\input your source path'
dest_path=r'input your destination path'
shutil.move(source_path,dest_path)

# Use the schedule library to run the script daily at a specfic time with the function as an input
schedule.every().day.at("HH:MM").do(Auto_File_Transfer)
while True:
     schedule.run_pending()
     time.sleep(1)