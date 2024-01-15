class GetMeta(type):
    def __new__(mcs, class_name, bases, input_attrs):
        output_attrs = {}
        for name, val in input_attrs.items():
            output_attrs[name] = val
            if not callable(input_attrs.get(name)) and not name.startswith("__"):
                output_attrs[f"get_{name}"] = lambda cls: getattr(cls, name)
                output_attrs[f"set_{name}"] = lambda cls, new: setattr(cls, name, new)
        return type(class_name, bases, output_attrs)


class Circle(metaclass=GetMeta):
    radius = 5.0


if __name__ == "__main__":
    circle = Circle()
    print(circle.get_radius())
    circle.set_radius(6.0)
    print(circle.get_radius())
