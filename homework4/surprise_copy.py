# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
for keys in targets:
	print (keys)
#print(targets.keys())


print(targets["Polaris"])

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
"""
for star in targets["star"]:
	print(targets["star"]["Spectral Type"])
		#IDK how to do this
print(targets["Sirius"]["Spectral Type"])
 f strings: f"{x} 
 print(targets.).      #use star no "star" to input variable but when inputting key name you know use ""
"""
for star in targets:
	print(star, targets[star]["Spectral Type"])
#OMG WHY WAS THIS SO HARD BRUHH THIS TOOK ME HOURS, no one told me you could print like this. illegal
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.

def find_mag(targets):
	for star in targets:
		if targets [star]["Magnitude"] > 0.1: 
			print(star)

find_mag(targets)
# my function is only going through vega and IDK why, ohh return inside, also if print function inside then don't do print again outside

# 4) Look up another star, add all the necessary information to the targets list. 


# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def brightest_star(targets):
	maximum = 0
	for star in targets:
		if targets [star]["Magnitude"] > maximum:
				maximum = targets [star]["Magnitude"]
				return (maximum)
		else:
			return (maximum)

print (brightest_star(targets))
# find brightest stars, then compare declinations. 1 Compare to eachother, 1 compare difference to 20. min max function
# I am confused about the directions? Which one matters most???

# 6) What is your favorite constellation
print("Ursa Minor")