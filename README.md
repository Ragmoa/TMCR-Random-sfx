# TMC SFX Randomizer

## Preresquites:
  - Python 3.7+

## Usage:
``` python tmcRandoSfx.py -p test.csv (output.event)``` -> Will create an .event file with the sfx plandoed according to the table

``` python tmcRandoSfx.py -r Rando_test (output.event)``` -> Will generate an .event with randomized sfx based on the .csv files inside the folder

### MORE INFO
    - For the -p option you need to provide a comma separated .csv, with two columns containing respectively the ids (in decimal) of the sfx you want to replace and the ids (in decimal) of the sfx you want to replace it with
    - For the -r option, you need to provide a folder with two comma separeted .csv, one named "to_replace.csv" with the list of ids (in decimal) of the sfx that will be replaced, and one named "replacing.csv" with the ids that will be used to replaced the ones from the first list
    - Use VG music studio or the music table to find out which id corresponds to which sfx
