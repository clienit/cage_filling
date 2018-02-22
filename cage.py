# cage dimensions
cage_heigth = 1603
cage_width = 697
cage_length = 846
cage_volume = cage_heigth * cage_width * cage_length
    
class Cage(object):
    """ Cage object with height, width, length, volume attribute and packages inside the cage"""
    def __init__(self):
        self.packages = []
        self.height = 0
        self.width = 0        
        self.length = 0
        self.volume = 0

    def append(self, packageForCage):
        self.packages.append(packageForCage)
        
        if (self.length + packageForCage[2]) <= cage_length and (packageForCage[0] <= self.height) and (packageForCage[1] <= self.width):
            self.length += packageForCage[2]
        elif (self.width + packageForCage[1]) <= cage_width and (packageForCage[0] <= self.height) and (packageForCage[2] <= self.length):
            self.width += packageForCage[1]
        else:
            self.height += packageForCage[0]
            self.width = packageForCage[1]
            self.length = packageForCage[2]
        
        if self.width < packageForCage[1]:
            self.width = packageForCage[1]
        if self.length < packageForCage[2]:
            self.length = packageForCage[2]
            
        self.volume += packageForCage[3]
        
    def __str__(self):
        """ Printable cage """
        #return 'Cage(height=%d, width=%d, length=%d, volume=%d, packages=%s)' % (self.height, self.width, self.length, self.volume, str(self.packages))
        return 'The volume utilisation percentage of the cages = %f' % (self.volume / cage_volume * 100)


if __name__ == '__main__':
    import csv 
    
    # array of all packages
    allPackages = []
    
    # open the .csv file to put all packages in a list
    with open('cage_products.csv', "rt") as csvfile:
        package_reader = csv.reader(csvfile, delimiter=',')
        packages_list = list(package_reader)
        for row in range(1, len(packages_list)):
            package_list = packages_list[row]
            for quantity in range(int(package_list[4])):
                # read excel and put each package in a package array with height / width / length / volume attribute
                package = [int(package_list[1]),int(package_list[2]),int(package_list[3]), int(package_list[1])*int(package_list[2])*int(package_list[3])]
                allPackages.append(package)
    
    # Since height > length > width for a cage sort packages according to height / lenght / width
    # Then apply First Fit Algorithm
    import operator
    sortedAllPackages = sorted(allPackages, key=operator.itemgetter(0, 2, 1), reverse = True)            

    # cage array
    cages = []
    
    for packageForCage in sortedAllPackages:
        # Try to fit package into a cage
        for cage in cages:
            if (cage.height + packageForCage[0] <= cage_heigth):
                cage.append(packageForCage)
                break
        else:
            # if package does not fit into current cage create a new cage
            cage = Cage()
            cage.append(packageForCage)
            cages.append(cage)
    
    print("The number of cages required to accommodate the listed products: " + str(len(cages)))
    
    for cage in cages:
        print (cage)
            


        