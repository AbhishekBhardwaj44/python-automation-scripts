from fabric.api import *

env.hosts=["192.168.30.135"]
env.user="student"
env.password="redhat2"

def storage():
    run("lsblk")
    run('df -h')
