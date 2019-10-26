import csv,os
# create new folder
if not os.path.exists('headerRemoved'):
    os.makedirs('headerRemoved')

for csvfile in os.listdir(r'.\removeCsvHeader'):
    if not csvfile.endswith('.csv'):
        continue
    else:
        print('removing header from '+csvfile)
        file=open(os.path.join('removeCsvHeader',csvfile))
        csvrow=[]
        # read csv
        newfile=csv.reader(file)
        for row in newfile:
            # skip 1 row
            if newfile.line_num == 1:
                continue
            csvrow.append(row)
        file.close()

        file=open(os.path.join('headerRemoved',csvfile),'w',newline='')
        newfile=csv.writer(file)
        # write csv
        for row in csvrow:
            newfile.writerow(row)

        file.close()
