import rna_functions as rna

mrna = rna.transcribe("test")
mrna1 = rna.transcribe("test1")
mrna2 = rna.transcribe("test2")
mrna3 = rna.transcribe("test3")
mrna4 = rna.transcribe("sample")

rna.translate(mrna)
rna.translate(mrna1)
rna.translate(mrna2)
rna.translate(mrna3)
rna.translate(mrna4)

print(rna.check(mrna,mrna1))
print(rna.check(mrna,mrna2))
print(rna.check(mrna,mrna3))
print(rna.check(mrna,mrna4))


