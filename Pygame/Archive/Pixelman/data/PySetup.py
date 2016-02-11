#! usr/bin/env python

# Alot of this script is from Pete Shinners pygame2exe script.
# Special thanks to him!

# import modules
from distutils.core import setup
import sys, os, shutil, pygame
import py2exe

print """PySetup.py
Created by Michael Burns
Some of the code was taken from Pete Shinners' pygame2exe script


"""


script = "Pixelman.pyw"      # Starting .py or .pyw script
dest_file = "Pixelman"       # Final name of .exe file
dest_folder = "Pixelman windows-v2.5"     # Final folder for the files
icon_file = "data/icon.ico"  # Icon file. Leave blank for the pygame icon.
extra_data = ["data",        # Extra data to copy in the final folder
              "README.txt",
              "LICENSE.txt"]
extra_modules = ["lib"]      # Extra modules to be included in the .exe
dll_excludes = []            # excluded dlls ["w9xpopen.exe", "msvcr71.dll"]

# Stuff to show who made it, etc.
copyright = "Copyright (C) 2007, Michael Burns"
author = "Michael Burns"
company = "Mindstorms"
version = "2.5"


# Run the script if no commands are supplied 
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")


# Use the pygame icon if there's no icon designated
if icon_file is '':
    path = os.path.split(pygame.__file__)[0]
    icon_file = '' + os.path.join(path, 'pygame.ico') 


# Copy extra data files
def installfile(name):
    dst = os.path.join(dest_folder)
    print 'copying', name, '->', dst
    if os.path.isdir(name):
        dst = os.path.join(dst, name)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(name, dst)
    elif os.path.isfile(name):
        shutil.copy(name, dst)
    else:
        print 'Warning, %s not found' % name
        

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.version = version
        self.company_name = company
        self.author = author
        self.copyright = copyright
        self.name = dest_file

target = Target(

    script = script,
    icon_resources = [(1, icon_file)],
    dest_base = dest_file,
    extra_modules = extra_modules
    )


# Create the executable
setup(
    options = {"py2exe": {"compressed": 1,
                          "optimize": 2,
                          "ascii": 1,
                          "bundle_files": 1,
                          "dll_excludes": dll_excludes,
                          "dist_dir": dest_folder}},
    zipfile = None,
    windows = [target],
    )


# install extra data files
print '\n' # Just a space to make it look nicer :)
for d in extra_data:
    installfile(d)

# If everything went okay, this should come up.
raw_input('\n\n\nConversion successful! Press enter to exit')
