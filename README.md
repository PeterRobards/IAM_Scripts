# IAM Scripts

This repository houses python scripts designed to assist with Identity and Access Management (IAM).
The current main file here is `new_pass.py` which creates new passwords based on user provided parameters.
An additional shell script:`new_pass.sh` also facillitates the creation of passwords, but provides less features.
This repository is a work in progress and more scripts will be added as they are developed/needed.

## Getting Started with `new_pass.py`

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Note: this program was built and optimized for Python 3.x - we recommend Python Version=3.8.5 

### Prerequisites

Only Python 3 is essential for running this program, as all the packages used (sys, string, random, secrets, and argparse)
are part of the standard library

Python libraries used by this program:

```
argparse
secrets
random
string
sys
```
If you already know you have an appropriate version of Python installed on your system, you can skip to Usage

If you know you're missing Python3, you can find download the appropriate package for your OS via the link below.
If you're unsure, or you have never installed Python before check out the next section about installing python.

* [Python.org](https://www.python.org/getit/) - Get Python 3.x here



## Installing

First check to see if Python is installed on your system and if so, what version is running. 
How that process works depends largely on your Operating System (OS).

### Linux

Note: Most Linux distributions come with Python preloaded, but it might not be with the latest version
 and you could only have Python 2 instead of Python 3 (which is what this program is written in).
 Double check your system's version by using the following commands:
```
# Check the system Python version
$ python --version

# Check the Python 2 version
$ python2 --version

# Check the Python 3 version
$ python3 --version
```

### Windows

In windows, open ‘cmd’ (Command Prompt) and type the following command.

```
C:\> python --version

```
Using the --version switch will show you the version that’s installed. Alternatively, you can use the -V switch:
```
C:\> python -V

```
Either of the above commands will give the version number of the Python interpreter installed or they will display an error if otherwise.

### Mac OSX

Starting with Catalina, Python no longer comes pre-installed on most Mac computers, and many older models only
have Python 2 pre-installed, not Python 3. In order to check the Python version currently installed on your Mac,
open a command-line application, i.e. Terminal, and type in any of the following commands:

```
# Check the system Python version
$ python --version

# Check the Python 2 version
$ python2 --version

# Check the Python 3 version
$ python3 --version
```
Note:
You’ll want to either download or upgrade to the latest version of Python if any of the following conditions are true:
* None of the above commands return a version number on your machine.
* The only versions you see listed when running the above commands are part of the Python 2.x series.
* Your version of Python 3 isn’t the latest available, which was version 3.8.5 as writing this.

If Python is not already on your system, or it is not version 3.6x or above, you can find
detailed installation instructions for your particular OS, here:

Detailed instructions for installing Python3 on Linux, MacOS, and Windows, are available at link below:

* [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/) - How to install Python3

## Usage

Once you have verified that you have Python 3.x installed and running on your system, using this program is
fairly straight forward. In the same command (or terminal) window that you checked the version number of Python,
run 'python new_pass.py -h' - as shown below there are also a couple of optional arguments:

```
 usage: NewPass.py [-h] [-l LENGTH] [-d DIGITS] [-s SPECIALS]

 optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        password will be provided length. Default value = 16.
  -d DIGITS, --digits DIGITS
                        password will include provided number of digits
  -s SPECIALS, --special_chars SPECIALS
                        password will include provided number of special characters
  -n NUMBER, --number_passwords NUMBER
                        specify number of passwords to be generated

```

If no arguments are specified upon running this program, the program will execute normally using the default settings. 
The default is to generate a single password of sixteen characters that is a random mix of upper and lower case characters. 
The optional arguments shown above allow the user to select the length of the password, how many digits/special characters/letters
their password will contain and the number of passwords to generate.

Operating System specific instructions are included below:

### Linux

If you're in the same directory as this Python's project file, simply enter the following command:

```
# If you only have Python3 installed or Python3 is set as your default
$ python new_pass.py
or
$ python new_pass.py -h

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 new_pass.py
or
$ python3 new_pass.py -h
```
If you're not in the directory where this Python's project file is, you can either navigate there, 
via: cd /Path/to/the/directory/ (substituting the appropriate directory names for your system) and
run the above command. Or you can instead run the below command from your current directory and 
just specify the path to the Python project file (.py), like so:
 
```
# If you only have Python3 installed or Python3 is set as your default
$ python /Path/to/the/directory/new_pass.py
or
$ python /Path/to/the/directory/new_pass.py -h

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 /Path/to/the/directory/new_pass.py
or
$ python3 /Path/to/the/directory/new_pass.py -h
```

### Windows

On some recent versions of Windows, it's possible to run Python scripts by only entering
the name of the file containing this project's code at the command prompt:
```
C:\> new_pass.py
or
C:\> new_pass.py -h
```
If you're in the same directory as this Python's project (.py) file, simply enter the above command,
or you can directly call the python interpreter via the below command: 
```
C:\> python new_pass.py
or
C:\> python new_pass.py -h
```
If you're not in the directory where this Python's project file is, you can either navigate there, 
via: cd /Path/to/the/directory/ (substituting the appropriate directory names for your system) and
run the above command. Or you can instead run the below command from your current directory and 
just specify the path to the Python project file (.py), like so:
```
C:\> python /Path/to/the/directory/new_pass.py
or
C:\> python /Path/to/the/directory/new_pass.py -h
```

### MacOS

If you're in the same directory as this Python's project file, simply enter the following command:

```
# If you only have Python3 installed or Python3 is set as your default
$ python new_pass.py
or 
$ python new_pass.py -h

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 new_pass.py
or
$ python3 new_pass.py -h
```
If you're not in the directory where this Python's project file is, you can either navigate there, 
via: cd /Path/to/the/directory/ (substituting the appropriate directory names for your system) and
run the above command. Or you can instead run the below command from your current directory and 
just specify the path to the Python project file (.py), like so:
 
```
# If you only have Python3 installed or Python3 is set as your default
$ python /Path/to/the/directory/new_pass.py
or
$ python /Path/to/the/directory/new_pass.py -h

# If you have both Python2 and Python3 installed and want to specify Python3
$ python3 /Path/to/the/directory/new_pass.py
or
$ python3 /Path/to/the/directory/new_pass.py -h
```
Upon the successful execution of this project's python (.py) file, the default execution will resemble 
something similar to the results shown below (with the values for the resulting password(s) being different).

```
==> python3 new_pass.py

***** Generating Password(s)... *****


Password(s):

	 fLOPqjoiJLeomMPw

```

## Author

* **Peter Robards** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


