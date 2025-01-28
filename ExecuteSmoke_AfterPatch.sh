#!/bin/bash
hostname=$(hostname -f)
#echo $hostname
python SmokeTestAutomate.py After_Patch
python ValidateSmokeTest.py Before_Patch After_Patch $hostname

/usr/bin/mail -s "Patch Activity Smoke test Result: Tableau $hostname Server" -a Before_Patch -a After_Patch user@tableauserver.com < emailbody
echo "Done from ExecuteScript_After..!"
