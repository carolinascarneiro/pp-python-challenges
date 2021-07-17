def validate(s):
    a = s.split()
    print(a)
    print(a)
    b = []
    for item in a:
    if "def" in item:
        b.append("There's def")
        elif ":" in item:
            b. append("There's :")
        elif "(" and ")" in item: #OK
            b. append("There's ( and )")
        elif "()" in item: #OK
            b.append("all parameters are fine")
        elif "    " in item: #NOT OK
            b.append("not missing indent")
        elif "validate" in item: #NOT OK
            b.append("right name")
        elif "return" in item: #OK
            b.append("there's return")
    print(b)
    print(len(b))


validate("def validate(s):   a = s.split(sep=" ") print(a) return")

