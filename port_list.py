sort_by_persona = {
    "PAN": {9002, 9300, 135, 445, 88},
    "PSN": {9090, 135, 445, 88, 8443, 8905},
    "PxGrid": {8910}
}

need_to_check = {
    "PAN": sort_by_persona.get("PAN") |
           sort_by_persona.get("PSN") |
           sort_by_persona.get("PxGrid"),
    "PSN": sort_by_persona.get("PSN") |
           sort_by_persona.get("PxGrid")
}

# print(need_to_check["PSN"])
