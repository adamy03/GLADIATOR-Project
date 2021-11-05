# GLADIATOR-Project
Training a superhuman sword fighting agent with Reinforcement Learning and Project Malmo

## How to make a custom environment (by copying a preexisting one)

Clone MineRL

`git clone https://github.com/minerllabs/minerl.git`

Make a new Jupyter Notebook inside of the cloned repo

Navigate to `minerl/minerl/herobraine/env_specs`

Make a copy of `treechop_specs.py` and rename it to `treechop_specs2.py`

Open `treechop_specs2.py` and change the class name (Line 121) to Treechop2. 

Change the kwargs['name'] line (line 124) to MineRLTreechop2-v0


## Model

We will be using a multi headed model with a CNN+GRU+FC base and two FC heads.


### https://adoptium.net/archive.html?variant=openjdk8&jvmVariant=hotspot
