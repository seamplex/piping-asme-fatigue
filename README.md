# Cloud-first thermomechanical analysis of fatigue in nuclear piping with FeenoX

This repository contains all the input data files to run the imaginary case study discussed in [xxx].
The scripts and input files contained in this repository are designed to be run in a cloud server.

## Setting up the server

Start with a fresh instance running a recent version of any GNU/Linux distribution, preferably Debian or Ubuntu.

The two mandatory tools are

 * [Gmsh](http://gmsh.info/), a free and open source three-dimensional finite element mesh generator
 * [FeenoX](https://www.seamplex.com/feenox), a free and open source finite element(ish) solver
 
You can, in decreasing order of complexity and efficiency, either

 a. compile them from source, or
 b. use a precompiled static binary, or
 c. install the distribution's packaged version (only for Gmsh).
 

### Use a binary


### Compile from source



In order to run the case, besides a working POSIX environment (i.e. Bash, M4, awk, etc.) the following two programs are needed:

 * [Gmsh](http://gmsh.info/), a three-dimensional finite element mesh generator with built-in pre- and post-processing facilities
 * [Fino](https://www.seamplex.com/fino), a free finite element solver

To plot results and figures, it is also needed

 * [Pyxplot](http://www.pyxplot.org.uk/) 
 * [Paraview](https://www.paraview.org/)
 
To generate the nicely-formatted tables with the fatigue cumulative usage factors, you also needed
 * [XeLaTeX](http://xetex.sourceforge.net/)

Some other standar tools such as `m4` and `awk` are also needed, which are usually provided by the operating system. 

## Quick instructions

These instructions show how to install all the requirements and make a quick run of the case in a fresh Ubuntu\ 20.04 box.
It is assumed that users of other distributions (as me) know what needs to be modified in order to make everything work.

```
sudo apt-get install
```

### GNU/Linux



Fino and Gmsh are better installed from their webpages:

```
gmsh_version=4.6.0
wget http://gmsh.info/bin/Linux/gmsh-${gmsh_version}-Linux64.tgz
tar xzf gmsh-${gmsh_version}-Linux64-sdk.tgz
sudo cp gmsh-${gmsh_version}-Linux64-sdk/bin/gmsh /usr/local/bin
```

```
fino_version=0.7.98-gf08ed0c
wget https://seamplex.com/fino/dist/linux/fino-v${fino_version}-linux-amd64.tar.gz
tar xzf fino-v${fino_version}-linux-amd64.tar.gz
sudo cp fino-v${fino_version}-linux-amd64/bin/fino /usr/local/bin
```

The other required tools can be installed from standard repositories:

```
sudo apt-get install awk m4 pyxplot paraview paraview-python
```



## Execution

Take a look at the file `lcs_geo`. By default a coarse mesh is created in order to allow a quick execution:

```
lc_thermal = 48;
lc_pipe = 48;
lc_actuator = 150;
```

Execute the top-level `run.sh` directory

```
./run.sh
```


### Transient data

```
cd transients
./run.sh
./plot.sh
cd ..
```


### Primary stresses

This subject is not discussed in the case study text.

```
cd primary
./run.sh
cd ..
```

### Modal analysis

```
cd modal
./run.sh
cd ..
```

### Transient thermal conduction

```
cd thermal
./run.sh
cd ..
```

### Secondary stresses

```
cd secondary
./run.sh
cd ..
```

### Fatigue analysis

```
cd fatigue
./run.sh
cd ..
```




# malla



# primary

Al correr `run.sh` se calcula las tensiones primarias y se comparan con los limites de ASME

# transients

En `orig` están las definiciones de los transitorios tal como estaban en las planillas.
Al correr `run.sh`  se generan los `.dat` y los PDFs.

# thermal

