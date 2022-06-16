from xml.etree import ElementTree
from xml.dom import minidom
import os
import re
import sys

POM_FILE="pom.xml"

namespaces = {'xmlns' : 'http://maven.apache.org/POM/4.0.0'}
tree = ElementTree.parse(POM_FILE)
root = tree.getroot()
rel_ver = root.find("./xmlns:version", namespaces=namespaces)
rel_gid = root.find("./xmlns:groupId", namespaces=namespaces)
rel_aid = root.find("./xmlns:artifactId", namespaces=namespaces)
#print(rel_ver.text)
#print(rel_gid.text)
file = open("output/artifact.properties", "w")
file.write("GAVC=" +rel_gid.text + ":" + rel_aid.text + ":" +rel_ver.text)
file.close
