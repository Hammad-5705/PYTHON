std_rnum={
    5705:"M.Hammad",
    5706:"Abdullah",
    5708:"Umer",
    7738:"Fahad",
}

print(std_rnum[5705])

print(std_rnum.get(7738))

print(std_rnum.keys())

print(std_rnum.values())

for i in std_rnum.keys():
    print(i)

for i in std_rnum.values():
    print(i)

for i in std_rnum.keys():
    print(f"The key {i} stores the value {std_rnum[i]}")

print("\n\n")

for i,ii in std_rnum.items():
    print(f"The key {i} stores {ii}")
