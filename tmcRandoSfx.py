import sys
import csv
import random
import os

def displayHelp():
    print("\t---TMC SFX Randomizer---\t")
    print("\nUsage:")
    print("python tmcRandoSfx.py -p my_plando_table.csv (output.event) //Will create an .event file with the sfx plandoed according to the table")
    print("                      -r a_folder (output.event) //Will generate an .event with randomized sfx based on the .csv inside the folder")
    print("\n\nMORE INFO:")
    print("For the -p option you need to provide a comma separated .csv, with two columns containing respectively the ids (in decimal) of the sfx you want to replace and the ids (in decimal) of the sfx you want to replace it with\n")
    print("For the -r option, you need to provide a folder with two comma separeted .csv, one named \"to_replace.csv\" with the list of ids (in decimal) of the sfx that will be replaced, and one named \"replacing.csv\" with the ids that will be used to replaced the ones from the first list")
    print("\nUse VG music studio or the music table to find out which id corresponds to which sfx.")

def loadData():
    sfxTableAddress={}
    sfxFileAddress={}
    with open("data") as csvDataFile:
        csvReader=csv.reader(csvDataFile)
        for row in csvReader:
            sfxTableAddress.update({row[0]:row[1]})
            sfxFileAddress.update({row[0]:row[2]})

    return (sfxTableAddress,sfxFileAddress);

def littleEndian(address):
    firstByte=address[0:2]
    secondByte=address[2:4]
    thirdByte=address[4:6]
    return ("0x"+thirdByte + " 0x"+secondByte + " 0x" + firstByte + " 0x08")

def writeFile(name, lines):
    f = open(name, "w")
    f.writelines(lines)
    f.close()

def plandoSfx(plandoFileName,outputName):
    (sfxTableAddress,sfxFileAddress)=loadData()

    lines=["PUSH;\n"]
    with open(plandoFileName) as plandoDataFile:
        csvReader=csv.reader(plandoDataFile)
        for row in csvReader:
            lines.append("// Replacing SFX "+ row[0]+ " with SFX "+ row[1]+"\n")
            line="ORG $"+sfxTableAddress[row[0]]+"; BYTE "+ littleEndian(sfxFileAddress[row[1]])+";\n"
            lines.append(line)

    lines.append("POP;")
    writeFile(outputName,lines)

def randomizeSfx(randoFolder, outputName):
    lines=[]
    replacing=[]
    with open(randoFolder+'/replacing.csv') as replacingDataFile:
        csvReader=csv.reader(replacingDataFile)
        for row in csvReader:
            replacing.append(row[0])

    with open(randoFolder+'/to_replace.csv') as toReplaceDataFile:
        csvReader=csv.reader(toReplaceDataFile)
        for row in csvReader:
            rd=random.randint(0,len(replacing)-1)
            lines.append(row[0]+','+replacing[rd]+"\n")

    writeFile("tmp.csv", lines)
    plandoSfx("tmp.csv",outputName)
    os.remove("tmp.csv")

if __name__ == '__main__':
    if (len(sys.argv)< 3):
        displayHelp()
    elif (sys.argv[1] == "-p"):
        plandoSfx(sys.argv[2], sys.argv[3] if (len(sys.argv)>3) else "output.event")
    elif (sys.argv[1] == "-r"):
        randomizeSfx(sys.argv[2],sys.argv[3] if (len(sys.argv)>3) else "output.event")
    else:
        displayHelp()
