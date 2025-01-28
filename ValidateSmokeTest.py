import filecmp
import os
import sys
import difflib
import datetime

def compare_files(File1,File2):
   compare = filecmp.cmp(File1,File2)
   if compare == True:
      file.write("\n\nAll things are good, Please find the attached smoke test result for more details.\n\nThank you.!")

   else:
      file.write("\n\nBelow is the difference in smoke test before and after the patch activity.\n\n")
      diffinfo(File1,File2)
      file.write("\n\nThe smoke test details are attached herewith, please take the necessory action.\n\nThank You.!")
      #diffinfo(File1,File2)


def diffinfo(File1,File2):
    file1 = open(File1, "r")
    file2 = open(File2, "r")
    file1_info = file1.readlines()
    file2_info = file2.readlines()
    diff = difflib.unified_diff(file1_info, file2_info, fromfile=File1, tofile=File2, lineterm='', n=0)
    for lines in diff:
        file.write(lines)

try:
    File1 = sys.argv[1]
    File2 = sys.argv[2]
    current_date = datetime.date.today()
    hostname  = sys.argv[3]
    file = open("/home/ax823/pythonscript/emailbody", 'w')
    file.write("Hello Team,\n\nPlease find the below Smoke test analysis, post linux patch activity dated: " +str(current_date) +" on Tableau " + hostname+" Server")
    line_Count1=0
    line_Count2=0
    with open(r"Before_Patch", 'r') as fp:
       line_Count1 = len(fp.readlines())
      # print('Total lines:', line_Count1) 
       fp.close()

    with open(r"After_Patch", 'r') as fp:
       line_Count2 = len(fp.readlines())
       #print('Total lines:', line_Count2)
       fp.close()

    if((line_Count1 > 10) and (line_Count2 > 10)):
      compare_files(File1,File2)
    else:
       file.write("\n\nThe automation script unable to get the required details, need manual intervention, Please take necessory action.\n\n Thank you.!")
    file.close()
except:
    print("all not okay..!")
    file = open("/home/ax823/pythonscript/emailbody", 'w')
    file.write("Hello Team,\n\nPlease find the below Smoke test analysis, post linux patch activity dated: " +str(current_date) +" on Tableau " + hostname+" Server")
    file.write("\n\nThe automation script unable to get the required details, need manual intervention, Please take necessory action.\n\n Thank you.!")
    file.close()
