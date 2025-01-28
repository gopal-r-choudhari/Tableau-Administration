from datetime import datetime
import psycopg2
import os
import sys
#File to log data
#current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
#file_name = str(current_datetime)

try:
   file_name = sys.argv[1]
   file = open(file_name, 'w')
   file.write("\n********SCRIPT EXECUTION STARTS HERE**********")

   #Database connectivity
   con = psycopg2.connect(database="workgroup", user="user", password="password", host="localhost",port="8060")
   cursor_obj = con.cursor()

   #Get the Site Details
   query_sitecount = "select count(*) from hist_sites"
   cursor_obj.execute(query_sitecount)
   result= cursor_obj.fetchone()
   site_count=0
   for r1 in result:
     site_count=r1
   file.write("\nSITE DETAILS:\nTotal Sites: "+str(site_count)+"\nSite Names:\n")

   #Get the Site name from the server
   query_sitecount = "select distinct name from hist_sites"
   cursor_obj.execute(query_sitecount)
   result= cursor_obj.fetchall()
   for r1 in result:
     file.write(r1[0])
     #print(r1[0])


   #Get the User Details
   query_creator = "select licensing_roles_count from licensing_roles where id=8"
   query_viewer = "select licensing_roles_count from licensing_roles where id=6"
   query_explorer = "select licensing_roles_count from licensing_roles where id=7"
   query_unlicensed = "select licensing_roles_count from licensing_roles where id=3"
   creator=0
   viewer=0
   explorer=0
   unlicensed=0
   total_user=0
   cursor_obj.execute(query_creator)
   result= cursor_obj.fetchone()
   for r1 in result:
     creator=r1

   cursor_obj.execute(query_viewer)
   result= cursor_obj.fetchone()
   for r1 in result:
     viewer=r1

   cursor_obj.execute(query_explorer)
   result= cursor_obj.fetchone()
   for r1 in result:
     explorer=r1

   cursor_obj.execute(query_unlicensed)
   result= cursor_obj.fetchone()
   for r1 in result:
     unlicensed=r1
   total_user = creator + viewer + explorer + unlicensed

   file.write("\n\nUSER DETAILS:")
   file.write("\nTotal User's: "+ str(total_user))
   file.write("\nCreator: "+ str(creator))
   file.write("\nViewer: "+str(viewer))
   file.write("\nExplorer: "+str(explorer))
   file.write("\nUnlicensed: "+str(unlicensed))

   #Get the Schedules Details
   query_schedulecount = "select count(*) from hist_schedules"
   cursor_obj.execute(query_schedulecount)
   result= cursor_obj.fetchone()
   schedule_count=0
   for r1 in result:
     schedule_count=r1
   file.write("\n\nSCHEDULES DETAILS:")
   file.write("\nTotal Schedule: "+str(schedule_count))
   cursor_obj.close()
   con.close()

   #TSM Service Details
   file.write("\n\nTABLEAU PROCESSES DETAILS:\n")
   file.close()
   command1 = "tsm status >> " +file_name
   command2 = "tsm status -v >> " +file_name
   os.system(command1)
   os.system(command2)
   file = open(file_name,"a")
   file.write("\n\nLICENSES DETAILS:\n")
   file.close()
   command3 = "tsm licenses list >> "+file_name
   os.system(command3)
   #file.close()
   file = open(file_name,"a")
   file.write("\n\nSCRIPT EXECUTION END HERE..!\n")
   file.close()
except:
   file = open(file_name,"a")
   file.write("\nError while retriving the details..!\nNeed Manual intervention\nThank you.\n")
   file.close()

