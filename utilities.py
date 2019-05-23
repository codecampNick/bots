import csv

class CsvFunctions:
    def createCsv(self,filePath, fileMode, job):
        with open('testFile.csv',mode='w') as testFile:
            writer = csv.DictWriter(testFile, fieldnames=list(job.__dict__))
            writer.writeheader()
        print('Headers Created!!')
    
    def addCsvRows(self, fileMode, job):
        props = []
        for key, value in job.__dict__.items():
            props.append(value)

        with open('testFile.csv',mode='a') as testFile:
            writer = csv.writer(testFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(props)
        print('Adding rows!')
        