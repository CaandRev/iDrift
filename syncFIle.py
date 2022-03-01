from shutil import copy2
import glob
import os

# Kopiere ifc filer til
def cifc(inpath,outpath):
    dst=[]
    for src in glob.glob(inpath +"*.ifc"):
        # bygg= i[]
        spos=(src.rfind("\\")+1)
        lenght=len(src)
        bygg =src[spos:lenght]
        dst = outpath + bygg
        copy2(src, dst,follow_symlinks=True)
        print(dst)
    print("\n")

 #Kopiere dwg filer

def cdwg(inpath,outpath):    
    dst =[]
    if not os.path.exists(outpath):
        os.mkdir(outpath)
    else :
        print("Mappen eksistere")

    for src in glob.glob(inpath+"*.dwg"):
        # bygg= i[]
        spos=(src.rfind("\\")+1)
        lenght=len(src)
        bygg =src[spos:lenght]
        dst = outpath + bygg
        copy2(src, dst,follow_symlinks=True)
        print(dst)

dropifc = "C:\\Users\\caand\Dropbox\\Gaupne barnehage, planlegging av utviding 2021-22\\12. BIM\\12.1 Fagmodeller\\"
dropdwg = "C:\\Users\\caand\Dropbox\\Gaupne barnehage, planlegging av utviding 2021-22\\12. BIM\\12.2 DWG\\"
destifc1 = "X:\\nor\\oppdrag\\Sogndal\\521\\03\\52103332\\BIM\\Felles\\"
destifc2 = "X:\\nor\\oppdrag\\Sogndal\\521\\03\\52103332\\BIM\\Innsynsmodell\\"
destdwg = "X:\\nor\\oppdrag\\Sogndal\\521\\03\\52103332\\BIM\\Felles\\Import\\"
# destifc1 = "C:\\Users\\caand\\OneDrive - Norconsult Group\\Trans\\"
#destdwg = "C:\\Users\\caand\\OneDrive - Norconsult Group\\Trans\\"

# # Kopiere ifc filer til
cifc(dropifc, destifc1)
cifc(dropifc, destifc2)

#Kopiere dwg filer
cdwg(dropdwg, destdwg)
    
print("Succes")
