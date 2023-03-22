for i in range(1,12):
    if(i==5):
        print("I skipped", "5*5")
        continue;
    print("5X", i, "=", 5*(i))
    if(i==10):
        break

print("Out of for loop")