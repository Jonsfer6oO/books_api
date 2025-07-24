def getattr_validate(obj: object, key: str):
    try:
        return getattr(obj, key)
    except:
        return None