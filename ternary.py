#if/else biasa
total=2000
if total > 1000:
	diskon=2.5
else:
	diskon=0.0
print(total,diskon)

#ternary
diskon=2.5 if total > 1000 else 0
print(total,diskon)
