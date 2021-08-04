class Truck:
    package_list = list
    current_location = str
    total_distance = float

    def __init__(self,package_list,size):

        self.size = size
        self.package_list = [None] * self.size
        self.total_distance = 0.0
        self.current_location = ''



        
        

