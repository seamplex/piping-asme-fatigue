import gmsh
import sys

if (len(sys.argv) != 3):
  print("usage: %s transient time" % sys.argv[0])
  sys.exit(0)
  
transient = int(sys.argv[1])
time = int(sys.argv[2])

gmsh.initialize()
gmsh.merge("../thermal/temp-%d.msh" % transient)


n_steps = int(gmsh.option.getNumber("View[0].NbTimeStep"))
times = []
temps = []

for i in range(n_steps):
  kind, tags, temp, t, _ = gmsh.view.getModelData(0, i)
  temps.append(temp)
  times.append(t)

end_time = t
temp_interpolated = [0] * len(temp)

if time > end_time:
  print("error: time %g larger than end_time %g transient time" % (time, end_time))
  sys.exit(1)


i = 0
while time > times[i]:
  i += 1

alpha = (time-times[i-1])/(times[i]-times[i-1])  
  
# aca dumpeamos el vector suelto, ocupa menos
#vector = open("temp/temp-%d-%d.dat" % (transient, time), "w") 
for j in range(len(temps[i])):
  temp_interpolated[j] = [temps[i-1][j][0] + alpha * (temps[i][j][0] - temps[i-1][j][0])]
  #print(j,temp_interpolated[j])
  #vector.write("%g\n" % temp_interpolated[j][0])
#vector.close()

# aca dumpeamos todo el msh, ocupa mas pero es mas consistente
view_interpolated = gmsh.view.add("temperature")
gmsh.view.addModelData(view_interpolated, 0, "", kind, tags, temp_interpolated)
gmsh.option.setNumber("Mesh.MshFileVersion", 2.2);
gmsh.view.write(view_interpolated, "temp/temp-%d-%d.msh" % (transient, time))

gmsh.finalize()
