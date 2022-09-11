from juliacall import Main as jl

jl.seval("using Capse")
jl.seval("using SimpleChains")
jl.seval("using BSON")
jl.seval("using Static")

capse_compute_Cl = jl.seval('Capse.compute_Cℓ')
load_emu = jl.seval('Capse.load_emulators')

def compute_Cl(input_test, emu):
    Cl = capse_compute_Cl(jl.collect(input_test), emu)
    return Cl

