target_ip = input("What is the target IP? ")
target_port = int(input("What is the target Port? "))

print(f"Target acquired at IP Address {target_ip} and Port Number {target_port}.")
if target_port == 8080:
    print("Alternate web port targeted!")
else:
    print("Standard port targeted.")
