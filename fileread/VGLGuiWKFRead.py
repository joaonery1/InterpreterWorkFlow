# Objective: read VGLGui workflow file and load content into memory
# File type: VGLGuiTemplate.wkf

# Glyph object structure
from collections import defaultdict

class objGlyph(object):
        
    def __init__(self, vlibrary, vlocalhost, vglyph_id, vglyph_name, vglyph_x, vglyph_y, vlst_par):
        
        self.library = vlibrary       #library name (Ex: VisionGL)
        self.localhost = vlocalhost   #folder where the image file or library function is located
        self.glyph_id = vglyph_id     #glyph identifier code
        self.glyph_name = vglyph_name #VisionGL image or function name
        self.glyph_x = vglyph_x       #numerical coordinate of the glyph's linear position on the screen 
        self.glyph_y = vglyph_y       #numerical coordinate of the column position of the Glyph on the screen
        self.lst_par = vlst_par       #parameter list


#
import os

# File to be read
vfile = str
vfile = "VGLGui.wkf"

# Structure to store data in memory

# Glyph - graphical representation of an image or function from the VisionGL library
vlibrary = ''    #library name (Ex: VisionGL)
vlocalhost = ''  #folder where the image file or library function is located
vglyph_id = 0    #glyph identifier code
vglyph_name = '' #VisionGL image or function name
vglyph_x = 0     #numerical coordinate of the glyph's linear position on the screen 
vglyph_y = 0     #numerical coordinate of the column position of the Glyph on the screen
vlst_par = []    #parameter list

lstGlyph 

# NodeConnection - graphic representation of the connection between two glyphs
def output_glyph_id = 0 # glyph identifier code output
def input_glyph_id = 0  # glyph identifier code input

#
def WorkflowRead(lstu,lstout,lstinp):
    if os.path.isfile(vfile):
        file1 = open(vfile,"r")
        for line in file1:
            if 'nodeconnection' in line.lower():
                conexao = line.split(':')
                lstu.append(conexao[2])
                lstu.append(conexao[4])
                lstinp.append(conexao[5])
                lstout.append(conexao[3])
                print(conexao)
        file1.close()

# Program execution
lstarestas = []
lstout = []
lstv = []
lstinp = []
WorkflowRead(lstarestas,lstout,lstinp)
print(lstarestas,lstout,lstinp)