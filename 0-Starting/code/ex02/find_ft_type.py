
def all_thing_is_obj(object: any) -> int:
    type_dict = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "Str"
    }
    object_type = type(object)
    type_name = type_dict.get(object_type, "Type not found")

    if type_name == "Str":
        print(f"{object} is in the kitchen : {object_type}")
    elif type_name == "Type not found":
        print(f"{type_name}")
    else:
        print(f"{type_dict[object_type]} : {object_type}")
    
    return 42
