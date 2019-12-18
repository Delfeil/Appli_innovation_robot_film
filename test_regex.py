# coding: utf-8
import sys

import re

string_to_test = sys.argv[1]

regex = ur"((d')?(\s*)?enqu(e|ê)tes?(criminelles?)?)|noir\s*(policiers?)?"

# regex = ur"n[ao](n|pe?)?|pas(\s*)(di[est])?\s*[cç]a|(in|pas\s*)cor?recte?|il\s*y\s*[aà]\s+erreur|pas\s*(bons?|biens?(\s*compri[est]?)?)"

# regex = "^\s*(?:s(?:lt|alut?)|b(?:on|'|)j(?:ou)?r?|coucous?|cc|wesh|yo)\s"
# regex = ur"(?:com[eé]die?s|drole)"
# regex = ur"bonjour"
# regex = ur"(d'\s*|de\s*)?action|(qui\s*)?bouge"

# pattern = re.compile(regex)

print(re.match(regex, string_to_test))