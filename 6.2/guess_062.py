def find():
    l = bottom
    h = top

    while l < h:
        mid = (h + l) // 2
        if guess(mid) == -1:
            l = mid + 1
        else:
            h = mid

    return l