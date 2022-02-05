import sys

# Dictionaries
temp_dict = {"T3": ["T3_300", 300], "T4": ["T4_305", 305], "T5":["T5_310", 310]}

# Functions
def read_sequences(path):
    with open(path, "r") as f:
        first_line = int(f.readline())
        second_line = int(f.readline())
    return first_line, second_line

# Main code
with open("variables.in", "r") as f:
    length = f.readline().split()[0]
    
    temperature = f.readline().split()[0]
    if (temperature in temp_dict.keys()):
        temperature = temp_dict[temperature]
    else:
        sys.exit("Insert a valid temperature: T3, T4, T5")

    steps = int(f.readline().split()[0])
    path_folder = f.readline().split()[0]

steps_write = 5000
total_write_steps = (steps//steps_write) + 1
timestep = 10.0*0.02/20.0

path = path_folder + temperature[0] + "/" + length

chain_number, chain_bases = read_sequences(path + "/seq")
flap_base_cut, flap_bases = read_sequences(path + "/flap")

site_dna2 = 3 * chain_bases - 1
site_total = 3 * chain_bases * 2 - 2
chains_total = site_total * chain_number

flap_cut = ((flap_base_cut - 1) * 3) - 1
site_flap2 = 3 * flap_bases - 1
flap_total = 3 * flap_bases * 2 - 2

site_dna = chains_total + flap_total
