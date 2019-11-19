import sys
import json
import csv
import logging
from collections import UserDict

class Node(object):
    def __init__(self, nid, parent, name):
        self.nid = nid
        self.parent = parent
        self.children = []
        self.name = name

class NodeDict(UserDict):
    def addNodes(self, nodes):
        """ Add every node as a child to its parent by doing two passes."""
        for i in (1, 2):
            print("i= " + str(i) )
            for node in nodes:
                print("node " + str(node)  )
                self.data[node.nid] = node
                print("checking childern of " +  str(node.parent ))
                print("checking childern  " + self.data.keys())
                if node.parent in self.data.keys():
                    print("children + " + self.data[node.parent].children)
                    if node.parent != "none" and node not in self.data[node.parent].children:
                        self.data[node.parent].children.append(node)
        #print(self.data)

class NodeJSONEncoder(json.JSONEncoder):
    def default(self, node):
        if type(node) == Node:
            return {"nid":node.nid, "name":node.name, "children":node.children}
        raise TypeError("{} is not an instance of Node".format(node))

if __name__ == "__main__":
    nodes = []
    inputfile = 'rutherford.csv'
    with open(inputfile, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        # Create Entity Type
        for row in csv_reader:
            if line_count == 0:
                    for key in row.keys():
                        logging.debug( "Column name for row 0  %s" %key  )
                    line_count += 1
            print("      path =" + str({row["Path"]}) + "      name =" + str({row["Name"]}) + "    value = " + str({row["Value"]})  +  "DataType = " + str({row["DataType"]})  )
            #path, name, value, opc_server = row.split()
            path = row["Path"]
            #print(" path " + str(row["Path"] ) )
            #path_length = len( path.split("/") )
            #print( "length of path " + str( path_length ) )
            #print( "last value of path " + str( tuple(path.split("/")[path_length-1]  )  ))
            #print("----------------------------")
            name = row["Name"]
            value = row["Value"]
            parent = row["Path"]
            datatype = row["DataType"]
            #print("Parent" + parent + " Name " + name + " Value "  + value  )
            nid = parent + name
            if value != None and path not in nodes:
                #print(" adding " + path + " to nodes")
                #node=Node( path, parent, name)
                nodes.append(path)

        print("Number of entities " + str(len(nodes) ) )
        #for node in nodes:
        #    print("node -------- " + node)

        # Get each Entity Type's get it's metrics
        entity_type_dict = {}
        for node in nodes:
            print("ENTITY TYPE " + node)
            entity_type_dict[node] = {}
            metrics_dict = {}
            entity_type_dict[node]['metrics'] = metrics_dict

            with open(inputfile, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 0
                # Getting metrics for each Entity
                for row in csv_reader:
                    if line_count == 0:
                            for key in row.keys():
                                logging.debug( "Column name for row 0  %s" %key  )
                            line_count += 1
                    path = row["Path"]
                    name = row["Name"]
                    value = row["Value"]
                    parent = row["Path"]
                    datatype = row["DataType"]
                    #print( "path === " + path  + "node === " + node)
                    if node == path and value != None:
                        #print("for node " + node + " adding key metric" + name + " to node" )
                        metrics_dict[name] = value

                i = 0
                for item in  metrics_dict.items():
                    print ("metric key = " +  item[i] + "       value  " + metrics_dict.get(item[i])  )
            # Assign metrics to Entity Type entity_dict[node]['metrics']=metrics_dict
            #print ("Assign metric to Entity = " +  node  )
            #entity_type_dict[node]['metrics'] = metrics_dict
            #for metric in entity_type_dict[node]['metrics'] :
            #    print ("metric " +  metric  )
