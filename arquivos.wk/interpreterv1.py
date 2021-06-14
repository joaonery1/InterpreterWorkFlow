# from copyGuiWk import lstConnection,lstGlyph,lstGlyphPar,lstNodeParameters


# # Shows the content of the Connections
# # for vConnection in lstConnection:
# #     print("Conexão:", vConnection.type, "Glyph_Output_Id:", vConnection.output_glyph_id, "Glyph_Output_Varname:", vConnection.output_varname,
# #           "Glyph_Input_Id:", vConnection.input_glyph_id, "Glyph_Input_Varname:", vConnection.input_varname)

# for vGlyphPar in lstGlyphPar:
#     print(vGlyphPar.name)

o = True
o1 = False
a = True
a1 = False

mylist = [o,o1,a,a1]

newlist = [x for x in mylist if o==True and a == True]
print(newlist)