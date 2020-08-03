def strip_prefix(target, prefix):
    if target.startswith(prefix):
        return target[len(prefix):]
    return target

def strip_suffix(target, suffix):
    if target.endswith(suffix):
        return target[:-len(suffix)]
    return target
