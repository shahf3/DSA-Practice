def IPValidation(ipAdd):

    n = len(ipAdd)

    if n > 3:
        return False

    for i in range(n):
        if not ipAdd[i].isdigit():
            return False
    
    convertIP2Int = int(ipAdd)

    return 0 <= convertIP2Int <= 255
    
ip1 = "128.0.0.1"
ip2 = "125.16.100.1"
ip3 = "125.512.100.1"
ip4 = "125.512.100.abc"
print(IPValidation(ip2))