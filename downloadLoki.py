import subprocess
import signal
from shutil import copyfile
import os
import sys

def installLoki():
    procss = subprocess.Popen(['loki.exe'] , stdout=subprocess.PIPE )
    print ("Installation process will start...")
    try:
        while True:
            line = procss.stdout.readline()
            print (line)
            if "Scanning " in str(line):
                signal.CTRL_C_EVENT
                break
                procss.wait(timeout=30)
    except subprocess.TimeoutExpired:
        procss.kill()
        print ("THe processsss Killed")
def changYarFiles():
        print("""Installation finished
        Removing unused files...
         """)
        folder = "C:\yar\loki_0.32.1\loki\signature-base\yara"
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            print ("'"+filename+"' Removed")
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        src = "C:\yar\Health_Sector_threats_yara_rules.yar"
        dst = "C:\yar\loki_0.32.1\loki\signature-base\yara\Health_Sector_threats_yara_rules.yar"
        copyfile(src, dst)
        print ("'Health_Sector_threats_yara_rules.yar' moved")
def runScan():
    """
    procss2 = subprocess.Popen(["loki.exe"," --noprocscan", "-l output_result.txt", "-p c:\\yar\\ "] ,   stdout=subprocess.PIPE )
    print ("Scanning process started .....")
    while True:
        line2 = procss2.stdout.readline()
        print ("Scann...",line2)
        if "Finished LOKI Scan" in str(line2):
            print ("Scanning process Ended ... ")
            sys.exit()"""
    subprocess.run("loki.exe --noprocscan -l outp.txt -p c:\\ ")


def main():

    if os.path.exists('./loki.exe'):
        installLoki()
        changYarFiles()
        runScan()
        sys.exit()
    else:
        print ("""please locate all files in the dirictory
         'C:\yar\loki_0.32.1\loki'
        """)
        sys.exit()
if __name__ == "__main__":
    main()
    sys.exit()
