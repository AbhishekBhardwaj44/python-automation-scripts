import os
import time
import humanize

parent_path=input("enter the directory name")

def walking(parent_path):
    print(f"starting working on {parent_path}")
    children= os.listdir(parent_path)
    for child in children:
        child_path=os.path.join(parent_path,child)
        if os.path.isfile(child_path):
            child_data=os.stat(child_path)
            print(f"file : {child_path}")

        elif os.path.isdir(child_path):
            walking(child_path)
walking(parent_path)
