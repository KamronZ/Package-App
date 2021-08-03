class Package:
    package_ID = 0
    address = ""
    city = ''
    state = ''
    zip = ''
    deadline = ''
    weight = ''
    status = ''

    def __init__(self, package_ID, address, city, state, zip, deadline, weight, status):
        self.package_ID = package_ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def print(self):
        print("Package ID: ", self.package_ID, "; Address: ", self.address, "; City: ", self.city,
              "; State: ", self.state, "; Zip ", self.zip, "; Deadline: ", self.deadline, "Package Weight: "
              , self.weight, "; Package Current Status: ", self.status)

    def get_package_ID(self):
        return self.package_ID


    def update_package_status(self, updated_status):
        self.status = updated_status
