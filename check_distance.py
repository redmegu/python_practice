meters = 0
destination = 1000

while meters < destination:
    distance = destination - meters
    print("You are still " + str(distance) + " meters away.")
    meters += 100
if meters == destination:
    print("You have arrived")
    