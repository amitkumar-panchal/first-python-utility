import os;
import csv;
import sqlite3;


def insertRecords(recordList):

    print(f'Inserting records to database, please wait...');
    
    processedRecords = 0;
    try:
    
        database = 'D:/Programs/SQLite/data/mydatabase.db';
        
        print(f'Connecting to {database}');
        dbConnection = sqlite3.connect(database);
        
        cursor = dbConnection.cursor();
        
        print(f'Connected to {database}');

        insertQuery = "" "INSERT INTO data (name, lei) VALUES (?, ?);"" ";
    
        cursor.executemany(insertQuery, recordList);
        
        dbConnection.commit();
    
        processedRecords = cursor.rowcount;
        
        dbConnection.commit();
        
        cursor.close();

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error);
        
    finally:
        if (dbConnection):
            dbConnection.close();
            print("Connection is closed");
        
        print(f'{cursor.rowcount} records inserted to database');


def getRecords(csvFilename):

    print(f'Reading {csvFilename}');
    
    fields = ['Name','lei'];
    
    lineCount = 0;

    with open(csvFilename, encoding='utf-8') as csvFile:
    
        csvReader = csv.DictReader(csvFile, delimiter=',');
        records = [];
        lineCount = -1;
        for row in csvReader:
        
                #print(f'Column names are {", ".join(row)}');
                #do nothing
            if (lineCount != 0) :
                record = [row[fields[0]], row[fields[1]]];
                records.append(record);
            
                #print(row[fields[0]], row[fields[1]]);
        
            lineCount += 1;
            
    #print(records);
    print(f'Found {lineCount} records');
    print(f'Reading {csvFilename} completed');
    
    return records;

def getFiles(directory):

    print();
    print(f'Scanning {directory}');
    
    fileList = [];
    fileCount = 0;
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                print(os.path.join(root, file));
                fileList.append(os.path.join(root, file));
                fileCount += 1;
    
    print(f'Found {fileCount} files');
    print(f'Scanning {directory} completed');
    #print(fileList);
    return fileList;

def main():

    # scan a directory
    fileList = getFiles('samples');

    #loop
    for fileName in fileList:
        print();
        print(f'Processing {fileName}, please wait..');
        
        # read a csv and get all records
        list = getRecords(fileName);
    
        # insert into database
        insertRecords(list);
    
        # move csv to backup directory
        # check if any file exists
        # if yes, rename it by suffixing
        # if no, copy it

    
main();


"""

HOW TO RUN
-------------
D:\Workspace\projects>py csv2sqlite.py
   
"""   

