## Singularity version (alternative to Docker)
Author: Neil P. Oxtoby - n.oxtoby@ucl.ac.uk

These instructions are for a Mac.

Singularity doesn't have a Mac version (as of this writing), so the first step is to install a Vagrant VM:
[sylabs installation guide](https://www.sylabs.io/guides/3.1/user-guide/installation.html?#mac)

Tested on a Mac running OS X Yosemite (10.10.5) using an unsupported (old) version of Docker because I hadn't yet updated to the latest Mac OS:

    Docker Community Edition
    Version 17.09.1-ce-mac42 (21090)
    Channel: stable
    3176a6af01

### 1. Converting Raz's Docker container to a Singularity image

0. Ensure that your Docker daemon is running and that you have installed `github:ucl-pond/brain_coloring` in `path/to/ucl-pond/brain-coloring`

1. Change to a directory of your choice and install a vagrant VM. I have supplied the VagrantFile I used to install ubuntu:

  ```path/to/ucl-pond/brain-coloring```

2. Copy the `docker-to-singularity` makefile from this repo:

  ```cp path/to/ucl-pond/brain-coloring/Makefile_brain-coloring_docker-to-singularity ./MakeFile```

3. Remove any previous iterations

  ```rm image/mrazvan22_brain-coloring*.img```

4. Run the MakeFile

  ```make all```

You should get some output confirming that the docker container has been converted to a singularity image:

    Done. Image can be found at: /tmp/mrazvan22_brain-coloring-[datestamp-hash].img

and then it should successfully execute Raz's script (although you may get an error if you haven't removed previous Singularity images), with the output ending something like this:

    Saved: 'output/pcaCover/cortical_1.png'

After this, it's your choice of whether to use the Singularity image or the Docker container (check it's available with `docker images`)

# === Brain colouring software ===
Author: Razvan V. Marinescu - razvan@csail.mit.edu


INPUT: list of numbers representing pathology at each region in the brain

OUTPUT: brain image coloured according to levels of pathology in those regions


# Installation

## Using the Docker container

In order to remove the need to install blender and the python libraries, we made a container which has blender and this repository already pre-installed and ready to run.

1. Install Docker for your current operating system. For MacOS use this link:
https://docs.docker.com/v17.12/docker-for-mac/install/#download-docker-for-mac

Make sure you run the docker deamon after installing. To check if it installer properly, run:

``` docker info```

If prompted to make an account with dockerhub, skip as you don't need one.

2. Download the docker image with the bundled blender and brain coloring software using:
 ``` docker run -it mrazvan22/brain-coloring ```

The image size may be large (~1GB), so use a good connection. Note that after the download, it will automatically connect to the container. If it connected successfully, you should see the shell as follows:

``` root@e3b175e886db:/# ```

3. Go to the directory and run make

``` cd /home/brain-coloring/ ```

Run the software using the Makefile command:

``` make ```

If successful, you should see the images in output/pcaCover being updated. 

## Using the software

1. simply generate the list of pathology numbers according to the format in data/pcaCover.csv  

1.1 If using docker, copy your input.csv to the docker container 

``` sudo docker cp input.csv 9f52258c25f6:/home/brain-coloring/data```

2. change configuration file config.py
	- input file: set to your input file
	- brain type: pial or cortical
	- colours to show pathology
	- the mapping between your atlas the 3D brain regions that will be coloured
	- image resolution, etc ...
	
3. re-generate images using the Makefile command
	
	``` make ```

3.1. If using docker, copy the image out of the docker container to the home directory ~/ :

``` sudo docker cp 9f52258c25f6:/home/brain-coloring/output/pcaCover/cortical_0.png ~/ ```

