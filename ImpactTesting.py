"""
in designated folder, there will be 4 cons files, 1 original pa2 and 1 original position.txt file. If not copy them in there. 
In that particular folder, there will be a NewParameter.xlsx file that specify the new scan range, intermonth charge, intercomm charge that we are interested in testing. That file need to be ordered in particular format.
Create subfolder old + new and run margin and stress loss each parameter
"""
import glob
import os
import subprocess
from shutil import copy2

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
    pa2_pa2 = pa2_pa2[0]
if len(position_txt) < 1:
    LOG.append("Position file not found")
    position_txt = "N/a"
else:
    position_txt = position_txt[0]
if len(rcCons_scan) < 1:
    LOG.append("RC cons Scan file not found")
    rcCons_scan = "N/a"
else:
    rcCons_scan = rcCons_scan[0]
if len(rcCons_intermonth) < 1:
    LOG.append("RC cons Intermonth file not found")
    rcCons_intermonth = "N/a"
else:
    rcCons_intermonth = rcCons_intermonth[0]
if len(rcCons_intercomm) < 1:
    LOG.append("RC cons Intercomm file not found")
    rcCons_intercomm = "N/a"
else:
    rcCons_intercomm = rcCons_intercomm[0]
if len(rcCons_house) < 1:
    LOG.append("RC cons House file not found")
    rcCons_house = "N/a"
else:
    rcCons_house = rcCons_house[0]
if len(TestPara_xlsx) < 1:
    LOG.append("New Parameter file not found")
    TestPara_xlsx = "N/a"
else:
    TestPara_xlsx = TestPara_xlsx[0]

# 3. grab timestamp 
timestamp = pa2_pa2[len(parent_dir) + 1:][4:8]   # in format mmdd
spanit_txt = parent_dir + r"\spanInstr.txt"

# 4. read new parameter file

# 5. parse them in 3 lists

# 6. read original pa2 file

# 7. re write proposing pa2 file: old and new

# 8. write SPAN instruction to re calculate risk array: old and new
spn = parent_dir + r"\test.spn"
with open (spanit_txt, "w") as f:
    f.write ("Load " + r"C:\Users\douglas.cao\Documents\Python\ImpactTesting\proposed.pa2" + "\n")   # load original pa2
    f.write ("Load " + position_txt + "\n")  # load position file
    f.write ("CalcRiskArray" + "\n")
    f.write ("Calc" + "\n") # calculate
    f.write ("Save " + spn + "\n") # save as spn file 

# 9. make old and new subfolder
os.chdir(parent_dir)
os.mkdir(timestamp + " old")
os.mkdir(timestamp + " new")

# 10. copying into subfolder old and new

# 11. calculate Margin and Stress Risk Capital using new parameter file for old and new
os.chdir(r"C:\Span4\Bin")
subprocess.call(["spanitrm.exe",spanit_txt])

for log in LOG: print (log)
print ("The End.") 