#!/bin/bash -ex

for i in feenox sed pvpython; do
 if [ -z "$(which ${i})" ]; then
  echo "error: ${i} not installed"
  exit 1
 fi
done

if [ ! -z "$1" ]; then
  what=$1
else
  n_modes=$(echo n_modes | m4 n_modes.m4 -)
  what=$(seq 1 ${n_modes})
fi


if [ ! -z "$2" ]; then
  n=$2
else
  n=40
fi

mkdir -p results

for i in ${what}; do
  feenox anim.fee $i $n

  files=""
  for f in results/mode${i}-*.vtk; do
   files+=$(echo \'$f\',);
  done
  f=$(grep -w ^${i} modes.dat | awk '{print $2}')
  sed s_\'results/mode1-0000.vtk\'_${files}_ new.py | sed s/mode\ i/mode\ ${i}\ --\ ${f}\ Hz/ > mode-${i}.py

  cat << EOF >> mode-${i}.py

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# save animation
SaveAnimation('mode${i}.png', renderView1, ImageResolution=[1920, 1080],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    ImageQuality=100,
    FrameRate=1,
    FrameWindow=[0, ${n}])
EOF

  pvpython mode-${i}.py
  ./genvideo.sh mode${i} 20
  mv mode${i}*.png results
done

ls results/*.vtk | grep -v mode1-0000 | xargs rm -f
