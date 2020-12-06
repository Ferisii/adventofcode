#!/usr/bin/env python3
from re import findall

pass_ruleset = {
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
requirement = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def ShakeyPassportChecker(passport_dict: dict) -> bool:
    return not any(set(requirement) - passport_dict.keys())


def SecurePassportChecker(passport_dict: dict) -> bool:
    if any(set(requirement) - passport_dict.keys()):
        return False

    for n in range(3):
        key, value = requirement[n], passport_dict[requirement[n]]
        if not len(value) == pass_ruleset[key]["digits"] or not pass_ruleset[key]["min"] <= int(value) <= pass_ruleset[key]["max"]:
            return False
        
    key, value = requirement[3], passport_dict[requirement[3]]
    unit = value[-2:]
    if unit not in ["cm", "in"] or not pass_ruleset[key][unit]["min"] <= int(value[:-2]) <= pass_ruleset[key][unit]["max"]:
        return False
        
    key, value = requirement[4], passport_dict[requirement[4]]
    if value[0] != pass_ruleset[key]["char"] or len(value[1:]) != pass_ruleset[key]["digits"]:
        return False
    try:
        int(value[1:], pass_ruleset[key]["bin_base"])
    except Exception:
        return False
        
    key, value = requirement[5], passport_dict[requirement[5]]
    if value not in pass_ruleset[key]["eyecolours"]:
        return False
        
    key, value = requirement[6], passport_dict[requirement[6]]
    if len(value) != pass_ruleset[key]["digits"] or not value.isdigit():
        return False

    return True
    

def main():
    passports = []
    with open("./input.txt", "r") as content:
        for block in content.read().split("\n\n"):
            parsed = findall(r'(\w+):(\S+)', block)
            passports.append({k[0]: k[1] for k in parsed})
    
    puzzle1, puzzle2 = 0, 0
    for passport in passports:
        puzzle1 += ShakeyPassportChecker(passport)
        puzzle2 += SecurePassportChecker(passport)

    print(f"Puzzle 1 solution: {puzzle1}\nPuzzle 2 solution: {puzzle2}")
    

if __name__ == "__main__":
    from time import time
    start_time = time()
    main()
    print(f"\nSolved in {round(time() - start_time, 4)} seconds.")