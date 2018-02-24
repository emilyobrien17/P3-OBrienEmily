import time

def main():
    totalDollarsPaid = eval(input("Enter Cash Amount ($2 / Gallon):  "))
    totalGallonsPumped = 0
    for i in range(0, totalDollarsPaid):
        # Wait half second to simulate gas being pumped
        time.sleep(0.5)
        totalGallonsPumped += 0.5
        if totalGallonsPumped % 1 == 0:
            print("Gas Pumped: ", totalGallonsPumped)
    print("Total gas pumped: ", totalGallonsPumped)

main()