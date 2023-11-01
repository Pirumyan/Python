def deepcopy(lis: list) -> list:
    """list will give back new deepcopy list,
        In this function I (GOr) will try make implement,
        I don`t  Care will do it Nigga"""
    # arajin depqum palyubomu stacvelu a list u aystexic sksum a mi hetaqrqir irakanutyun
    if isinstance(lis, list):
        new_list = []
        for item in lis:
            new_item = deepcopy(item)
            new_list.append(new_item)
        return new_list
    # haziv gta valui mej ei  lrvel bayc heto kayfot exav zut ujex recursia em shnium fori mej ))
    elif isinstance(lis, dict):
        new_dict = {}
        for key, value in lis.items():
            new_key = deepcopy(key)
            new_value = deepcopy(value)
            new_dict[new_key] = new_value
        return new_dict
    # erkar em lrvum bayc stacvec sarqum em list mejy sxa lcnum cast anum tuple)))
    elif isinstance(lis, tuple):
        new_tuple = []
        for item in lis:
            new_item = deepcopy(item)
            new_tuple.append(new_item)
        return tuple(new_tuple)
    # seti hamar em  anum
    elif isinstance(lis, set):
        new_set = set()
        for item in lis:
            new_item = deepcopy(item)
            new_set.add(new_item)
        return new_set
    # deep deep baytsareys hamar el em anum
    elif isinstance(lis, bytearray):
        new_bytearray = bytearray()
        for item in lis:
            new_item = deepcopy(item)
            new_bytearray.append(new_item)
        return new_bytearray

    else:
        return lis


