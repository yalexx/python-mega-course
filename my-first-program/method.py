def mean(value):
    if isinstance(value, int):
        return sum(value) / len(value)
   

print(mean({"yanko": 1, "en": 3}))
