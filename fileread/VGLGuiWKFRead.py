# Objective: read VGLGui workflow file and load content into memory
# File type: structure.txt

#
import re
import os
import string
from collections import defaultdict

# Structure for storing Glyphs in memory
class objGlyph(object):
        
    #Glyph:[Library]:comment::localhost:[Glyph_ID]:[Glyph_X]:[Glyph_Y]:: -[var_str] '[var_str_value]' -[var_num] [var_num_value]    
    def __init__(self, vlibrary, vfunc, vlocalhost, vglyph_id, vglyph_x, vglyph_y, vlst_par):       
        self.library = vlibrary       #library name (Ex: VisionGL)
        self.func = vfunc             #function
        self.localhost = vlocalhost   #folder where the image file or library function is located
        self.glyph_id = vglyph_id     #glyph identifier code
        self.glyph_x = vglyph_x       #numerical coordinate of the glyph's linear position on the screen 
        self.glyph_y = vglyph_y       #numerical coordinate of the column position of the Glyph on the screen
        self.lst_par = vlst_par       #parameter list

# Structure for storing Connections in memory
class objConnection(object):

    #NodeConnection:data:[output_Glyph_ID]:[output_varname]:[input_Glyph_ID]:[input_varname]        
    def __init__(self, vtype, voutput_glyph_id, voutput_varname, vinput_glyph_id, vinput_varname):       
        self.type = vtype                           #type 'data', 'controle' 
        self.output_glyph_id = voutput_glyph_id     #glyph identifier code output
        self.voutput_varname = voutput_varname      #nome variável saída
        self.input_glyph_id = vinput_glyph_id       #glyph identifier code input
        self.input_varname = vinput_varname         #nome variável entrada

# File to be read
vfile = 'fileread/data.wksp'

lstGlyph = []                #List to store Glyphs
lstConnection = []           #List to store Connections
vGlyph = objGlyph            #Glyph in memory 
vConnection = objConnection  #Connection in memory

# Method for reading the workflow file
def fileRead(lstGlyph):
    if os.path.isfile(vfile):

        # Opens the workflow file
        file1 = open(vfile,"r")
        for line in file1:

            # Creates the glyphs of the workflow file
            if 'glyph:' in line.lower():
                contentGly = line.split(':')
                vGlyph = objGlyph(contentGly[1], contentGly[2], contentGly[4], contentGly[5], contentGly[6], contentGly[7], contentGly[8])
                lstGlyph.append(vGlyph)

            # Creates the connections of the workflow file
            if 'nodeconnection:' in line.lower():
                contentCon = line.split(':')
                vConnection = objConnection(contentCon[1], contentCon[2], contentCon[3], contentCon[4], contentCon[5])
                lstConnection.append(vConnection)

        file1.close()

# Program execution
lstGlyph = []
lstConnection = []
contentGly = []
contentCon = []

# Reading the workflow file
fileRead(lstGlyph)

# Shows the content of the Glyphs
for vGlyph in lstGlyph:
    print("Library:", vGlyph.library, "Localhost:", vGlyph.localhost, "Glyph_Id:", vGlyph.glyph_id, "Glyph_Name:", vGlyph.glyph_name,
          "Position_Line:", vGlyph.glyph_x, "Position_Column:", vGlyph.glyph_y, "Parameters:", vGlyph.lst_par)

# Shows the content of the Connections
for vConnection in lstConnection:
    print("Glyph_Output_Id:", vConnection.output_glyph_id, "Glyph_Input_Id:", vConnection.input_glyph_id)
