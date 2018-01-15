class Car():
    def __init__(self,make,model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self,miles):
        self.odometer_reading += miles

class Battery():
    """ 一次模拟电动汽车的简单测试"""
    
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("这辆车大约有 " + str(self.battery_size) + "千瓦时容量.")
        
    def get_range(self):
        """打印一条信息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "这辆车充满电大约能行驶" + str(range) + '里'
        print(message)
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()