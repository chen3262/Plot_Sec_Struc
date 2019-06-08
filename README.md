<img src ="https://github.com/chen3262/Rectified_Trj/blob/master/pic.png" width="750">

Plot_sec_struct.py is Python script to process and plot the secondary strcuture of a preotrin, which requires inputs files from VMD Timeline > Cal. Sec. Struc ( [tutorial](https://www.ks.uiuc.edu/Training/Tutorials/science/timeline/tutorial_timeline-html/)).

## Requirements
numpy, pandas, matplotlib, seaborn

To check if you have these modules installed, you can either do
```bash
conda list | grep "module_name"
pip list | grep "module_name"
```
If nothing is shown, you will need to install the module using either of the following commands
```bash
conda install module_name
pip install module_name
```
## Preparation Steps
Step 1: Obtain a *.tml output from VMD Timeline > Cal. Sec. Struc.
Step 2: provide the path of the .tml file, output folder path, and adjust the dimension of the picture in line 2-6 of the scripts.

## Download and Testing
```bash
python Plot_Sec_Struct.py
```


## License

Copyright (C) 2019 Si-Han Chen chen.3262@osu.edu
