ribosome = {}

keys = ["AUG"]
for key in keys:
	ribosome[key] = "start"

keys1 = ["UAA","UAG","UGA"]
for key in keys1:
	ribosome[key] = "stop"


keys2 = ["UUU", "UUC"]
for key in keys2:
	ribosome[key] = "phenylalanine"

keys3 = ["UUA","UUG","CUU","CUC","CUA","CUG"]
for key in keys3:
	ribosome[key] = "leucine"


keys4 = ["AUU", "AUC", "AUA"]
for key in keys4:
	ribosome[key] = "isoleucine"


keys5 = ["GUU","GUC","GUA","GUG"]
for key in keys5:
	ribosome[key] = "valine"


keys6 = ["UCU","UCC","UCA","UCG","AGU","AGC"]
for key in keys6:
	ribosome[key] = "serine"


keys7 = ["CCU","CCC","CCA","CCG"]
for key in keys7:
	ribosome[key] = "proline"


keys8 = ["ACU","ACC","ACA","ACG"]
for key in keys8:
	ribosome[key] = "threonine"


keys9 = ["GCU","GCC","GCA","GCG"]
for key in keys9:
	ribosome[key] = "alanine"

keys10 = ["UAU","UAC"]
for key in keys10:
	ribosome[key] = "tyrosine"

keys11 = ["CAU","CAC"]
for key in keys11:
	ribosome[key] = "histidine"

keys12 = ["CAA","CAG"]
for key in keys12:
	ribosome[key] = "glutamine"


keys13 = ["AAU","AAC"]
for key in keys13:
	ribosome[key] = "asparagine"

keys14 = ["AAA","AAG"]
for key in keys14:
	ribosome[key] = "lysine"

keys15 = ["GAU","GAC"]
for key in keys15:
	ribosome[key] = "aspartic acid"


keys16 = ["GAA","GAG"]
for key in keys16:
	ribosome[key] = "glutamic acid"


keys17 = ["UGU","UGC"]
for key in keys17:
	ribosome[key] = "cysteine"


keys18 = ["UGG"]
for key in keys18:
	ribosome[key] = "tryptophan"

keys19 = ["CGU","CGC","CGA","CGG","AGA","AGG"]
for key in keys19:
	ribosome[key] = "arginine"

keys20 = ["GGU","GGC","GGA", "GGG"]
for key in keys20:
	ribosome[key] = "glycine"

