"""
in designated folder, there will be 4 cons files, 1 original pa2 and 1 original position.txt file. If not copy them in there. 
In that particular folder, there will be a NewParameter.xlsx file that specify the new scan range, intermonth charge, intercomm charge that we are interested in testing. That file need to be ordered in particular format.
Create subfolder old + new and run margin and stress loss each parameter
"""
import glob
import os
import subprocess
from shutil import copy2
import xlrd     # to read excel file and store in a list
from datetime import datetime

""" input """
parent_dir = r"C:\Users\douglas.cao\Documents\Python\ImpactTesting"

""""""""""""
LOG = []    # create an empty list for logging

# 1. find all the files
pa2_pa2 = glob.glob(parent_dir + "\\" + "*.pa2")
position_txt = glob.glob(parent_dir + "\\" + "*_SPANPOS*.txt")
rcCons_scan = glob.glob(parent_dir + "\\" + "*_rc_scan.csv")
rcCons_intermonth = glob.glob(parent_dir + "\\" + "*_rc_intermonth.csv")
rcCons_intercomm = glob.glob(parent_dir + "\\" + "*_rc_intercomm.csv")
rcCons_house = glob.glob(parent_dir + "\\" + "*_house.csv")
TestPara_xlsx = glob.glob(parent_dir + "\\" + "TestParameter.xlsx")

# 2. check if all the pre requisite files exist
if len(pa2_pa2) <1:
    LOG.append("Pa2 file not found")
    pa2_pa2 = "N/a"
else:
    pa2_pa2 = pa2_pa2[0][(len(parent_dir)+1):]
if len(position_txt) < 1:
    LOG.append("Position file not found")
    position_txt = "N/a"
else:
    position_txt = position_txt[0][(len(parent_dir)+1):]
if len(rcCons_scan) < 1:
    LOG.append("RC cons Scan file not found")
    rcCons_scan = "N/a"
else:
    rcCons_scan = rcCons_scan[0][(len(parent_dir)+1):]
if len(rcCons_intermonth) < 1:
    LOG.append("RC cons Intermonth file not found")
    rcCons_intermonth = "N/a"
else:
    rcCons_intermonth = rcCons_intermonth[0][(len(parent_dir)+1):]
if len(rcCons_intercomm) < 1:
    LOG.append("RC cons Intercomm file not found")
    rcCons_intercomm = "N/a"
else:
    rcCons_intercomm = rcCons_intercomm[0][(len(parent_dir)+1):]
if len(rcCons_house) < 1:
    LOG.append("RC cons House file not found")
    rcCons_house = "N/a"
else:
    rcCons_house = rcCons_house[0][(len(parent_dir)+1):]
if len(TestPara_xlsx) < 1:
    LOG.append("New Parameter file not found")
    TestPara_xlsx = "N/a"
else:
    TestPara_xlsx = TestPara_xlsx[0][(len(parent_dir)+1):]

# 3. grab timestamp 
timestamp = pa2_pa2[len(parent_dir) + 1:][4:8]   # in format mmdd
spanit_txt = parent_dir + r"\spanInstr.txt"

# 4. read new parameter file
### 4.1. define function to parse from each parameter sheet to 3 lists
def parse_parameterWb_2_lists(sheet):
    ### 4.1.1. insert every rows in the sheet to Para list
    rowscount = oldsheet.nrows
    colscount = oldsheet.ncols
    Para = []
    records = []
    for x in range(rowscount):
        for y in range(colscount):
            records.append( oldsheet.cell(x,y).value)
        Para.append(records)
        records = []

    ### 4.1.2. append data from Para list into dictionary style lists
    scanrange = []
    intermonth = []
    intercomm = []
    for r in Para:
        if r[0] == 'Scan Range':
            scanrange.append({
                'Commodity':r[1].strip(),
                'Tier':int(r[2]),
                'StartDate':int(r[3]),
                'EndDate':int(r[4]),
                'PriceRange':float(r[5]),
                'VolRange':float(r[6])
            })
        
        elif r[0] == 'Tier Spreads':
            intermonth.append({
                'Commodity':r[1].strip(),
                'Priority':int(r[2]),
                'TierA':int(r[3]),
                'DeltaA':int(r[4]),
                'TierB':int(r[5]),
                'DeltaB':int(r[6]),
                'TierSpread':float(r[7])
            })
        elif r[0] == 'Intercom Spreads':
            intercomm.append({
                'CommGroup':r[1].strip(),
                'Priority':int(r[2]),
                'CommA':r[3].strip(),
                'DeltaA':int(r[4]),
                'CommB':r[5].strip(),
                'DeltaB':int(r[6]),
                'CommSpread':float(r[7])
            })

    ### 4.1.3. convert start date & end date in scan range list 
    for r in scanrange:
        # convert general number to tuple
        start_date = xlrd.xldate_as_tuple(r['StartDate'], 0)
        end_date = xlrd.xldate_as_tuple(r['EndDate'], 0)

        # convert to yyymm format
        start_date = datetime(*start_date[0:5]).strftime("%Y%m") 
        end_date = datetime(*end_date[0:5]).strftime("%Y%m") 

        # update value for key StartDate and EndDate
        r['StartDate'] = start_date
        r['EndDate'] = end_date

    return scanrange, intermonth, intercomm

### 4.2. read old sheet & parse them to lists
oldsheet = xlrd.open_workbook(TestPara_xlsx).sheet_by_name("Old")
oldscanrange, oldintermonth, oldintercomm = parse_parameterWb_2_lists(oldsheet)

### 4.2. read new sheet
newsheet = xlrd.open_workbook(TestPara_xlsx).sheet_by_name("New")
newscanrange, newintermonth, newintercomm = parse_parameterWb_2_lists(newsheet)

# 6. read original pa2 file
### 6.1. read and store each r into original_pa2
with open (pa2_pa2, "r") as temp:
    original_pa2 = temp.readlines()

### 6.2. loop through each fron in original_pa2, store record into 3 lists
origin_scanrange = []
origin_intermonth = []
origin_intercomm = []

for r in original_pa2:
    if r.startswith("B"):
        origin_scanrange.append({
            'comm':r[5:15].strip(),
            'instype':r[15:18].strip(),
            'maturity':int(r[18:24]),
            'volscanrange':r[44:52],
            'futscanrange':r[52:57]
        })
    elif r.startswith("C"):
        origin_intermonth.append({
            'comm':str(r[2:8]).strip(),
            'priority':int(r[10:12].strip()),
            'tiera':int(r[23:25].strip() or 0),
            'deltaa':int(r[25:27].strip() or 0),
            'tierb':int(r[30:32].strip() or 0),
            'deltab':int(r[32:34].strip() or 0),
            'spread':int(r[14:21].strip() or 0)
        })
    elif r.startswith("6"):
        origin_intercomm.append({
            'commgroup':str(r[2:5].strip()),
            'priority':int(r[5:9].strip() or 0),
            'comma':str(r[20:26]).strip(),
            'deltaa':int(r[26:29].strip() or 0),
            'commb':str(r[38:44]).strip(),
            'deltab':int(r[44:47].strip() or 0),
            'spread':int(r[9:12].strip() or 0)
        })

# 7. create old and new subfolder
os.chdir(parent_dir)
os.mkdir(timestamp + " old")
os.mkdir(timestamp + " new")

# 8. re write proposing pa2 file: old and new
### 8.1. loop through original 3 lists, compare to old/new 3 lists
### make amended list of record B, C, 6

### 8.2. write old & new pa2 files in old & new directory


# # 8. write SPAN instruction to re calculate risk array: old and new
# spn = parent_dir + r"\test.spn"
# with open (spanit_txt, "w") as f:
#     f.write ("Load " + r"C:\Users\douglas.cao\Documents\Python\ImpactTesting\proposed.pa2" + "\n")   # load original pa2
#     f.write ("Load " + position_txt + "\n")  # load position file
#     f.write ("CalcRiskArray" + "\n")
#     f.write ("Calc" + "\n") # calculate
#     f.write ("Save " + spn + "\n") # save as spn file 

# 10. copying into subfolder old and new

# # 11. calculate Margin and Stress Risk Capital using new parameter file for old and new
# os.chdir(r"C:\Span4\Bin")
# subprocess.call(["spanitrm.exe",spanit_txt])

# for log in LOG: print (log)
print ("The End.") 