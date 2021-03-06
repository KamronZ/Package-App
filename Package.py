import datetime

# O(1)
class Package:
    package_ID = int

    def __init__(self, package_ID, address, city, state, zip, deadline, weight, special, left_hub_timestamp,
                 delivery_timestamp):
        today = today = datetime.datetime.today()
        self.left_hub_timestamp = datetime.datetime(today.year, today.month, today.day, 0, 00, 0, 0)
        self.delivery_timestamp = datetime.datetime(today.year, today.month, today.day, 0, 00, 0, 0)

        self.package_ID = package_ID
        self.address = " " + address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.special = special

    def print(self):
        print("Package ID: ", self.package_ID, "; Address: ", self.address, "; City: ", self.city,
              "; State: ", self.state, ";Zip ", self.zip, ";Deadline: ", self.deadline, "Package Weight: "
              , self.weight, "; Package Special Notes: ", self.special, ";Left hub at:", self.left_hub_timestamp,
              "; Delivered at: ", self.delivery_timestamp, end='\n')

    def get_package_ID(self):
        return self.package_ID

    def update_package_special(self, updated_special):
        self.special = updated_special

    def update_package_delivery_time(self, delivery_time):
        self.delivery_timestamp = delivery_time

    def update_package_lefthub_time(self, left_hub_timestamp):
        self.left_hub_timestamp = left_hub_timestamp

    def get_package_range(self, start_range, end_range):
        if start_range >= self.delivery_timestamp <= end_range:
            print("Package id:", self.package_ID, "| Was Delivered To:",self.address,self.city
                  ,self.state, "| At", self.delivery_timestamp)
        if self.left_hub_timestamp > end_range:
            print("Package id: ",self.package_ID, "| Is at the HUB |")
        if self.left_hub_timestamp <= start_range and self.delivery_timestamp >= end_range:
            print("Package id: ", self.package_ID, "| Is enroute |")



    def package_status(self, time):
        if self.left_hub_timestamp > time:
            print("Package id: ", self.package_ID, "| Is at the HUB |")
        if self.left_hub_timestamp <= time < self.delivery_timestamp:
            print("Package id: ", self.package_ID, "| Is enroute |")
        if self.left_hub_timestamp <= time and self.delivery_timestamp <= time:
            print("Package id:", self.package_ID, "| Was Delivered To:", self.address, self.city
                  , self.state, "| At", self.delivery_timestamp)

