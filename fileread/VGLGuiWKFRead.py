# Objective: read VGLGui workflow file and load content into memory
# File type: VGLGuiTemplate.wkf

#
import re
import os
import string

# Glyph object structure
from collections import defaultdict

# Structure to store data in memory
class objGlyph(object):
        
    def __init__(self, vlibrary, vlocalhost, vglyph_id, vglyph_name, vglyph_x, vglyph_y, vlst_par):       
        self.library = vlibrary       #library name (Ex: VisionGL)
        self.localhost = vlocalhost   #folder where the image file or library function is located
        self.glyph_id = vglyph_id     #glyph identifier code
        self.glyph_name = vglyph_name #VisionGL image or function name
        self.glyph_x = vglyph_x       #numerical coordinate of the glyph's linear position on the screen 
        self.glyph_y = vglyph_y       #numerical coordinate of the column position of the Glyph on the screen
        self.lst_par = vlst_par       #parameter list

# File to be read
vfile = 'VGLGui.wkf'

# Glyph - graphical representation of an image or function from the VisionGL library
vlibrary = ''    #library name (Ex: VisionGL)
vlocalhost = ''  #folder where the image file or library function is located
vglyph_id = 0    #glyph identifier code
vglyph_name = '' #VisionGL image or function name
vglyph_x = 0     #numerical coordinate of the glyph's linear position on the screen 
vglyph_y = 0     #numerical coordinate of the column position of the Glyph on the screen
vlst_par = []    #parameter list

# List to store glyphs
lstGlyph = []

# NodeConnection - graphic representation of the connection between two glyphs
#def output_glyph_id = 0 # glyph identifier code output
#def input_glyph_id = 0  # glyph identifier code input

#
def fileRead(lstGlyph):
    if os.path.isfile(vfile):
        file1 = open(vfile,"r")
        for line in file1:
            if 'Glyph' in line.lower():
                conteudo = line.split(':')
                for column in conteudo:
                    lstGlyph.append(conteudo)
        file1.close()

# Program execution
lstGlyph = []
fileRead(lstGlyph)
print(lstGlyph)