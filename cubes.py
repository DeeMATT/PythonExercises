cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)

print(cubes)


# Cube comprehension

cubes = [cube**3 for cube in range(1,11)]
print(cubes)