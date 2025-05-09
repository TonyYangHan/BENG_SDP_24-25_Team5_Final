# Code Repo of Senior Design Team 5 (2024-2025)
## Project: AI-based Detection and 3D Imaging of Suspended Organoid Culture

### Contributions <br>
Note: hour counts are only contributions relevant to this repo <br>
### Yang Han <br>
1. Processed image data of organoids from Raspberry Pi (RPi)
2. Constructed, trained, and tested all AI_model under 
3. Evaluated AI model performance
4. Created all RPi control and data transmission codes listed in this repo under `RPi_control`
5. Contributed 8 hours per week from June 15 - July 20 (2024 summer break), 8 hours per week during FA24 quarter,  6 hours per day from Dec.17 - Jan.5, 12 hours per week during WI25 quarter, 2 hours per week during SP25 quarter. <br>
<br>

**Shadee Hemaidan** <br>
1. Helped with code development
2. Tested the hardware with code (~70 hours total)
<br>

**Camilla Hong** <br>
1. Helped with organoid imaging and code improvements (~40 hours total)
<br>

**Reem Khojah, Ph.D. (PI)** <br>
1. Offered project scope and high-level guidance
<br>

### Content Overview
1. `AI_training` contains jupyter notebook source code for training AI_models.
2. `RPi_control` contains Python scipts that controls the movement of the prototype
3. `Trained_AI_models` contains trained AI models saved as `.keras` files
4. `Simple_segmentation` contains simple segmentation scripts based on `opencv` and `scikit-image`

## Usage
1. Models can be trained, saved, and evaluated by running jupyter notebooks.
- Please change the path names to your own path names before running!
2. Segmentation pipelines are contained in the notebooks
3. Downloading Python scripts to RPi locally can allow the usage of device
4. Prototype can be operated with Graphical User Interface by `ssh` into it via VS Code. <br>
[Link to set up guide](https://docs.google.com/document/d/1Pasej9hr26GGmt-eEhycTkIp9jgyvk-u1y0uANi0hPM/edit?usp=sharing)

### Requirements and Recommendations
1. Hardware for AI training: 
- Google Colab T4 GPU runtime (minimum, because accessibility varies) or <br>
- NVIDIA RTX 4070+ GPU + AMD Ryzen 7+/Intel i7+ CPU (preferred) <br>
- SDSC/AWS purchased runtime (more accessibility compared to Google Colab, more complex usage, more performance) <br>

2. Conda package management is recommended for this project due to complexity of packages <br>
- Necessary packages for AI training can be installed using this command in terminal
```
conda env create -f AI_training_env.yml
```
- Necessary packages on RPi can be installed through conda, pip, or apt. See their manuals for detailed installation guides as some may require more than one line of code :( <br>




