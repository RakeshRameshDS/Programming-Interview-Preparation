num = 1775
print(bin(num))
listing = []
prev = 0
counter = 0
while num != 0:
    if num & 1 == 1 and prev == 1:
        counter += 1
    elif num & 1 == 1 and prev == 0:
        listing.append(counter)
        prev = 1
        counter = 1
    elif num & 1 == 0 and prev == 0:
        counter += 1
    else:
        listing.append(counter)
        prev = 0
        counter = 1
    num >>= 1
listing.append(counter)
print(listing)

max_comb = 0
for i in range(len(listing)):
    if i-1>0:
        max_comb = max(max_comb, listing[i-1])
    elif i+1<len(listing):
        max_comb = max(max_comb, listing[i+1])
    if i-1 > 0 and i + 1 < len(listing) and listing[i] == 1:
        max_comb = max(max_comb, listing[i-1]+listing[i+1]+1)
    i += 2
print(max_comb)
