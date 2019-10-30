# author: @mano9733 

class Graph:
    
    graph_dict={}
    
    def addEdge(self,node,neighbour):  
        if node not in self.graph_dict:
            self.graph_dict[node]=[neighbour]
        else:
            self.graph_dict[node].append(neighbour)
            
    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(",node,", ",neighbour,")")
     
    def find_path(self,start,end,path=[],res=[]):
            path = path + [start]  
            #print("path= ")
            print(start)
            #print(" start= "+ start + "end= " +end)  
            if start==end:
                path = path
                res = path
                return res 
            for node in self.graph_dict:
                if start+node in E:
                    #print("in E" + start + node)
                    res = self.find_path(node,end,path,res)
                #print("not in E " + start + node)
            return res

E = ["12", "14", "23", "25", "35", "42", "43", "45"]
x= Graph()
x.addEdge('1', '2')
x.addEdge('1', '4')
x.addEdge('2', '3') 
x.addEdge('2', '5')
x.addEdge('3', '5') 
x.addEdge('4', '2')
x.addEdge('4', '3')
x.addEdge('4', '5') 
x.addEdge('5', '')
print(x.find_path('1', '3'))
