ostoslista = []

while True:
	print("Haluatko")
	print("(1)Lisätä listaan")
	print("(2)Poistaa listalta vai")
	valinta = input("(3)Lopettaa?: ")
	if valinta == "1":
		lisays = input("Mitä lisätään?: ")
		ostoslista.append(lisays)
	elif valinta == "2":
		pituus = len(ostoslista)
		print("Listalla on", pituus, "alkiota.")
		poistettava = input("Monesko niistä poistetaan?: ")
		try:
			poistettava = int(poistettava)
			ostoslista.pop(poistettava)
		except Exception:
			print("Virheellinen valinta.")
	elif valinta == "3":
		print("Listalla oli tuotteet:")
		for i in ostoslista:
			print(i)
		break
	else:
		print("Virheellinen valinta.")