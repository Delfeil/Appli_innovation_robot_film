# coding: utf-8
import sys

import re

string_to_test = sys.argv[1]

# des scenes, des propos ou des images peuvent heurter la sensibilite des spectateurs

regex = ur"(p(eut|ouvant)\s*heurter\s*[lm]a\s*sensibilit(e|é)|polemique|adulte|(plus|interdit?\s*au[xs]?\s*moins?)\s*de\s*(18|dix-?\s*huit|16|seize)\s*ans?)"

# regex = ur"n[ao](n|pe?)?|pas(\s*)(di[est])?\s*[cç]a|(in|pas\s*)cor?recte?|il\s*y\s*[aà]\s+erreur|pas\s*(bons?|biens?(\s*compri[est]?)?)"

# regex = "^\s*(?:s(?:lt|alut?)|b(?:on|'|)j(?:ou)?r?|coucous?|cc|wesh|yo)\s"
# regex = ur"(?:com[eé]die?s|drole)"
# regex = ur"bonjour"
# regex = ur"(d'\s*|de\s*)?action|(qui\s*)?bouge"

# pattern = re.compile(regex)

print(re.match(regex, string_to_test))