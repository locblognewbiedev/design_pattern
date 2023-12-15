class House:
    def __init__(self) -> None:
        self.floor = None
        self.wall = None
        self.roof = None

    def __str__(self) -> str:
        return f"floor:{self.floor}\n wall:{self.wall}\n roof:{self.roof}"
    
# đây là product
class HouseBuilder:
    def __init__(self) -> None:
        self.house = House()

    def set_floor(self, amount):
        self.house.floor = amount
        
    def set_wall(self, amount):
        self.house.wall = amount
        
    def set_roof(self, amount):
        self.house.roof = amount
        
    def build(self):
        return self.house
# đây là builder
# cách xây dựng đt
# mô tả đối tượng
class SmallHouseBuilder(HouseBuilder):
    def build_foor(self):
        self.set_floor('small floor')
    def build_wall(self):
        self.set_wall('small wall')
    def build_roof(self):
        self.set_roof('small roof')
# mô tả chi tiết đối tượng
# bản chất này là quá trình tạo đt nhưng thay vì truyền dưới dạng thma số nó đóng gọi lại vào một class
# để tạo chỉ cần gọi class

class Contractor:
    def __init__(self, builder) -> None:
        self.builder = builder
    def contractor_house(self):
        self.builder.build_foor()
        self.builder.build_wall()
        self.builder.build_roof()
#đây là hàm bắt đầu xây dựng
small_builder = SmallHouseBuilder()
contractor = Contractor(small_builder)
contractor.contractor_house()
small_house = small_builder.build()

print(small_house)

# bản chất ở đây là khởi tạo đc đối tượng mà ko truyền tham số nào,
#có vẻ sẽ hữu ích nếu đó là các đối tượng của hệ thống chứ những đối tượng mà lấy dữ liệu dộng thì ko hợp lí lắm
# small_house_builder  = HouseBuilder()
# small_house_builder.\
#     set_floor(5).\
#     set_roof(6).\
#     set_wall(7)

# small_house = small_house_builder.build()
# print(small_house)


    
