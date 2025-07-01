original = {"Argentina" : "Buenos Aires", "Chile" : "Santiago", "Brasil" : "Brasilia"}
invertida = {value : key for key, value in original.items()}

print(f"La lista original es {original} y la invertida es {invertida}")