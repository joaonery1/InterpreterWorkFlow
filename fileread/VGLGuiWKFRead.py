# Objective: read VGLGui workflow file and load content into memory
# File type: VGLGuiTemplate.wkf

#
import re
import os
import string
from collections import defaultdict

# Structure for storing Glyphs in memory
class objGlyph(object):
        
    def __init__(self, vlibrary, vlocalhost, vglyph_id, vglyph_name, vglyph_x, vglyph_y, vlst_par):       
        self.library = vlibrary       #library name (Ex: VisionGL)
        self.localhost = vlocalhost   #folder where the image file or library function is located
        self.glyph_id = vglyph_id     #glyph identifier code
        self.glyph_name = vglyph_name #VisionGL image or function name
        self.glyph_x = vglyph_x       #numerical coordinate of the glyph's linear position on the screen 
        self.glyph_y = vglyph_y       #numerical coordinate of the column position of the Glyph on the screen
        self.lst_par = vlst_par       #parameter list

# Structure for storing Connections in memory
class objConnection(object):
        
    def __init__(self, voutput_glyph_id, vinput_glyph_id):       
        self.output_glyph_id = voutput_glyph_id    #glyph identifier code output
        self.input_glyph_id = vinput_glyph_id      #glyph identifier code input


# File to be read
vfile = 'fileread/VglGui.wkf'

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
                vGlyph = objGlyph(contentGly[1], contentGly[2], contentGly[3], contentGly[4], contentGly[5], contentGly[6], contentGly[8])
                lstGlyph.append(vGlyph)

            # Creates the connections of the workflow file
            if 'NodeConnection:' in line.lower():
                contentCon = line.split(':')
                vConnection = objConnection(contentCon[1], contentCon[2])
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
