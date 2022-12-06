with open("./data.txt", "r", encoding="utf-8") as data_file:
    data = data_file.read()
    print([i+4 for i, _ in enumerate(data) if len(set(data[i:i+4])) > 3][0])
    print([i+14 for i, _ in enumerate(data) if len(set(data[i:i+14])) > 13][0])
