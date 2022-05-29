from ribosome import ribosome as ribosome

def transcribe(name):
  filename = name + ".txt"
  genetic_code = open(filename,'r')
  
  cnvtd = ""
  
  
  while 1:
      # read by character
    string = genetic_code.read(1)  
    if string == "A":
      cnvtd = cnvtd + "U"
    elif string == "T":
      cnvtd = cnvtd + "A"
    elif string == "G":
      cnvtd = cnvtd + "C"
    elif string == "C":
       cnvtd = cnvtd + "G"
    elif string == "U":
      cnvtd = cnvtd + "A"
    else:
      print("Not a valid strand of DNA")
    try:
      ord(string)
    except:
      break
    
  
  genetic_code.close()
  
  if (len(cnvtd) == 0):
    print("Not a valid strand of DNA")
  return cnvtd






def check(s1,s2):
  base_num = 0
  if (s1 == s2):
    return "No Mutation"
  elif (len(s1) != len(s2)):
    return "Strands have different lengths; not able to compare"
  else:
    for i in range(len(s2)-1):
      if (s1[i] != s2[i]):
        base_num = i

    if (len(s1) == len(s2)):
      result = "Substitution mutation at " + "base " + str(base_num)
      return result
    
    elif (len(s1) > len(s2)):
      result = "Deletion mutation at " + "base " + str(base_num)
      return result

    elif (len(s1) < len(s2)):
      result = "Insertion mutation at " + "base " + str(base_num)
      return result

def translate(mrna):
  codon = ""
  aminos = []
  c = 0
  for s in mrna:
    codon = codon + s
    c = c + 1
    if c == 3:
      aminos.append(ribosome[codon])
      codon = ""
      c = 0
  print(aminos)