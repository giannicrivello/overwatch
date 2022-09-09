#!/usr/bin/python3

import os
import sys
import time

class MakeGenerator():
    def __init__(self, pwd):
        self._cached_stamp = 0
        self.pwd = pwd
    def _sort(self, dictionary):
        sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
        file_list = []
        for k,v in sorted_dict.items():
            file_list.append(k)
        return file_list

    def _get_ctime_sorted_files(self, list_files):
        files = list_files
        c_time = []
        for i in list_files:
            c_time.append(os.path.getctime(i))
        return self._sort(dict(zip(files,c_time)))
    def watch(self):
        files = os.listdir(self.pwd)
        watched_files = [os.path.join(self.pwd, basename)for basename in files]
        stamp = os.stat(self.pwd).st_mtime
        if stamp != self._cached_stamp:
            sorted_files = self._get_ctime_sorted_files(watched_files)
            ignored_list = []
            for i in sorted_files:
                if i == "./Makefile":
                    continue
                else:
                    ignored_list.append(i)

            self._cached_stamp = stamp
            string = f'''
# define compiler and compiler flag variables
#
JFLAGS = -d .
JC = javac
#
# Clear any default targets for building .class files from .java files; we 
# will provide our own target entry to do this in this makefile.
# make has a set of default targets for different suffixes (like .c.o) 
# Currently, clearing the default for .java.class is not necessary since 
# make does not have a definition for this target, but later versions of 
# make may, so it doesn't hurt to make sure that we clear any default 
# definitions for these
#
.SUFFIXES: .java .class
#
# Here is our target entry for creating .class files from .java files 
# This is a target entry that uses the suffix rule syntax:
#	DSTS:
#		rule
#  'TS' is the suffix of the target file, 'DS' is the suffix of the dependency 
#  file, and 'rule'  is the rule for building a target	
# '$*' is a built-in macro that gets the basename of the current target 
# Remember that there must be a < tab > before the command line ('rule') 
#
.java.class:
    $(JC) $(JFLAGS) $*.java
#
# CLASSES is a macro consisting of 4 words (one for each java source file)
#
#Register calsses here
CLASSES = {' '.join(ignored_list)} 
        
#
# the default make target entry
#
default: classes
        #add entry point command here
#
# This target entry uses Suffix Replacement within a macro: 
# $(name:string1=string2)
# 	In the words in the macro named 'name' replace 'string1' with 'string2'
# Below we are replacing the suffix .java of all words in the macro CLASSES 
# with the .class suffix
#
classes: $(CLASSES:.java=.class)
#
# RM is a predefined macro in make (RM = rm -f)
#
clean:
    $(RM) *.class ''' 
            with open('Makefile', 'w') as file:
                file.write(string)
                file.close()


if __name__ == "__main__":
    watcher = MakeGenerator("./")
    while True:
        try:
            time.sleep(1)
            watcher.watch()
            #do op
        except KeyboardInterrupt:
            os.kill()
            print("Overwatch stoped")


    


