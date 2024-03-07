class ParserMeta(type):
    """
    A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'get_value') and 
                callable(subclass.get_value) and
                isinstance(subclass.get_value(), str)
        )

class Glove_sensor(metaclass=ParserMeta):
    """
    This interface is used for sensor like classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass