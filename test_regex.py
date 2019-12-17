# coding: utf-8
import sys

import re

string_to_test = sys.argv[1]

regex = ur"^\s*(?:n(?:an|o(?:n|pe))\b|pas?\s*(?:di[est]?\s*)[cç]a|incorr?ecte?|(?:il\s*y'?\s*[aà]\s*erreur)|pas\s*(?:corr?ecte?|[cç](?:el)?a|bons?|(?:biens?\s*compri[est]?)))\s"

regex = ur"n[ao](n|pe?)|pas(\s+)di[est]|incor?recte?|il\s+y\s+[aà]\s+erreur"

# regex = "^\s*(?:s(?:lt|alut?)|b(?:on|'|)j(?:ou)?r?|coucous?|cc|wesh|yo)\s"
# regex = ur"(?:com[eé]die?s|drole)"
# regex = ur"bonjour"
regex = ur"(d'\s*|de\s*)?action|(qui\s*)?bouge"

# pattern = re.compile(regex)

print(re.match(regex, string_to_test))