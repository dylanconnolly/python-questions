import random, string

addresses = []
num_to_create = 1000

for i in range(1000):
  s = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
  addresses.append(s)

with open('mac_addresses.txt', 'w') as file:
      for a in addresses:
          file.write(a + "\n")