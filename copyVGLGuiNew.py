# Objective: read VGLGui workflow file and load content into memory
# File type: structure.txt

#
import re
import os
import string
from collections import defaultdict

# Structure for storing Glyphs in memory
# Glyph represents a function
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
        self.ready = False            #defines if the glyph is ready to run
        self.done = False             #defines if the glyph was executed
        self.lst_entry = []           #glyph entries list
        self.lst_output = []          #glyph output list

    #Function to add glyph input
    ########
    ######## P E N D E N T E   T E S T A R   S E   E N T R A D A   J A   E X I S T E
    ########
    def funcGlyphAddEnt (self, vinput_varname):
        self.lst_entry.append(vinput_varname)

    #Function to add glyph output
    ########
    ######## P E N D E N T E   T E S T A R   S E   S A Í D A   J A   E X I S T E
    ########
    def funcGlyphAddOut (self, voutput_varname):
        self.lst_output.append(voutput_varname)


# Structure for storing Parameters in memory
class objGlyphParameters(object):

    def __init__(self, vglyph_id, vname, vvalue):
        self.glyph_id = vglyph_id   #glyph identifier code
        self.name = vname           #variable name
        self.value = vvalue         #variable value

# Structure for storing Glyphs entries list in memory
class objGlyphEntry(object):

    def __init__(self, vglyph_id, vnameent):
        self.glyph_id = vglyph_id   #glyph identifier code
        self.nameent = vnameent     #glyph entry name

# Structure for storing Glyphs output list in memory
class objGlyphOutput(object):

    def __init__(self, vglyph_id, vnameout):
        self.glyph_id = vglyph_id   #glyph identifier code
        self.nameout = vnameout     #glyph output name

# Structure for storing Connections in memory
# Images are stored on edges (connections between Glyphs)
class objConnection(object):

    #NodeConnection:data:[output_Glyph_ID]:[output_varname]:[input_Glyph_ID]:[input_varname]        
    def __init__(self, vtype, voutput_glyph_id, voutput_varname, vinput_glyph_id, vinput_varname):       
        self.type = vtype                           #type 'data', 'controle' 
        self.output_glyph_id = voutput_glyph_id     #glyph identifier code output
        self.output_varname = voutput_varname       #variable name output
        self.input_glyph_id = vinput_glyph_id       #glyph identifier code input
        self.input_varname = vinput_varname         #variable name input
        self.image = None                           #image
        self.ready = False                          #False = unread or unexecuted image; True = image read or executed

# File to be read
vfile = 'fileread/data.wksp'

lstGlyph = []                   #List to store Glyphs
lstGlyphPar = []                #List to store Glyphs Parameters
lstConnection = []              #List to store Connections
lstGlyphEnt = []                #List to store Glyphs Entries
lstGlyphOut = []                #List to store Glyphs Outputs

vGlyph = objGlyph               #Glyph in memory 
vGlyphPar = objGlyphParameters  #Glyph parameters in memory
vGlyphEnt = objGlyphEntry       #Glyph entry in memory
vGlyphOut = objGlyphOutput      #Glyph output in memory
vConnection = objConnection     #Connection in memory

# Method for reading the workflow file
def fileRead(lstGlyph):
    try:
        if os.path.isfile(vfile):
            count = 0   #variable to count the lines 
            # Opens the workflow file
            file1 = open(vfile,"r")
            for line in file1:
                count += 1

                # Creates the glyphs of the workflow file
                if 'glyph:' in line.lower():
                    try:
                        contentGly = line.split(':')    #extracts the contents of the workflow file line in a list separated by the information between the ":" character
                        contentGlyPar = []              #clears the glyph parameter list
                        vparName = ''
                        vparValue = ''

                        #Creates the parameters of the Glyph
                        #:: -[var_str] '[var_str_value]' -[var_num] [var_num_value]
                        contentGlyPar = contentGly[9].split(' ')
                        for vpar in contentGlyPar:
                            if vpar != '' and vpar != '\n':
                                vparName = vpar.replace('-', '')                        
                                vGlyphPar = objGlyphParameters(contentGly[5], vparName, 'fixo')
                                lstGlyphPar.append(vGlyphPar)

                                ########
                                ######## P E N D E N T E   A R M A Z E N A R   O S   P A R A M E T R O S
                                ########

                                #if vparName != '' and vparName != vpar:
                                #    vGlyphPar = objGlyphParameters(contentGly[5], vparName, vparValue)
                                #    lstGlyphPar.append(vGlyphPar)
                                #    vparName = ''
                                #    vparValue = ''
                                #else:
                                #    if vpar.find('-') >= 0:
                                #        vparName = vpar.replace('-', '')
                                #    else:
                                #        vparValue = vpar

                        #Create the Glyph
                        vGlyph = objGlyph(contentGly[1], contentGly[2], contentGly[4], contentGly[5], contentGly[6], contentGly[7], lstGlyphPar)
                        lstGlyph.append(vGlyph)
                    except IndexError as d:
                        print("Falta incides no glifo", {d}, "na linha",{count},"do arquivo")
                    #Creates the connections of the workflow file
                    #NodeConnection:data:[output_Glyph_ID]:[output_varname]:[input_Glyph_ID]:[input_varname]        
                if 'nodeconnection:' in line.lower():
                    try:
                        contentCon = line.split(':')
                        vConnection = objConnection(contentCon[1], contentCon[2], contentCon[3], contentCon[4], contentCon[5])
                        lstConnection.append(vConnection)           

                        #Create the entries for the glyph
                        for i, vGlyph in enumerate(lstGlyph):
                            #If the glyph has input
                            if contentCon[5] != '\n' and vGlyph.glyph_id == contentCon[4]:
                                lstGlyph[i].funcGlyphAddEnt (contentCon[5])
                            
                        #Creates the outputs for the glyph 
                            if contentCon[3] != '\n' and vGlyph.glyph_id == contentCon[2]:
                                lstGlyph[i].funcGlyphAddOut (contentCon[3]) 
                    except IndexError as c:
                        print("falta indices nas conexões",{c},"na linha",{count},"do arquivo")
    finally:
        file1.close()

# Program execution
lstGlyph = []
lstConnection = []
contentGly = []
contentCon = []
lstGlyphEnt = []                #List to store Glyphs Entries
lstGlyphOut = []                #List to store Glyphs Outputs

# Reading the workflow file
try:
    fileRead(lstGlyph)
except UnboundLocalError as c:
    print("Arquivo inexistente ou diretório selecionado errado", {c})

# Shows the content of the Glyphs
for vGlyph in lstGlyph:
    print("Library:", vGlyph.library, "Function:", vGlyph.func, "Localhost:", vGlyph.localhost, "Glyph_Id:", vGlyph.glyph_id, 
          "Position_Line:", vGlyph.glyph_x, "Position_Column:", vGlyph.glyph_y)#, "Parameters:", vGlyph.lst_par)
    #show entries
    for vGlyphEnt in vGlyph.lst_entry:
        print("Glyph_Id:", vGlyph.glyph_id, "Glyph_Ent:", vGlyphEnt)
    #show outputs
    for vGlyphOut in vGlyph.lst_output:
        print("Glyph_Id:",vGlyph.glyph_id,  "Glyph_Out:", vGlyphOut)


# Shows the content of the Connections
#for vConnection in lstConnection:
#    print("Conexão:", vConnection.type, "Glyph_Output_Id:", vConnection.output_glyph_id, "Glyph_Output_Varname:", vConnection.output_varname,
#          "Glyph_Input_Id:", vConnection.input_glyph_id, "Glyph_Input_Varname:", vConnection.input_varname)