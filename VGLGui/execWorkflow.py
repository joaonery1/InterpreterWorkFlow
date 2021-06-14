#from .readWorkflow import lstConnection
import os, sys , inspect

sys.path.append(os.getcwd())
from VGLGui.readWorkflow import lstGlyph,lstConnection,lstGlyphIn,lstGlyphOut


for vGlyph in lstGlyph:
         if vGlyph.getGlyphReady():
             for vConnection in lstConnection:
                 for vGlyphIn in lstGlyphIn:
                     for vGlyphOut in lstGlyphOut:
                         print('oi')
