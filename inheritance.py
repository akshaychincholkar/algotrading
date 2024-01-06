from abc import ABCMeta, abstractmethod
class Base(object):
# class Base(metaclass = ABCMeta): <- Python 3
    __metaclass__ = ABCMeta
    def __init__(self, str_dir_config):
        self.str_dir_config = str_dir_config
    
    @abstractmethod
    def _do_stuff(self, signals):
        pass
    
    @property    
    @abstractmethod
    def name(self):
        """This property will be supplied by the inheriting classes
        individually.
        """
        pass
    

class Base1(Base):
    __metaclass__ = ABCMeta
    """This class does not provide the name property and should
    raise an error.
    """
    def __init__(self, str_dir_config):
        super(Base1, self).__init__(str_dir_config)
        # super().__init__(str_dir_config) <- Python 3
    
    def _do_stuff(self, signals):
        print("Base_1 does stuff")
        # print("Base_1 does stuff") <- Python 3

class C(Base1):
    @property
    def name(self):
        return "class C"
    

if __name__ == "__main__":
    b1 = Base1("abc")
    b1._do_stuff("test")
    print("hello")