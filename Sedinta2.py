class Ball(object):
      
         def __init__ (self, color, size):
             self.color = color
             self.size = size
  
  

# print(id(ball1))
# print(id(ball2))


class Box(object):
     
        def __init__ (self, color, size):
            self.color = color
            self.size = size
            
 
        def __eq__(self,other):
            if isinstance( other, self.__class__):
                return self.color == other.color and self.size == other.size
            return False
        def __ne__(self, other):
            if isistance( other, self.__class__):
                return self.color != other.color or  self.size == other.size
            return False
 
ball1 = Ball('blue','small')
ball2 = Ball('blue','small')
box1 = Box('blue','small')
ball3 = Ball('blue','small')
print(ball1==box1)
print(ball1 == ball2) 