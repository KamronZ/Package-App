class Package:
    # package_ID = 0
    # address = ""
    # city = ''
    # state = ''
    # zip = ''
    # deadline = ''
    # weight = ''
    # special = ''

    def __init__(self, package_ID, address, city, state, zip, deadline, weight, status):
        self.package_ID = package_ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.special = status

    def print(self):
        print("Package ID: ", self.package_ID, "; Address: ", self.address, "; City: ", self.city,
              "; State: ", self.state, ";Zip ", self.zip, ";Deadline: ", self.deadline, "Package Weight: "
              , self.weight, "; Package Special Notes: ", self.special)

    def get_package_ID(self):
        return self.package_ID

    def update_package_special(self, updated_special):
        self.special = updated_special
