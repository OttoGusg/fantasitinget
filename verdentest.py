from verden import Verden 
from politiker import Politiker

min_verden = Verden()

for politiker in politikerliste:
    ny_politiker = Politiker(navn, parti)
    min_verden.append(ny_politiker)

    mitt_parti = parti("Nasjonal Blanding")
    jonas = min_verden.finn_politiker("Jonas Gahr Støre")
    mitt_parti.kjop(jonas)

