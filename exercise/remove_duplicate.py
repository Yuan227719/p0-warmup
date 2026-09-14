
rows = [1,1,12,3,3,2,2,3,4,4,4,5,5,53,3,3,3333,4455,332]

set_rows = set()

no_duplicate_rows = []

for i in rows:

    if i not in set_rows:
        set_rows.add(i)
        no_duplicate_rows.append(i)


print(no_duplicate_rows)
print("\a")

del rows

print(rows) 


print('_'.join(('ab', 'ra ca da bra')))



