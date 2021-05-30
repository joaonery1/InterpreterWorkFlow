# Objective: read VGLGui workflow file and load content into memory
# File type: VGLGuiTemplate.wkf
#
import os

# File to be read
def vfile = str
vfile = "VGLGui.wkf"

# Structure to store data in memory

# Glyph - graphical representation of an image or function from the VisionGL library
def vlibrary = ''    #library name (Ex: VisionGL)
def vlocalhost = ''  #folder where the image file or library function is located
def vglyph_id = 0    #glyph identifier code
def vglyph_name = '' #VisionGL image or function name
def vglyph_x = 0     #numerical coordinate of the glyph's linear position on the screen 
def vglyph_y = 0     #numerical coordinate of the column position of the Glyph on the screen
def vlst_par = []    #parameter list



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