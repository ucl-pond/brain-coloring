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

1. Change to a directory of your choice and install a vagrant VM. I have supplied the Vagrantfile (Singularity recipe) I used to install ubuntu:

  [Vagrantfile](Vagrantfile)

2. Copy the `docker-to-singularity` makefile from this repo:

  ```cp [path/to/ucl-pond/brain-coloring/Makefile_brain-coloring_docker-to-singularity](Makefile_brain-coloring_docker-to-singularity) ./MakeFile```

3. Remove any previous output from `make all`

  ```rm image/mrazvan22_brain-coloring*.img```

4. Run the MakeFile

  ```make all```

You should get some output confirming that the docker container has been converted to a singularity image (located in the `./image` folder):

    Done. Image can be found at: /tmp/mrazvan22_brain-coloring-[datestamp-hash].img

and it should continue to successfully execute Raz's script (although you may get an error if you haven't removed previous Singularity images), with the output ending something like this:

    Saved: 'output/pcaCover/cortical_1.png'

After this, it's your choice of whether to use the Singularity image or the Docker container (check it's available with `docker images`)
