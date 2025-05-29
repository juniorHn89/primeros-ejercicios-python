print("Cual es la media de goles de Yamal esta temporada?")
print("Cual es la media de goles de Mbappe esta temporada?")

goles_yamal = [24.4,22.1,7.3,15.4,6.4]
goles_mbappe = [22.1,6.2,9.3,15.6,19.2,30.8]

def mean(numbers):
    return sum(numbers)  / len(numbers)

yamal_mean = mean(goles_yamal)
mbappe_mean = mean(goles_mbappe)\


print(f"Media de Yamal {yamal_mean:.1f} goles")
print(f"Media de Mbappe {mbappe_mean:.1f} goles")


