Quake MDL format (for Blender 2.83)
written by Bill Currie
maintened by epiplon

1. Info
This extension converts a mesh to a compatible .mdl format.
The texture will be converted to 256x256 size and the colors will be mapped
to the equivalent color palette.
Since the last 32 colors in the Quake palette are reserved to full bright 
colors (will glow even in the dark), there's a custom setting to prevent 
textures from getting bright colors.

1. Exporting
- select the mesh
- set a custom property "bright" to:
	> 1: lit colors
	> 0: normal colors
- export to destination file
