# Programming Skills -- Coursework 1
This is a full development framework that implements a sequential version of a two-dimensional predator-prey model with spatial diffusion using Python. <br> 
## Getting started
### Prerequisites
Python 3.0 and up 
### Installing
1. The version of code is **python 3.6.4**, you need to load module at first using the command line as below 
```
$ module load anaconda/python3
```
2. To output PPM files, you need to download several packages using the command line as below      
```
$ pip install -U Pillow
$ pip install -U imageio
```
3. To implement test you need to install **pytest**. Type the following command at the command line
```		
$ pip install -U pytest
```
## Execution
### Code
There are two ways to run the code: running from the command-line in batch mode, or from the interface.
When using batch mode, you can change values of variables (r, a, b, m, k, l, dt, T) and the path of image\_file in "Inputs.txt" which is in the same folder as the py file before executing. Then, you need to type the following command on the command-line. 
```
$ python pumahares_file.py
```
When using interface, you need to run the code by typing the following command on the command-line. After the interface prompting a window, you can change values of variables (r, a, b, m, k, l, dt, T) on the window.
```
$ python pumahares_GUI.py
```

### Test
To run the code you need to type the following command on the command line:
```
$ py.test
```
## Author
* Yeow Tong Yeo s1887493@ed.ac.uk <br>
* Zhiyao Qian s1815492@ed.ac.uk <br>
* Yajuan Zhang s1883916@ed.ac.uk <br>

For any question and for reporting bugs please send an email to us. <br>
