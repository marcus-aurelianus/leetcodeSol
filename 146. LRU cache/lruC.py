from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache=OrderedDict()
        self.capacity=capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        self.cache[key]=value
        self.cache.move_to_end(key)
        if len(self.cache)>self.capacity:
            self.cache.popitem(last=False)

##cache = LRUCache(2)        
##cache.put(1, 1);
##cache.put(2, 2);
##print(cache.get(1));       
##cache.put(3, 3);    
##print(cache.get(2));      
##cache.put(4, 4);  
##print(cache.get(1))  
##print(cache.get(3))     
##print(cache.get(4))      

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
