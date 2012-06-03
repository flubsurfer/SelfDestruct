import os

# __file__ is a global attribute in python which is the pathname of the file from which the module was loaded, if it was loaded from a file
#since __file__ is relative to path, you'll need to use os.path.abspath(__file__) to get the actual path to the file
thisfile = os.path.abspath ( __file__ )

#deletes current file using path and name given by 'thisfile' variable
os.remove(thisfile)

#getcwd shows current working directory
thisdir = os.getcwd()
os.remove(thisdir)

#a much more straightforward way to remove the directory
#os.rmdir(thisdir)

