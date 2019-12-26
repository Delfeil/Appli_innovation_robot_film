# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*
# coding: utf-8
###############################################################################
# PyDial: Multi-domain Statistical Spoken Dialogue System Software
###############################################################################
#
# Copyright 2015 - 2018
# Cambridge University Engineering Department Dialogue Systems Group
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
###############################################################################

"""
RegexSemI_TV.py - regular expression based TV SemI decoder
=====================================================================


HELPFUL: http://regexr.com

"""

'''
    Modifications History
    ===============================
    Date        Author  Description
    ===============================
    Jul 21 2016 lmr46   Refactoring, creating abstract class SemI
'''

import RegexSemI
import re,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)
from utils import ContextLogger
logger = ContextLogger.getLogger('')


class RegexSemI_Films(RegexSemI.RegexSemI):
    """
    """
    def __init__(self, repoIn=None):
        RegexSemI.RegexSemI.__init__(self)  #better than super() here - wont need to be changed for other domains
        self.domainTag = "Films"  #FIXME
        self.create_domain_dependent_regex()
    
    def init_regular_expressions(self):
        # self.rHELLO = ur"^\s*(?:s(?:lt|alut?)|b(?:on|'|)j(?:ou)?r?|coucous?|cc|wesh|yo)\s"
        self.rHELLO = ur"s(alut|lt)|b(jr|onjour)|coucou|cc|wesh|yo"
        # self.rNEG =  ur"^\s*(?:n(?:an|o(?:n|pe))\b|pas?\s*(?:di[est]?\s*)(c|\xc3\xa7)a|incorr?ecte?|(?:il\s*y'?\s*(a|à)\s*erreur)|pas\s*(?:corr?ecte?|(c|\xc3\xa7)(?:el)?a|bons?|(?:biens?\s*compri[est]?)))\s"
        self.rNEG =  ur"n[ao](n|pe?)?|pas(\s*)(di[est])?\s*(c|\xc3\xa7)a|(in|pas\s*)cor?recte?|il\s*y\s*(a|à)\s+erreur|pas\s*(bons?|biens?(\s*compri[est]?)?)"
        # self.rAFFIRM = ur"^\s*(?:oua?is?|ye[ps]|ok|[c\xc3\xa7s]a\s*m['e]?\s*va[st]?|absolue?ment|(?:c(?:e\s*n|)'?\s*e(?:ts?|st?)\s*|)(?:bons?|corr?ecte?|[c\xc3\xa7s]a))\s*$"
        self.rAFFIRM = ur"\s*(oua?is?|ye[ps]|ok|(\xc3\xa7|c)a\s*m['e]?\s*va[st]?|absolue?ment|c'est?\s*(bons?|corr?ecte?|(\xc3\xa7|c)a))"
        # self.THATSALL = ur"c(?:'?e(?:st?|ts?)|e\s*serr?as?)\s*tou[ts](?:\s*pour\s*(?:moi|nous)|)"
        self.THATSALL = ur"c('?e(st?|ts?)|e\s*serr?as?)\s*tou[ts](\s*pour\s*(moi|nous)|)"
        self.HELPFUL = ur"(?:c'?\s*(?:(e|é)tai[st]?|e(?:st?|ts?))\s*|)(?:une?\s*info(?:rmations?)\s*|)(?:ass(?:ez|(e|é)e?)\s*|)utiles?"
        self.THANK = ur"thx|[cs]imer(?:\s*bro|h?omer|albert?)|mer[csk]i\s*(?:b(?:eau|o|)c(?:ou|)p|)"
        self.GREAT = ur"nickele?|nice|g(e|é)niale?|pas?\s*male?|(?:tr(?:(e|é|è)s|op?)\s*)biens?"
        self.BYE = ur"au\s*re?v(?:oi?|i?o)r[ers]?|[+a]\+\s*(?:dans\s*l['e]?\s*bus|)"
        self.rBYE = (
            ur"^\s*(?:" +
                ur"(?P<GREAT1>" + self.GREAT + ur"\s*(?:[,\.!]\s*|)|)" + ur"(?P<HELPFUL1>" + self.HELPFUL + ur"\s*(?:[,\.!]\s*|)|)" +
                ur"|(?P<THATSALL>" + self.THATSALL + ur"\s*([,\.!]\s*|))" +
            ur")(?:" +
                ur"(?P<THANK1>" + self.THANK + ur"\s*(?:,\s*|et\s*|))" + ur"(?P<BYE1>" + self.BYE + ur"\s*|)" +
                ur"|(?P<BYE2>" + self.BYE + ur")\s*" + ur"(?P<THANK2>(?:[,\.!]\s*|et\s*|)" + self.THANK + ur"\s*|)" +
            ur")(?:[\.!]\s*|)$"
        )
        self.rTHANKS = (
            ur"^\s*(?P<GREAT>" + self.GREAT + ur"\s*(,\s*)|)(?:" +
                ur"(?P<HELPFUL>" + self.HELPFUL + ur"\s*(,\s*)|)(?P<THANK>" + self.THANK + ur")" +
                ur"|(?P<THANK>" + self.THANK + ur"\s*(,\s*)|)(?P<HELPFUL>" + self.HELPFUL + ur")" +
            ur")(?:[\.!]\s*|)$"
        )
        self.rREQALTS = (
            # heading part : [isthere|iwant|canihave|mayihave]
            ur"^\s*(?:" +
                ur"(?:j[e']?\s*|on|nous)\s*" +
                ur"(?:en\s*)?" +
                ur"(?:" +
                    ur"v(?:oudr(?:ai[estx]|i?on[st])|eu[stx])" +
                    ur"|pr(e|é)f(e|è)re(?:rai[est]|s|)\s*" +
                    ur"|aimerai[est]|peu[stx]?\s*avoir" +
                    ur"|" +
                ur")\s*" +
                ur"|y'?\s*a-?\s*t-?\s*ils?\s*" +
                ur"|p(?:uis|eu[stx]|ourrai[est])-?\s*(?:je|on)\s*avoir\s*" +
            ur"|)" +
            # Central part : <(an)other|alternative>
            ur"(?:" +
                ur"(?:(?:une?(?:\s*(?:choses?|trucs?|machins?|options?|propositions?))?|quell?e?\s*que\s*chose\s*d[e']?|choses?|trucs?|machins?|options?|propositions?|choi[esx]|d'?)\s*|)" +
                ur"(autres?|diff(e|é)rente?s?|alternati[fv]e?s?)" +
                ur"(?:\s*(?:choses?|trucs?|machins?|options?|propositions?|choi[esx])|)" +
            ur")" +
            # if available
            ur"(?:si\s*(?:vous\s*avez(?:\s*(c|\xc3\xa7)e?l?a|)|t[u']?\s*as?(?:\s*(c|\xc3\xa7)e?l?a|)|(?:(?:c(?:'|ela)\s*est\s*|)possible))|)" +
            # Tail : courtesy
            ur"(?:\s*s'?\s*(?:il\s*|)(?:te?|v(?:ous|))\s*p(?:la[iî][st]|)|)" +
            # Quesiton mark for correctness
            ur"\s*(?:\?\s*|)$" +

            # idontwantthis
            ur"|^\s*(?:j(?:e\s*n'?\s*en?|'?\s*en)\s*|on\s*(?:n['e]?\s*|)|)" +
            ur"veu[stx]\s*pas" +
            ur"(?:\s*(?:d['e]\s*|)(c|\xc3\xa7)(?:e?l?a|elui-?\s*(?:ci|l(a|à))|et?t?e?s?\s*(?:choses?|trucs?|machins?|options?|propositions?|choi[esx]))|)\s*(?:!\s*|)$"
        )
        self.rREPEAT = (
            ur"^\s*(?:(?:tu\s*|)peu[stx]?\s*(?:-\s*tu\s*|)|(?:vous\s*|)pouvez\s*(?:-\s*vous\s*|)|)" +
            ur"(r(?:(e|é)p(e|é|è)te[rsz]?|edi[str]?e?s?))" +
            ur"(?:\s*(c|\xc3\xa7)e?l?a|)" +
            # Tail : courtesy
            ur"(?:\s*s'?\s*(?:il\s*|)(?:te?|v(?:ous|))\s*p(?:la[iî][st]|)|)" +
            # Quesiton mark for correctness
            ur"\s*(?:\?\s*|)$"
        )

        self.rTYPE = (
            ur"(genre|type)"
        )

        # The remaining regex are for the slot,value dependent acts - and so here in the base class are \
        # just aiming to catch intent.
        # REQUESTS:
        self.WHATIS = ur"(?:(?:quell?e?\s*(?:est|sont)\s*)?l[ea]|combien\s*(?:y'?\s*)?a-?\s*t-\s*il\sde|s(?:['i]?\s*il|i)\s*(?:y'?\s*)?a(?:\s*d[eu]s?\b)?)"
        self.IT = ur"l[ae]s?"
        self.CYTM = ur"(?:(?:(?:tu\s*)?peu[stx]?\s*(?:-\s*tu\s*)?)?me\s*dire|di[st]\s*moi)"
        self.NEGATE =ur"((i\ )*(don\'?t|do\ not|does\ not|does\'?nt)\ (care|mind|matter)(\ (about|what))*(\ (the|it\'?s*))*)"
        self.DONTCARE = (ur"()(?:(?:(?:je\s*)?m|(?:on\s*)?s)'?en?\s*(?:f(?:iche|ou[st])|tape|cogne|branle|bat\s*les\s*couilles)\s*(?:d[ue]s?)?" +
            ur"|(?:c'?e(?:st?|ts?)\s*)?pas?\s*graves?" +
            ur"|(c|\xc3\xa7)a\s*importe\s*p(?:as?|eu)" +
            ur"|peu[stx]?\s*importe(?:\s*l[ae]s?)?" +
            ur"|(?:j'?\s*en\s*ai\s*)?rien\s*(a|à)\s*(?:f(?:out|ai)re|battre|cir(e|é)r?)(?:\s*de\s*(c|\xc3\xa7)a)?" +
            ur"|ba(?:llec|t\s*les\s*couilles|lais?\s*couilles?)(?:\s*fr(e|è)re?)?" +
        ")")
        self.DONTCAREWHAT = "(i\ dont\ care\ what\ )"
        self.DONTCAREABOUT = "(i\ dont\ care\ about\ )"
        self.rREQUEST = ur"(\b|^|\s)("+self.CYTM+r"\s*("+self.WHATIS+r"|"+self.IT+r"))"
        # INFORMS:
        self.WANT = ur"(?:pourquoi\s*pas?|(?:j[e']|on)\s*v(?:eu[stx]|oudron[st])(?:\s*qu'?il\s*y\s*(?:aie?t?s?|est?|ets?))?|avec|j'ai\s*besoin\s*d[e']|(?:je\s*)(?:re)?cherche|(?:je\s*suis?\s*)habitue\s*a)(?:\s*(?:une?|des?|du))?"
        self.WBG = ur"(?:(?:serr?ai[est]\s*"+self.GREAT+ur")(?:$|[^\?]$))"
        self.rINFORM = ur"(?:\b|^|\ )"+self.WANT
        self.rINFORM_DONTCARE = self.DONTCARE+ur"\s*(?:comment|(a|à)\s*quell?e?\s*point?|si)\s*c'?e(?:st?|ts?)"
        self.rINFORM_DONTWANT = ur"(?:je\s*[nl]e\s*veu[estx]\s*pas?(?:\s*que\s*(c|\xc3\xa7)[ae]\s*so[iy][est]s?))"
        # Contextual dontcares: i.e things that should be labelled inform(=dontcare)
        self.rCONTEXTUAL_DONTCARE = self.DONTCARE
        # The following are NOT regular expresions, but EXACT string matching:
        self.COMMON_CONTEXTUAL_DONTCARES = [ur"(?:n'?|peu[st]?)\s*(importe)(?:\s*quoi)?", self.DONTCARE]
        self.COMMON_CONTEXTUAL_DONTCARES += ["it doesn\'t matter", "dont care"]

        self.general_INFORM = ur"(?:(?:j[e']|on)\s*(?:(?:v(?:eu|oudrai)[stx]?|pr(e|é)f(e|è)re(?:rai[stx]?|s|)|(?:aime(?:rai[stx]?|s|)))\s*(?:biens?|)|(?:ai|aurai[stx]?)\s*(?:biens?|)\s*(?:besoin|envie)(?:\s*d[e'])?)\s*(?:que\s*(c|\xc3\xa7)e?l?[ae]\s*so(?:i[stx]?|yen?t?s?)|quel(?:les?\s*)?que\s*chose\s*d['e]|une?\s*(?:truc|machin)s?|))"
        
        self.contextual_NOT = ur"(?:n(?:o(?:n|pe)|an)|(?:absolument|surtout|certainement)\s*pas?|pas?\s*du\s*tou[stx]?|pas\s*celui-?\s*l[aà]|un\s*autres?)"
        self.contextual_YES = ur"(?:oua?is?|ye[ps]|tou[stx]\s*(a|à)\s*fai[st](?:\s*le\s*f(?:ai|eu?)san[st])?|absolument)"
        self.contextual_DONTCARE = (ur"()(?:(?:(?:je\s*)?m|(?:on\s*)?s)'?en?\s*(?:f(?:iche|ou[st])|tape|cogne|branle|bat\s*les\s*couilles)\s*(?:d[ue]s?)?" +
            ur"|(?:c'?e(?:st?|ts?)\s*)?pas?\s*graves?" +
            ur"|(c|\xc3\xa7)a\s*importe\s*p(?:as?|eu)" +
            ur"|(n'?|peu[stx]?)\s*importe(?:\s*l[ae]s?)?" +
            ur"|(?:j'?\s*en\s*ai\s*)?rien\s*(a|à)\s*(?:f(?:out|ai)re|battre|cir(e|é)r?)(?:\s*de\s*(c|\xc3\xa7)a)?" +
            ur"|ba(?:llec|t\s*les\s*couilles|lais?\s*couilles?)(?:\s*fr(e|è)re?)?" +
        ")")

        # self.contextual_COM_DRAMA = ur"(com(e|é)die?s\s*dramatique?s)"
        # self.contextual_DIVERS = ur"(divers)"
        self.contextual_COMEDIE = ur"(comm?(e|é)dies?|drole|comm?iques?|((qui)?\s*fai[st]\s*(moi)?|je\s*veux?)\s*rire)"
        self.contextual_ADVENTURE = ur"(?:(d')?\s*aventures?)"
        # self.contextual_ANIMATION = ur"(?:(?:an?nimation?s|?(dessin)?s\s*anim(e|é)?s))"
        self.contextual_ANIMATION = ur"(?:(d')?\s*ann?imations?|(dessins?)?\s*an?nim(e|é)e?s?)"
        # self.contextual_COPS = ur"(policier?s|?(d')?(\s*)enqu(e|ê)te?s?(criminelle?s))"
        self.contextual_DARK_COPS = ur"((d')?(\s*)?enqu(e|\xc3\xaa)tes?(criminelles?)?)|noir\s*(policiers?)?"
        # self.contextual_DRAME = ur"(?:?(d')\s*dram(atique|e)?s|triste?s)"
        self.contextual_DRAME = ur"(dram(atique|e)s?|tristes?)"
        # self.contextual_HOROR = ur"(?:?(qui\s*)?(fait\s*)peur|horeur?s|(e|é)pouvante?s)"
        self.contextual_HOROR = ur"(?:peur|(d')?\s*horr?eurs?|(d')?\s*(e|é)pouvante(s)?)"
        self.contextual_HISTORY = ur"(?:(d')?\s*histo(?:rique|ire)s?)"
        self.contextual_THRILLER = ur"(?:(thriller|suspense?)s?)"
        self.contextual_BIOPIC = ur"(?:(auto)?bio(graphi((que|e)|pic))?s?)"
        # self.contextual_ROMANCE = ur"((romance|?(d')\s*amours|?(à|a)\s*?(l')\s*de\s*rose)?s)"
        self.contextual_ROMANCE = ur"(roman(tique|ce)s?|(d'?\s*)amours?|(a|à)\s*l'eau\s*de\s*r(o|au)se)"
        self.contextual_ACTION = ur"(?:((d')?\s*action|bagarr?es?|course\s*poursuite|(d('|es))?\s*explosion)s?)"
        self.contextual_WAR = ur"(?:(guerre|bataill?e|confli?t)s?)"
        self.contextual_FANTASTIQUE = ur"(?:(fantastique|imaginn?aire)s?)"
        # self.contextual_SCIENCE_FICTION = ur"(science(-|\s*)fiction?s|futur(ist(e|ique))?s|espace?s|fictif?s|super\s*h(é|e)ro?s|marvel?s)"

        ####Restriction####
        self.contextual_MORE6 = ur"(?:((plus)?\s*(de)?\s*(6|six)\sans))" #OK
        self.contextual_MORE12 = ur"(?:(((plus)?\s*(de)?\s*(12|douze)\sans)|interdit\s(au(x)?)?\s*(moins)?\s*(de)?\s*(12|douze)\sans))"
        self.contextual_FORALL = ur"(?:((tou(s|t)?\s*public(s)?)|(pour)?\s*tou(s|t)?)|non\s*violent?)" #OK
        self.contextual_NONE = ur"(?:pas?(?:\s*du\s*tou[stx]?|)|sans\s*(restriction|limites)?|non|aucunes?)"
        self.contextual_SENSIBLE = ur"(p(eut|ouvant)\s*heurter\s*[lm]a\s*sensibilit(e|é)|polemique|adulte|(plus|interdit?\s*au[xs]?\s*moins?)\s*(de)?\s*(18|dix-?\s*huit|16|seize)\s*(ans?)?|sensibles?)"


    def create_domain_dependent_regex(self):
        """Can overwrite any of the regular expressions set in RegexParser.RegexParser.init_regular_expressions().
        This doesn't deal with slot,value (ie domain dependent) semantics. For those you need to handcraft
        the _decode_[inform,request,confirm] etc.
        """
        # REDEFINES OF BASIC SEMANTIC ACTS (ie those other than inform, request): (likely nothing needs to be done here)
        #eg: self.rHELLO = "anion"

        self._domain_init(dstring=self.domainTag)

        # DOMAIN DEPENDENT SEMANTICS:
        self.slot_vocab = dict.fromkeys(self.USER_REQUESTABLE,'')
        # FIXME: define slot specific language -  for requests
        #---------------------------------------------------------------------------------------------------
        #exit("THESE NEED FIXING FOR THIS DOMAIN")

            # REGEXs
        self.slot_vocab["name"] = ur"(film|titre|nom)"
        self.slot_vocab["release"] = ur"(((date|jour)\s*de\s*)?sortie)"
        self.slot_vocab["duration"] = ur"(dur(é|e)e)"
        self.slot_vocab["synopsis"] = ur"(de\s*quoi\s*(\xc3\xa7|c)a\s*parle|trame|sc(e|é)nario|intrigue|synopsis|description|r(é|e)sum(é|e))"
        self.slot_vocab["restriction"] = ur"(restriction)"
        self.slot_vocab["genre"] = ur"(genre|type|style|nature|cath(e|é)gorie)"

        #---------------------------------------------------------------------------------------------------
        # Generate regular expressions for requests:
        self._set_request_regex()


        # FIXME:  many value have synonyms -- deal with this here:
        self._set_value_synonyms()  # At end of file - this can grow very long
        self._set_inform_regex()
    
    def _set_request_regex(self):
        """
        """
        self.request_regex = dict.fromkeys(self.USER_REQUESTABLE)
        for slot in self.request_regex.keys():
            # FIXME: write domain dependent expressions to detext request acts
            self.request_regex[slot] = self.rREQUEST+ur"\s*"+self.slot_vocab[slot]
            self.request_regex[slot] += "|"+self.IT+ur"\s*"+self.slot_vocab[slot]
            
            # To remove for no synopsis
        # self.request_regex["synopsis"] = ur"(de\s*quoi\s*(\xc3\xa7|c)a\s*parle|trame|sc(e|é)nario|intrigue|synopsis|description|r(é|e)sum(é|e)|di[st]\s*(m'(\s*)?en)?\s*plus|c'est?\s*quoi)"

    def _set_inform_regex(self):
        """
        """
        self.inform_absolute = dict.fromkeys(self.USER_INFORMABLE)
        self.inform_contextual = dict.fromkeys(self.USER_REQUESTABLE)

        for slot in self.inform_contextual.keys():
            self.inform_contextual[slot] = {}
            for value in self.slot_values[slot].keys():
                # if value == "0":
                #     self.inform_contextual[slot][value] = self.contextual_NOT
                # elif value == "1":
                #     self.inform_contextual[slot][value] = self.contextual_YES

                #### Genres 
                # if value == "comedie dramatique":
                #     self.inform_contextual[slot][value] = self.contextual_COM_DRAMA
                # if value == "divers":
                #     self.inform_contextual[slot][value] = self.contextual_DIVERS
                if value == "comedie":
                    self.inform_contextual[slot][value] = self.contextual_COMEDIE
                elif value == "aventure":
                    self.inform_contextual[slot][value] = self.contextual_ADVENTURE
                elif value == "animation":
                    self.inform_contextual[slot][value] = self.contextual_ANIMATION
                    # elif value == "film policier":
                    #     self.inform_contextual[slot][value] = self.contextual_COPS
                elif value == "noirpolicier":
                    self.inform_contextual[slot][value] = self.contextual_DARK_COPS
                elif value == "drame":
                    self.inform_contextual[slot][value] = self.contextual_DRAME
                elif value == "epouvantehorreur":
                    self.inform_contextual[slot][value] = self.contextual_HOROR
                elif value == "historique":
                    self.inform_contextual[slot][value] = self.contextual_HISTORY
                elif value == "thriller":
                    self.inform_contextual[slot][value] = self.contextual_THRILLER
                elif value == "biopic":
                    self.inform_contextual[slot][value] = self.contextual_BIOPIC
                elif value == "romance":
                    self.inform_contextual[slot][value] = self.contextual_ROMANCE
                elif value == "action":
                    self.inform_contextual[slot][value] = self.contextual_ACTION
                elif value == "guerre":
                    self.inform_contextual[slot][value] = self.contextual_WAR
                elif value == "fantastique":
                    self.inform_contextual[slot][value] = self.contextual_FANTASTIQUE
                elif value == "forall": ### Restrictions
                    self.inform_contextual[slot][value] = self.contextual_FORALL
                elif value == "more12":
                    self.inform_contextual[slot][value] = self.contextual_MORE12
                elif value == "more6":
                    self.inform_contextual[slot][value] = self.contextual_MORE6
                elif value == "none":
                    self.inform_contextual[slot][value] = self.contextual_NONE
                elif value == "sensible":
                    self.inform_contextual[slot][value] = self.contextual_SENSIBLE
                else:
                    continue
                self.inform_contextual[slot][value] = ur"^\s*" + self.inform_contextual[slot][value] + ur"\s*$"

        for slot in self.inform_absolute.keys():
            self.inform_absolute[slot] = {}
            for value in self.slot_values[slot].keys():
                self.inform_absolute[slot][value] = ur"^\s*(?:" + self.general_INFORM + ur"\s*" +  self.slot_values[slot][value] + ur"|" + self.slot_values[slot][value] + self.WBG + ur")\s*$"

        self.inform_regex = dict.fromkeys(self.USER_INFORMABLE)
        for slot in self.inform_regex.keys():
            self.inform_regex[slot] = {}
            self.inform_regex[slot]['dontcare'] = ''
            for value in self.slot_values[slot].keys():
                self.inform_regex[slot][value] = (self.general_INFORM + ur"\s*" + self.slot_values[slot][value] +
                    ur"|" + self.slot_values[slot][value])
            s = (self.DONTCARE + ur"(?:\s*(?:comment|(a|à)\s*quell?e?\s*point?|si)\s*c'?e(?:st?|ts?)\s*(" +
                "|".join([self.slot_values[slot][value] for value in self.slot_values[slot].keys()])
                + ur")(?:\s*ou\s*pas?)?)")

            if (self.inform_regex[slot]['dontcare'] != ''):
                s = "|" + s
            self.inform_regex[slot]['dontcare'] += s


                # FIXME:  Handcrafted extra rules as required on a slot to slot basis:

            # FIXME: value independent rules:

    def _generic_request(self,obs,slot):
        """
        """
        if self._check(re.search(self.request_regex[slot],obs, re.I)):
            self.semanticActs.append('request('+slot+')')

    def _generic_inform(self, obs, slot):
        """
        """
        DETECTED_SLOT_INTENT = False
        '''for value in self.inform_contextual[slot].keys():
            if self._check(re.search(self.inform_contextual[slot][value], obs, re.I)):
                # -> informed !
                print u"Recognized [Contextual] : " + slot + u"::" + value
                pass
            elif self._check(re.search(self.inform_absolute[slot][value], obs, re.I)):
                #informed
                print u"Recognized [Absolute] : " + slot + u"::" + value
                pass
        for other_slot in self.inform_absolute.keys():
            if (other_slot == slot):
                continue
            for value in self.inform_absolute[slot].keys():
                if (self._check(re.search(self.inform_absolute[slot][value], obs, re.I))):
                    print u"Recognized [Absolute|Other(" + slot + u")] : " + other_slot + u"::" + value'''
        obs = re.sub(ur"\s{2,}", ' ', obs)
        # print(self.slot_values[slot].keys())
        for value in self.slot_values[slot].keys():
            # print slot + "::" + value
            # print(self.inform_regex[slot][value],obs, re.I)
            # print(re.search(self.inform_regex[slot][value],obs, re.I))
            if self._check(re.search(self.inform_regex[slot][value],obs, re.I)):
                # print slot + "::" + value
                #FIXME:  Think easier to parse here for "dont want" and "dont care" - else we're playing "WACK A MOLE!"
                ADD_SLOTeqVALUE = True
                # Deal with -- DONTWANT --:
                if self._check(re.search(self.rINFORM_DONTWANT + r"\s*" + self.slot_values[slot][value], obs, re.I)):
                    self.semanticActs.append('inform('+slot+'!='+value+')')  #TODO - is this valid?
                    ADD_SLOTeqVALUE = False
                # Deal with -- DONTCARE --:
                elif self._check(re.search(self.rINFORM_DONTCARE + r"\s*" + value, obs, re.I)) and not DETECTED_SLOT_INTENT:
                    self.semanticActs.append('inform('+slot+'=dontcare)')
                    ADD_SLOTeqVALUE = False
                    DETECTED_SLOT_INTENT = True
                # Deal with -- REQUESTS --: (may not be required...)
                #TODO? - maybe just filter at end, so that inform(X) and request(X) can not both be there?
                elif ADD_SLOTeqVALUE and not DETECTED_SLOT_INTENT:
                    self.semanticActs.append('inform('+slot+'='+value+')')

    def _decode_request(self, obs):
        """
        """
        # if a slot needs its own code, then add it to this list and write code to deal with it differently
        DO_DIFFERENTLY= [] #FIXME
        for slot in self.USER_REQUESTABLE:
            if slot not in DO_DIFFERENTLY:
                self._generic_request(obs,slot)
        # Domain independent requests:
        self._domain_independent_requests(obs)

    def _decode_inform(self, obs):
        """
        """
        # if a slot needs its own code, then add it to this list and write code to deal with it differently
        DO_DIFFERENTLY = [] #FIXME
        for slot in self.USER_INFORMABLE:
            if slot not in DO_DIFFERENTLY:
                self._generic_inform(obs,slot)
        # Check other statements that use context
        self._contextual_inform(obs)

    def _decode_type(self,obs):
        """
        """
        # This is pretty ordinary - will just keyword spot for now since type really serves no point at all in our system
        if self._check(re.search(self.inform_type_regex,obs, re.I)):
            self.semanticActs.append('inform(type='+self.domains_type+')')


    def _decode_confirm(self, obs):
        """
        """
        #TODO?
        pass

    def _set_value_synonyms(self):
        """Starts like:
            self.slot_values[slot] = {value:"("+str(value)+")" for value in domain_ontology["informable"][slot]}
            # Can add regular expressions/terms to be recognised manually:
        """
        #FIXME:
        #---------------------------------------------------------------------------------------------------
        #exit("THESE NEED FIXING FOR THIS DOMAIN")

        # TYPE:
        self.inform_type_regex = ur"(film)"
        # SLOT: stars
        # {u'west': '(west)', u'east': '(east)', u'north': '(north)', u'south': '(south)', u'centre': '(centre)'}
        regex_de = "?(d'\s*|de\s*)"
        regex_qui = "?(qui\s*)"
        regex_en = "?(en)"

        ### Genres
        slot = 'genre'

        self.slot_values[slot]['comedie'] = ur"(" + self.contextual_COMEDIE + ur")"
        self.slot_values[slot]['aventure'] = ur"(" + self.contextual_ADVENTURE + ur")"
        self.slot_values[slot]['animation'] = ur"(" + self.contextual_ANIMATION + ur")"
        # self.slot_values[slot]['film policier'] = ur"(" + self.contextual_COPS + ur")"
        self.slot_values[slot]['noirpolicier'] = ur"(" + self.contextual_DARK_COPS + ur")"
        self.slot_values[slot]['drame'] = ur"(" + self.contextual_DRAME + ur")"
        self.slot_values[slot]['epouvantehorreur'] = ur"(" + self.contextual_HOROR + ur")"
        self.slot_values[slot]['historique'] = ur"(" + self.contextual_HISTORY + ur")"
        self.slot_values[slot]['thriller'] = ur"(" + self.contextual_THRILLER + ur")"
        self.slot_values[slot]['biopic'] = ur"(" + self.contextual_BIOPIC + ur")"
        self.slot_values[slot]['romance'] = ur"(" + self.contextual_ROMANCE + ur")"
        self.slot_values[slot]['action'] = ur"(" + self.contextual_ACTION + ur")"
        self.slot_values[slot]['guerre'] = ur"(" + self.contextual_WAR + ur")"
        self.slot_values[slot]['fantastique'] = ur"(" + self.contextual_FANTASTIQUE + ur")"
        # self.slot_values[slot]['science-fiction'] = ur"(" + self.contextual_SCIENCE_FICTION + ur")"
        
        ### Restrictions
        slot = 'restriction'
        self.slot_values[slot]['forall'] = ur"(" + self.contextual_FORALL + ur")"
        self.slot_values[slot]['more12'] = ur"(" + self.contextual_MORE12 + ur")"
        self.slot_values[slot]['more6'] = ur"(" + self.contextual_MORE6 + ur")"
        self.slot_values[slot]['none'] = ur"(" + self.contextual_NONE + ur")"
        self.slot_values[slot]['sensible'] = ur"(" + self.contextual_SENSIBLE + ur")"
        #---------------------------------------------------------------------------------------------------


#END OF FILE
