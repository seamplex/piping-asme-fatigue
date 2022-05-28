gmsh thermal-fig.geo
convert -trim thermal-mesh.png thermal-mesh.png
# ./svg2pdf.sh thermal-mesh.svg
# gmsh thermal-nodes.geo
pyxplot temp.ppl
