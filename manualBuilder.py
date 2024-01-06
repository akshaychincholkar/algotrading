class Computer:
    # def __init__(self, cpu):
    #     self.cpu = cpu
    #     self.ram = None
    #     self.hdd = None
    #     self.isGraphicsEnabled = False
    #     self.isBluetoothEnabled = False

    def set_ram(self, ram):
        self.ram = ram

    def set_hdd(self, hdd):
        self.hdd = hdd

    def isGraphicsEnabled(self,isGraphicsEnabled):
        self.isGraphicsEnabled = isGraphicsEnabled

    def isBluetoothEnabled(self,isBluetoothEnabled):
        self.isBluetoothEnabled = isBluetoothEnabled

    def __init__(self,computerBuilder):
        self.hdd = computerBuilder.hdd
        self.cpu = computerBuilder.cpu
        self.ram = computerBuilder.ram
        self.isBluetoothEnabled= computerBuilder.isBluetoothEnabled
        self.isGraphicsEnabled = computerBuilder.isGraphicsEnabled

    def __str__(self):
        return f"Computer - CPU: {self.cpu}, RAM: {self.ram}GB, HDD: {self.hdd}GB, isBluetoothEnabled: {self.isBluetoothEnabled}, isGraphicsEnabled: {self.isGraphicsEnabled}"

class ComputerBuilder:
    def __init__(self, cpu):
        self.cpu = cpu
        self.ram = None
        self.hdd = None
        self.isGraphicsEnabled = False
        self.isBluetoothEnabled = False
    
    def __init__(self, cpu, hdd, ram):
        self.cpu = cpu
        self.hdd = hdd
        self.ram = ram
        self.isGraphicsEnabled = False
        self.isBluetoothEnabled = False

    def setGraphicsCardEnabled(self,isGraphicsEnabled):
        print("isGraphicsEnabled: ",isGraphicsEnabled)
        self.isGraphicsEnabled = isGraphicsEnabled
        return self

    def setBluetoothEnabled(self,isBluetoothEnabled):
        self.isBluetoothEnabled = isBluetoothEnabled
        return self
    
    def build():
        return Computer()
        
# Example usage
if __name__ == "__main__":
    # # Creating a computer instance
    # my_computer = Computer(cpu="Intel i5")

    # # Setting RAM and HDD later
    # my_computer.set_ram(8)
    # my_computer.set_hdd(512)

    # # Printing the computer details
    # print(my_computer)

    # Creating the builder and passing to the computer
    # computerBuilder = ComputerBuilder("M1 Processor")
    computerBuilder = ComputerBuilder("M1 processor","500", "8")
    # computer =  Computer(computerBuilder.setBluetoothEnabled(True).setGraphicsCardEnabled(True))
    computer =  Computer(computerBuilder.setBluetoothEnabled(True))
    print(computer)
