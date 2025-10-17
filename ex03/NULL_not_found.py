def NULL_not_found(object: any) -> int:    
    object_type = type(object)
    flag = 0
    prelude = ""

    if not object and object_type == int:
        prelude = "Zero"
    elif not object and object_type == bool:
        prelude = "Fake"
    # NaN is never equal to itself
    elif object != object:
        prelude = "Cheese"
    # None is a value not a type so you cant check via type(object) == None
    elif not object and object is None:
        prelude = "Nothing"
    elif not object and object_type == str:
        prelude = "Empty"
    else:
        flag = 1
    
    if flag == 1:
        print("Type not Found")
    else:
        if object_type != str:
            print(f"{prelude}: {object} {object_type}")
        else:
            print(f"{prelude}: {object_type}")
    return flag

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

# print(math.nan)

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))