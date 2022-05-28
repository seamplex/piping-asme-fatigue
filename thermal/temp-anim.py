import gmsh
import sys

dt = 1

if (len(sys.argv) < 2):
  n = 1
else:
  n = int(sys.argv[1])
  
gmsh.initialize(sys.argv)
gmsh.merge("temp-%d.msh" % n)

gmsh.option.setNumber("General.Trackball", 0);
gmsh.option.setNumber("General.RotationX", 290)
gmsh.option.setNumber("General.RotationY", 2)
gmsh.option.setNumber("General.RotationZ", 25)

gmsh.option.setNumber("General.ScaleX", 1.3)
gmsh.option.setNumber("General.ScaleY", 1.3)
gmsh.option.setNumber("General.ScaleZ", 1.3)

gmsh.option.setNumber("Mesh.SurfaceEdges", 0)
gmsh.option.setNumber("Mesh.SurfaceFaces", 0)
gmsh.option.setNumber("Mesh.VolumeFaces", 0)
gmsh.option.setNumber("Mesh.VolumeEdges", 0)


n_steps = int(gmsh.option.getNumber("View[0].NbTimeStep"))
times = []
temps = []

for i in range(n_steps):
  kind, tags, temp, t, _ = gmsh.view.getModelData(0, i)
  temps.append(temp)
  times.append(t)

end_time = t
temp_inst = [0] * len(temp)
view_inst = gmsh.view.add("Temperature transient #%d" % n) # as in temperature and temporal

#sys.exit()

t = 0
step = 0
i = 1
while t < end_time:
  if t > times[i]:
    while times[i] < t:  
      i += 1
  alpha = (t-times[i-1])/(times[i]-times[i-1])  
  print(t,i,alpha)
  
  for j in range(len(temps[i])):
    temp_inst[j] = [temps[i-1][j][0] + alpha * (temps[i][j][0] - temps[i-1][j][0])]

  gmsh.view.addModelData(view_inst, step, "", kind, tags, temp_inst, t)
  
  step += 1
  t += dt

gmsh.view.remove(0)
gmsh.fltk.initialize()

for i in range(step):
  print(i)  
  gmsh.option.setNumber("View[0].TimeStep", i)
  gmsh.fltk.update()
  gmsh.write("temp-%d-%04d.png" % (n,i))


gmsh.finalize()
print("all frames dumped, now run")
print("ffmpeg -y -framerate 10 -f image2 -i temp-%d-%%04d.png temp-%d.mp4" % (n, n))
print("to get a video")


