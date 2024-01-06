# Product
class PersonalComputer:
    def __init__(self, cpu, memory, storage, graphics_card=None, motherboard=None):
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.graphics_card = graphics_card
        self.motherboard = motherboard

    def __str__(self):
        gpu_info = f" with {self.graphics_card}" if self.graphics_card else ""
        mb_info = f" on {self.motherboard}" if self.motherboard else ""
        return f"Personal Computer - CPU: {self.cpu}, Memory: {self.memory}, Storage: {self.storage}{gpu_info}{mb_info}"


# Abstract Builder
class PCBuilder:
    def __init__(self):
        self.pc = PersonalComputer("", "", "")

    def set_cpu(self, cpu):
        self.pc.cpu = cpu
        return self

    def set_memory(self, memory):
        self.pc.memory = memory
        return self

    def set_storage(self, storage):
        self.pc.storage = storage
        return self

    def set_graphics_card(self, graphics_card):
        self.pc.graphics_card = graphics_card
        return self

    def set_motherboard(self, motherboard):
        self.pc.motherboard = motherboard
        return self

    def build(self):
        return self.pc


# Concrete Builder
class GamingPCBuilder(PCBuilder):
    def set_graphics_card(self, graphics_card):
        # Overriding set_graphics_card to ensure gaming PCs always have a graphics card
        self.pc.graphics_card = graphics_card
        return self

    def set_motherboard(self, motherboard):
        # Overriding set_motherboard to ensure gaming PCs have a gaming motherboard
        self.pc.motherboard = f"Gaming {motherboard}"
        return self


# Director
class PCDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        return self.builder.set_cpu("Intel i7").set_memory("16GB").set_storage("512GB SSD").build()


# Client
if __name__ == "__main__":
    # Creating a standard personal computer
    builder = PCBuilder()
    director = PCDirector(builder)
    pc = director.construct()
    print(pc)

    # Creating a gaming personal computer
    gaming_builder = GamingPCBuilder().set_cpu('1TB')
    gaming_director = PCDirector(gaming_builder)
    gaming_pc = gaming_director.construct()
    print(gaming_pc)
