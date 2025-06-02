import queue

class Node :
    def __init__(self,data,left=None,right=None):
        
        self.data = data
        self.left = left
        self.right =right
        
        
class TreeNode :
    def __init__(self):
        self.root = None
        
    def inserting(self,data) :
        new_node = Node(data)
        
        if self.root is None :   
            self.root = new_node        
            return
    
        current = self.root
        
        while True :
            if new_node.data > current.data :
                if current.right is None :
                    current.right = new_node
                    
                else :
                    current = current.right
                    

                    
            elif new_node.data < current.data :
                if current .left is None :
                    
                    current.left =new_node 
                else :
                    current = current.left
                    
            else :
                return        
                                       
    def search(self,search_value) :
        
        if self.root is None :
            return
        
        current =self.root
        while current :
            if search_value == current.data :
                
                return True
            
            elif search_value > current.data :
                current = current.right 
                
            else :
                current = current.left
                
        return False          
    
    
    
    

    
    
    def delete(self,value) :
        def recursive_delete(node,value) :
            current = self.root   
            if node is None :
                return None
            
            
            if value > node.data :
                

                node.right = recursive_delete(node.right,value) 
                
                
            elif value < node.data :
                node.left = recursive_delete(node.left,value) 
                
                
            else :
                
                if node.left is None and node.right is None:
                    return None

                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                
                sucessor = self.get_sucessor(node) 
                node.data = sucessor.data
                node.right = recursive_delete(node.right,sucessor.data)
                
                
            return node
            
                
        self.root = recursive_delete(self.root, value)
     
     
    def get_sucessor(self,node) :
         current = node.right
         while current and current.left: 
            current = current.left
         return current    
             
    def inorder(self,node) :
         if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    
     def bfs(self) :
        if self.root :
            visited_list = []
            bfs_queue = queue.SimpleQueue()
            bfs_queue.put(self.root)
            
            while not bfs_queue.empty() :
                current_node=bfs_queue.get()
                visited_list.append(current_node.data)
                if current_node.left :
                    bfs_queue.put(current_node.left)
                    
                if current_node.right :
                    bfs_queue.put(current_node.right)    
        return visited_list        
             
             


                
                

                
            
        
            
        
           
               
               
           
                        
                
                
                
            
     
        
            
            
