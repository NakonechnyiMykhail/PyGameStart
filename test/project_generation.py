#!/usr/bin/python

#	06/01/2018
#	m1ss10n
#	v.001
#	Code generation the basic project structure
#	ideas
#	create folders and copy standart files
#	add regular for input path and case for different situations
#	
import os, sys

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            #os.mkdir(directory);
            #os.mkdir( directory, 0755 );
            #print "Path is created"
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
# standart_path = "~/Documents/Projects"
# Path to be created
#path = input("Where do you want to create the structure of project?\rEnter full path:\n")

name = input("Take the name of project:\n")





#createFolder( './' + name + '/' )
#os.cd( path + "/" + name )

#createFolder('./tex')
createFolder( name + '/tex/docs')
createFolder( name + '/tex/docs/multirow')
createFolder( name + '/tex/docs/chapters')
createFolder( name + '/tex/slides')
createFolder( name + '/tex/bib')
createFolder( name + '/tex/includes')
createFolder( name + '/images')
createFolder( name + '/code')
createFolder( name + '/code/src/lib')
createFolder( name + '/code/src/classes')
createFolder( name + '/code/src/')
createFolder( name + '/code/bin')
createFolder( name + '/code/output_data')
createFolder( name + '/code/Debug/src')
createFolder( name + '/uml')

# Creates a folder in the current directory called data



