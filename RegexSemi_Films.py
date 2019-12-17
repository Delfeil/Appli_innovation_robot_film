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


class RegexSemI_KUSTOM(RegexSemI.RegexSemI):
    """
    """
    def __init__(self, repoIn=None):
        RegexSemI.RegexSemI.__init__(self)  #better than super() here - wont need to be changed for other domains
        self.domainTag = "Films"  #FIXME
        self.create_domain_dependent_regex()
    
    def init_regular_expressions(self):
        self.rHELLO = ur"^\s*(?:s(?:lt|alut?)|b(?:on|'|)j(?:ou)?r?|coucous?|cc|wesh|yo)\s"
        self.THANK = ur"thx|[cs]imer(?:\s*bro|h?omer|albert?)|mer[csk]i\s*(?:b(?:eau|o|)c(?:ou|)p|)"
        self.GREAT = ur"nickele?|nice|g[eé]niale?|pas?\s*male?|(?:tr(?:[eéè]s|op?)\s*)biens?"
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
                    ur"|pr[eé]f[eè]re(?:rai[est]|s|)\s*" +
                    ur"|aimerai[est]|peu[stx]?\s*avoir" +
                    ur"|" +
                ur")\s*" +
                ur"|y'?\s*a-?\s*t-?\s*ils?\s*" +
                ur"|p(?:uis|eu[stx]|ourrai[est])-?\s*(?:je|on)\s*avoir\s*" +
            ur"|)" +
            # Central part : <(an)other|alternative>
            ur"(?:" +
                ur"(?:(?:une?(?:\s*(?:choses?|trucs?|machins?|options?|propositions?))?|quell?e?\s*que\s*chose\s*d[e']?|choses?|trucs?|machins?|options?|propositions?|choi[esx]|d'?)\s*|)" +
                ur"(autres?|diff[eé]rente?s?|alternati[fv]e?s?)" +
                ur"(?:\s*(?:choses?|trucs?|machins?|options?|propositions?|choi[esx])|)" +
            ur")" +
            # if available
            ur"(?:si\s*(?:vous\s*avez(?:\s*[cç]e?l?a|)|t[u']?\s*as?(?:\s*[cç]e?l?a|)|(?:(?:c(?:'|ela)\s*est\s*|)possible))|)" +
            # Tail : courtesy
            ur"(?:\s*s'?\s*(?:il\s*|)(?:te?|v(?:ous|))\s*p(?:la[iî][st]|)|)" +
            # Quesiton mark for correctness
            ur"\s*(?:\?\s*|)$" +

            # idontwantthis
            ur"|^\s*(?:j(?:e\s*n'?\s*en?|'?\s*en)\s*|on\s*(?:n['e]?\s*|)|)" +
            ur"veu[stx]\s*pas" +
            ur"(?:\s*(?:d['e]\s*|)[cç](?:e?l?a|elui-?\s*(?:ci|l[aà])|et?t?e?s?\s*(?:choses?|trucs?|machins?|options?|propositions?|choi[esx]))|)\s*(?:!\s*|)$"
        )
        self.contextual_NOT = ur"(?:n(?:o(?:n|pe)|an)|(?:absolument|surtout|certainement)\s*pas?|pas?\s*du\s*tou[stx]?)"
        self.contextual_YES = ur"(?:oua?is?|ye[ps]|tou[stx]\s*[aà]\s*fai[st](?:\s*le\s*f(?:ai|eu?)san[st])?|absolument)"
        self.contextual_DONTCARE = (ur"()(?:(?:(?:je\s*)?m|(?:on\s*)?s)'?en?\s*(?:f(?:iche|ou[st])|tape|cogne|branle|bat\s*les\s*couilles)\s*(?:d[ue]s?)?" +
            ur"|(?:c'?e(?:st?|ts?)\s*)?pas?\s*graves?" +
            ur"|[cç]a\s*importe\s*p(?:as?|eu)" +
            ur"|peu[stx]?\s*importe(?:\s*l[ae]s?)?" +
            ur"|(?:j'?\s*en\s*ai\s*)?rien\s*[aà]\s*(?:f(?:out|ai)re|battre|cir[eé]r?)(?:\s*de\s*[cç]a)?" +
            ur"|ba(?:llec|t\s*les\s*couilles|lais?\s*couilles?)(?:\s*fr[eè]re?)?" +
        ")")
        self.contextual_NONE = ur"(?:pas?(?:\s*du\s*tou[stx]?|)|sans|non)"

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
            self.slot_vocab["titre"] = ur"(film|titre)"
            self.slot_vocab["release_date"] = ur"((?:date*de\s*)?sortie)"
            self.slot_vocab["duration"] = ur"(dur(é|e)e)"
            self.slot_vocab["synopsis"] = ur"(synopsis|description|r(é|e)sum(é|e))"
            self.slot_vocab["restriction"] = ur"(restriction)"
            self.slot_vocab["genre"] = ur"(genre|type)"

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

    def _set_inform_regex(self):
        """
        """
        self.inform_absolute = dict.fromkeys(self.USER_INFORMABLE)
        self.inform_contextual = dict.fromkeys(self.USER_REQUESTABLE)

        for slot in self.inform_contextual.keys():
            self.inform_contextual[slot] = {}
            for value in self.slot_values[slot].keys():
                if value == "0":
                    self.inform_contextual[slot][value] = self.contextual_NOT
                elif value == "1":
                    self.inform_contextual[slot][value] = self.contextual_YES
                elif value == "free":
                    self.inform_contextual[slot][value] = self.contextual_NONE
                elif value == "little":
                    self.inform_contextual[slot][value] = self.contextual_LITTLE
                elif value == "fair":
                    self.inform_contextual[slot][value] = self.contextual_FAIR
                elif value == "much":
                    self.inform_contextual[slot][value] = self.contextual_MUCH
                elif value == "enormous":
                    self.inform_contextual[slot][value] = self.contextual_VERYMUCH
                elif value == "full":
                    self.inform_contextual[slot][value] = self.contextual_COMPLETELY
                elif value == "dontcare":
                    self.inform_contextual[slot][value] = self.contextual_DONTCARE
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
            s = (self.DONTCARE + ur"(?:\s*(?:comment|[aà]\s*quell?e?\s*point?|si)\s*c'?e(?:st?|ts?)\s*(" +
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
        for value in self.slot_values[slot].keys():
            if self._check(re.search(self.inform_regex[slot][value],obs, re.I)):
                print slot + "::" + value
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
        # SLOT: stars
        # Genres
        slot = 'genre'
        # {u'west': '(west)', u'east': '(east)', u'north': '(north)', u'south': '(south)', u'centre': '(centre)'}
        regex_de = "(d'\s*|de\s*)?"
        regex_qui = "(qui\s*)?"
        regex_en = "(en)?"
        self.slot_values[slot]['action'] = ur"("+regex_de+"action|"+regex_qui+"bouge)"
        self.slot_values[slot]['horeur'] = ur"("+regex_de+"(horreur|(\xc3\xa9|e)pouv(a|e)nte|peur)|"+regex_qui+"(fait\s*)?peur)"
        self.slot_values[slot]['animation'] = ur"(("+regex_de+"|"+regex_en+"|dessin(s)?)\s(anim(ation|é)?|image(s)?\s*"+regex_de+"synth(e|é)se(s)?))"
        self.slot_values[slot]['thriller'] = ur"(thriller)"
        self.slot_values[slot]['comedie'] = ur"(?:n'?|peu[st]?)\s*(importe)(?:\s*quel\s*produits?)"
        self.slot_values[slot]['drame'] = ur"(?:n'?|peu[st]?)\s*(importe)(?:\s*quel\s*produits?)"
        self.slot_values[slot]['biopic'] = ur"(?:n'?|peu[st]?)\s*(importe)(?:\s*quel\s*produits?)"
        self.slot_values[slot]['historique'] = ur"(?:n'?|peu[st]?)\s*(importe)(?:\s*quel\s*produits?)"
        #---------------------------------------------------------------------------------------------------


#END OF FILE
