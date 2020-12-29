# LokiScan

This python script will run several command lines to allow the tool "loki.exe" scan the c drive 
this script need to be located in C under as following 
The file will do the following:
1.	Install loki
2.	Interrupt the scanning process 
3.	Clear the folder “loki\signature-base\yara”
4.	Move the file “Health_Sector_threats_yara_rules.yar” to the target folder
5.	Run the scanning command as required “ "loki.exe --noprocscan -l output_result.txt -p c:\ ”

However, the file needs to be located with the loki.exe in the same folder. Both need to be in the 'C:\yar\loki_0.32.1\loki' so the script can do all the process. Please test and get back to me for any update.  
