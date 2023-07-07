def ObjIDParser(model):
    data = model.dict()
    data["id"] = str(data["id"])
    return data
