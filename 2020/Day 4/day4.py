#!/usr/bin/env python3
from aoc_utils import ExecutionTime

ruleset = {
    "byr": { # Birth year (byr:1926)
        "digits": 4,
        "min": 1920,
        "max": 2002
        }, 
    "iyr": { # Issue year (iyr:2010)
        "digits": 4,
        "min": 2010,
        "max": 2020
        }, 
    "eyr": { # Expiration year (eyr:2020)
        "digits": 4,
        "min": 2020,
        "max": 2030
        }, 
    "hgt": { # Height (hgt:178)
        "cm": { # if cm: min-max 150-193
            "min": 150,
            "max": 193
            }, 
        "in": { # if in: min-max 59-76
            "min": 59,
            "max": 76
            }
        },  
    "hcl": { # Hair colour (hcl:#efcc98)
        "digits": 6,
        "char": "#",
        "bin_base": 16
        }, 
    "ecl": { # Eye colour (ecl:blu)
        "eyecolours": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        },
    "pid": { # Passport ID (pid:433543520)
        "digits": 9
        },
    "cid": "" # Country ID (cid:92) No rules... yet
}

def PassportChecker(string: str) -> bool:
    key_n_values = dict((x,y) for x, y in tuple(x.split(":") for x in string.split(" "))).items()
    switch = True
    
    if len(key_n_values) < 7:
        return False
    
    string_set = set()
    for key, value in key_n_values:
        string_set.add(key)
    
    if string_set != set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")) and len(key_n_values) == 8:
        return False
    
    if string_set != set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")) and len(key_n_values) == 7:
        return False

    for key, value in key_n_values:
        if key == "byr":
            byr = value
            if not len(value) == ruleset[key]["digits"] or not ruleset[key]["min"] <= int(value) <= ruleset[key]["max"]:
                return False
            
        if key == "iyr":
            iyr = value
            if not len(value) == ruleset[key]["digits"] or not ruleset[key]["min"] <= int(value) <= ruleset[key]["max"]:
                return False
            
        if key == "eyr":
            eyr = value
            if not len(value) == ruleset[key]["digits"] or not ruleset[key]["min"] <= int(value) <= ruleset[key]["max"]:
                return False
            
        if key == "hgt":
            hgt = value
            unit = value[-2:]
            if unit not in ["cm", "in"]: 
                return False
            if not ruleset[key][unit]["min"] <= int(value[:-2]) <= ruleset[key][unit]["max"]:
                return False
            
        if key == "hcl":
            hcl = value
            if value[0] != ruleset[key]["char"] or len(value[1:]) != ruleset[key]["digits"]:
                return False
            try:
                if not int(value[1:], ruleset[key]["bin_base"]):
                    return False 
            except Exception:
                return False
            
        if key == "ecl":
            ecl = value
            if value not in ruleset[key]["eyecolours"]:
                return False
            
        if key == "pid":
            pid = value
            if len(value) != ruleset[key]["digits"] or not value.isdigit():
                return False
            
        if key == "cid":
            cid = value
            switch = not switch
            
    if switch:
        cid = "whatever"
            
    #return {"byr": byr, "iyr": iyr, "eyr": eyr, "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid, "cid": cid}
    return True
    

valid_vars = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt", "cid"]
semi_valid = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]

string_list = []

@ExecutionTime
def main():
    with open("./input.txt", "r") as content:
        lines = [x.strip() for x in content.readlines()]

    string = ""
    for line in lines:
        if line == "" or line == lines[-1]:
            if line == lines[-1]:
                string += line.strip() + " "
            string_list.append(string.strip())
            string = ""
        else:
            string += line.strip() + " "
    
    valid_list = []
    non_valid = []
    for string in string_list:
        if PassportChecker(string):
            valid_list.append(string)
        else:
            non_valid.append(string)

    print(f"CORRECT LIST: ({len(valid_list)})")
    print(f"NONVALID LIST: ({len(non_valid)})")
    

if __name__ == "__main__":
    main()