def validate(s):
    a = s.split(sep=" ")
    check = ["def", ":", ""]
    for i in check:
        if i in a:
            "must contain something"

validate("def validate(s): a = s.split(sep=" ") print(a)")

