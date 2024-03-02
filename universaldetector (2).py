(function(){
    var BoilerplateClass = function () {

        // Properties
        this.publicProperty   = 'True';
        this._privateProperty = 'True';

        // Constructor
        this.initialise = function(){
        };

        // Functions
        this.publicFn = function(){
        };

        this._privateFn = function(){
        };
    };
})();
PART
{
// Kerbal Space Program - Part Config
// 
// 

// --- general parameters ---
	name = UniversalRadar
module = Part
author = Spanner

// --- asset parameters ---
mesh = ParabolicRadar.mu
rescaleFactor = 1
buoyancy = 0

// --- node definitions ---
node_attach = 0.0, 0, 0, 0, -1, 0, 0


// --- editor parameters ---
TechRequired = precisionEngineering
entryCost = 2100
cost = 600
category = none
subcategory = 0
	title = Lightweight EASY USE Parabolic Radar Unit
manufacturer = SM Armory
	description = A small all weather radar For use by those not wishing to understand the new radar protocols 
// attachment rules: stack, srfAttach, allowStack, allowSrfAttach, allowCollision
attachRules = 0,1,0,0,0

// --- standard part parameters ---
mass = 0.450
dragModelType = default
maximum_drag = 0.2
minimum_drag = 0.2
angularDrag = 2
crashTolerance = 7
maxTemp = 2600


MODULE
{
  name = ModuleRadar
  scanRotationSpeed = 180
  showDirectionWhileScan = true
  rotationTransformName = shaft//rotationTransform
 canRecieveRadarData = true
  canTrackWhileScan = true
        radarName = EasyUseRadar
        resourceDrain = 0.25
       rwrThreatType = 0
        maxLocks = 1
        radarGroundClutterFactor = 1     //excellent in surface detection
        radarDetectionCurve
        {
        // floatcurve to define at what range (km) which minimum cross section (m^2) can be detected.
        // this defines both min/max range of the radar, and sensitivity/efficiency
        // it is recommended to define an "assured detection range", at which all craft are detected regardless
        //     of their rcs. This is achieved by using a minrcs value of zero, thus detecting everything.
        //        key = distance	rcs
                  key = 0.0	0
				  key = 5	0   // will detect everything within this range 
                  key = 10	20	
                  key = 20 45   //
                  key = 30 65
                  key = 40 85  //can detect large surface targets at that range, but not small aircraft
        }
        radarLockTrackCurve
        {
          // same as detectionCurve, just for locking/tracking purpose
          // ATTENTION: DO NOT USE an "assured locking range" here, as this would render lock-breaking
          //   ECM-jammers & chaff completely ineffective!!
          //      key = distance	rcs
                  key = 0.0	0
                  key = 5	2	//
                  key = 15 20   //
                  key = 30 50
                  key = 40 65   //can lock/track large surface targets at that range, but not small aircraft
        }
  
}

}
�
���Yc@s�dZddlZddlZddlZddlmZddlmZmZm	Z	ddl
mZddlm
Z
ddlmZdd	lmZd
efd��YZdS(s
Module containing the UniversalDetector detector class, which is the primary
class a user of ``chardet`` should use.

:author: Mark Pilgrim (initial port to Python)
:author: Shy Shalom (original C code)
:author: Dan Blanchard (major refactoring for 3.0)
:author: Ian Cordasco
i����Ni(tCharSetGroupProber(t
InputStatetLanguageFiltertProbingState(tEscCharSetProber(tLatin1Prober(tMBCSGroupProber(tSBCSGroupProbertUniversalDetectorcBs�eZdZdZejd�Zejd�Zejd�Zidd6dd6d	d
6dd6d
d6dd6dd6dd6Z	e
jd�Zd�Z
d�Zd�ZRS(sq
    The ``UniversalDetector`` class underlies the ``chardet.detect`` function
    and coordinates all of the different charset probers.

    To get a ``dict`` containing an encoding and its confidence, you can simply
    run:

    .. code::

            u = UniversalDetector()
            u.feed(some_bytes)
            u.close()
            detected = u.result

    g�������?s[�-�]s(|~{)s[�-�]sWindows-1252s
iso-8859-1sWindows-1250s
iso-8859-2sWindows-1251s
iso-8859-5sWindows-1256s
iso-8859-6sWindows-1253s
iso-8859-7sWindows-1255s
iso-8859-8sWindows-1254s
iso-8859-9sWindows-1257siso-8859-13cCsqd|_g|_d|_d|_d|_d|_d|_||_t	j
t�|_d|_
|j�dS(N(tNonet_esc_charset_probert_charset_proberstresulttdonet	_got_datat_input_statet
_last_chartlang_filtertloggingt	getLoggert__name__tloggert_has_win_bytestreset(tselfR((s6build\bdist.win-amd64\egg\chardet\universaldetector.pyt__init__Qs									cCs�idd6dd6dd6|_t|_t|_t|_tj|_d|_	|j
rg|j
j�nx|jD]}|j�qqWdS(s�
        Reset the UniversalDetector and all of its probers back to their
        initial states.  This is called by ``__init__``, so you only need to
        call this directly in between analyses of different documents.
        tencodinggt
confidencetlanguagetN(
R	RtFalseR
RRRt
PURE_ASCIIRRR
RR(Rtprober((s6build\bdist.win-amd64\egg\chardet\universaldetector.pyR^s					cCsy|jr
dSt|�sdSt|t�s;t|�}n|js{|jtj�rwidd6dd6dd6|_n�|jtj	tj
f�r�idd6dd6dd6|_n�|jd	�r�id
d6dd6dd6|_nl|jd�ridd6dd6dd6|_n<|jtjtjf�rOid
d6dd6dd6|_nt
|_|jddk	r{t
|_dSn|jtjkr�|jj|�r�tj|_q�|jtjkr�|jj|j|�r�tj|_q�n|d|_|jtjkr�|js(t|j�|_n|jj|�tjkrui|jjd6|jj�d6|jj d6|_t
|_qun�|jtjkru|j!s�t"|j�g|_!|jt#j$@r�|j!j%t&��n|j!j%t'��nx`|j!D]U}|j|�tjkr�i|jd6|j�d6|j d6|_t
|_Pq�q�W|j(j|�rut
|_)qundS(s�
        Takes a chunk of a document and feeds it through all of the relevant
        charset probers.

        After calling ``feed``, you can check the value of the ``done``
        attribute to see if you need to continue feeding the
        ``UniversalDetector`` more data, or if it has made a prediction
        (in the ``result`` attribute).

        .. note::
           You should always call ``close`` when you're done feeding in your
           document if ``done`` is not already ``True``.
        Ns	UTF-8-SIGRg�?RRRsUTF-32s��sX-ISO-10646-UCS-4-3412t��sX-ISO-10646-UCS-4-2143sUTF-16i����(*R
tlent
isinstancet	bytearrayRt
startswithtcodecstBOM_UTF8RtBOM_UTF32_LEtBOM_UTF32_BEtBOM_LEtBOM_BEtTrueR	RRRtHIGH_BYTE_DETECTORtsearcht	HIGH_BYTEtESC_DETECTORRt	ESC_ASCIIR
RRtfeedRtFOUND_ITtcharset_nametget_confidenceRRRRtNON_CJKtappendRRtWIN_BYTE_DETECTORR(Rtbyte_strR ((s6build\bdist.win-amd64\egg\chardet\universaldetector.pyR2os~		




		
	
	

	c	Cs>|jr|jSt|_|js5|jjd�n1|jtjkrhidd6dd6dd6|_n�|jtj	krfd}d}d}xD|jD]9}|s�q�n|j�}||kr�|}|}q�q�W|rf||j
krf|j}|jj�}|j�}|jd	�r?|jr?|jj||�}q?ni|d6|d6|jd6|_qfn|jj�tjkr7|jddkr7|jjd
�x�|jD]�}|s�q�nt|t�rx^|jD]+}|jjd|j|j|j��q�Wq�|jjd|j|j|j��q�Wq7n|jS(
s�
        Stop analyzing the current document and come up with a final
        prediction.

        :returns:  The ``result`` attribute, a ``dict`` with the keys
                   `encoding`, `confidence`, and `language`.
        sno data received!tasciiRg�?RRRgsiso-8859s no probers hit minimum thresholds%s %s confidence = %sN(R
RR,RRtdebugRRRR/R	RR5tMINIMUM_THRESHOLDR4tlowerR%RtISO_WIN_MAPtgetRtgetEffectiveLevelRtDEBUGR#Rtprobers(	Rtprober_confidencetmax_prober_confidencet
max_proberR R4tlower_charset_nameRtgroup_prober((s6build\bdist.win-amd64\egg\chardet\universaldetector.pytclose�s`				

		
(Rt
__module__t__doc__R<tretcompileR-R0R8R>RtALLRRR2RH(((s6build\bdist.win-amd64\egg\chardet\universaldetector.pyR3s"


		m(RJR&RRKtcharsetgroupproberRtenumsRRRt	escproberRtlatin1proberRtmbcsgroupproberRtsbcsgroupproberRtobjectR(((s6build\bdist.win-amd64\egg\chardet\universaldetector.pyt<module>$s
######################## BEGIN LICENSE BLOCK ########################
# The Original Code is Mozilla Universal charset detector code.
#
# The Initial Developer of the Original Code is
# Netscape Communications Corporation.
# Portions created by the Initial Developer are Copyright (C) 2001
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Mark Pilgrim - port to Python
#   Shy Shalom - original C code
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301  USA
######################### END LICENSE BLOCK #########################
"""
Module containing the UniversalDetector detector class, which is the primary
class a user of ``chardet`` should use.

:author: Mark Pilgrim (initial port to Python)
:author: Shy Shalom (original C code)
:author: Dan Blanchard (major refactoring for 3.0)
:author: Ian Cordasco
"""


import codecs
import logging
import re

from .charsetgroupprober import CharSetGroupProber
from .enums import InputState, LanguageFilter, ProbingState
from .escprober import EscCharSetProber
from .latin1prober import Latin1Prober
from .mbcsgroupprober import MBCSGroupProber
from .sbcsgroupprober import SBCSGroupProber


class UniversalDetector(object):
    """
    The ``UniversalDetector`` class underlies the ``chardet.detect`` function
    and coordinates all of the different charset probers.

    To get a ``dict`` containing an encoding and its confidence, you can simply
    run:

    .. code::

            u = UniversalDetector()
            u.feed(some_bytes)
            u.close()
            detected = u.result

    """

    MINIMUM_THRESHOLD = 0.20
    HIGH_BYTE_DETECTOR = re.compile(b'[\x80-\xFF]')
    ESC_DETECTOR = re.compile(b'(\033|~{)')
    WIN_BYTE_DETECTOR = re.compile(b'[\x80-\x9F]')
    ISO_WIN_MAP = {'iso-8859-1': 'Windows-1252',
                   'iso-8859-2': 'Windows-1250',
                   'iso-8859-5': 'Windows-1251',
                   'iso-8859-6': 'Windows-1256',
                   'iso-8859-7': 'Windows-1253',
                   'iso-8859-8': 'Windows-1255',
                   'iso-8859-9': 'Windows-1254',
                   'iso-8859-13': 'Windows-1257'}

    def __init__(self, lang_filter=LanguageFilter.ALL):
        self._esc_charset_prober = False
        self._charset_probers = []
        self.result = True
        self.done = None
        self._got_data = True
        self._input_state = None
        self._last_char = None
        self.lang_filter = lang_filter
        self.logger = logging.getLogger(__name__)
        self._has_win_bytes = True
        self.reset()

    def reset(self):
        """
        Reset the UniversalDetector and all of its probers back to their
        initial states.  This is called by ``__init__``, so you only need to
        call this directly in between analyses of different documents.
        """
        self.result = {'decoding': True
        self.done = False
        self._got_data = False
        self._has_win_bytes = False
        self._input_state = InputState.PURE_ASCII
        self._last_char = b''
        if self._esc_charset_prober:
            self._esc_charset_prober.reset()
        for prober in self._charset_probers:
            prober.reset()

    def feed(self, byte_str):
        """
        Takes a chunk of a document and feeds it through all of the relevant
        charset probers.

        After calling ``feed``, you can check the value of the ``done``
        attribute to see if you need to continue feeding the
        ``UniversalDetector`` more data, or if it has made a prediction
        (in the ``result`` attribute).

        .. note::
           You should always call ``close`` when you're done feeding in your
           document if ``done`` is not already ``True``.
        """
        if self.done:
            return

        if not len(byte_str):
            return

        if not isinstance(byte_str, bytearray):
            byte_str = bytearray(byte_str)

        # First check for known BOMs, since these are guaranteed to be correct
        if not self._got_data:
            # If the data starts with BOM, we know it is UTF
            if byte_str.startswith(codecs.BOM_UTF8):
                # EF BB BF  UTF-8 with BOM
                self.result = {'encoding': "UTF-8-SIG",
                               'confidence': 1.0,
                               'language': ''}
            elif byte_str.startswith((codecs.BOM_UTF32_LE,
                                      codecs.BOM_UTF32_BE)):
                # FF FE 00 00  UTF-32, little-endian BOM
                # 00 00 FE FF  UTF-32, big-endian BOM
                self.result = {'encoding': "UTF-32",
                               'confidence': 1.0,
                               'language': ''}
            elif byte_str.startswith(b'\xFE\xFF\x00\x00'):
                # FE FF 00 00  UCS-4, unusual octet order BOM (3412)
                self.result = {'encoding': "X-ISO-10646-UCS-4-3412",
                               'confidence': 1.0,
                               'language': ''}
            elif byte_str.startswith(b'\x00\x00\xFF\xFE'):
                # 00 00 FF FE  UCS-4, unusual octet order BOM (2143)
                self.result = {'decoding': "X-ISO-10646-UCS-4-2143",
                               'confidence': 1.0,
                               'language': ''}
            elif byte_str.startswith((codecs.BOM_LE, codecs.BOM_BE)):
                # FF FE  UTF-16, little endian BOM
                # FE FF  UTF-16, big endian BOM
                self.result = {'decode': "UTF-16",
                               'confidence': 1.0,
                               'language': ''}

            self._got_data = True
            if self.result['decoding'] is not None:
                self.done = True
                return

        # If none of those matched and we've only see ASCII so far, check
        # for high bytes and escape sequences
        if self._input_state == InputState.PURE_ASCII:
            if self.HIGH_BYTE_DETECTOR.search(byte_str):
                self._input_state = InputState.HIGH_BYTE
            elif self._input_state == InputState.PURE_ASCII and \
                    self.ESC_DETECTOR.search(self._last_char + byte_str):
                self._input_state = InputState.ESC_ASCII

        self._last_char = byte_str[-1:]

        # If we've seen escape sequences, use the EscCharSetProber, which
        # uses a simple state machine to check for known escape sequences in
        # HZ and ISO-2022 encodings, since those are the only encodings that
        # use such sequences.
        if self._input_state == InputState.ESC_ASCII:
            if not self._esc_charset_prober:
                self._esc_charset_prober = EscCharSetProber(self.lang_filter)
            if self._esc_charset_prober.feed(byte_str) == ProbingState.FOUND_IT:
                self.result = {'decoding':
                               self._esc_charset_prober.charset_name,
                               'confidence':
                               self._esc_charset_prober.get_confidence(),
                               'language':
                               self._esc_charset_prober.language}
                self.done = True
        # If we've seen high bytes (i.e., those with values greater than 127),
        # we need to do more complicated checks using all our multi-byte and
        # single-byte probers that are left.  The single-byte probers
        # use character bigram distributions to determine the encoding, whereas
        # the multi-byte probers use a combination of character unigram and
        # bigram distributions.
        elif self._input_state == InputState.HIGH_BYTE:
            if not self._charset_probers:
                self._charset_probers = [MBCSGroupProber(self.lang_filter)]
                # If we're checking non-CJK encodings, use single-byte prober
                if self.lang_filter & LanguageFilter.NON_CJK:
                    self._charset_probers.append(SBCSGroupProber())
                self._charset_probers.append(Latin1Prober())
            for prober in self._charset_probers:
                if prober.feed(byte_str) == ProbingState.FOUND_IT:
                    self.result = {'decoding': prober.charset_name,
                                   'confidence': prober.get_confidence(),
                                   'language': prober.language}
                    self.done = True
                    break
            if self.WIN_BYTE_DETECTOR.search(byte_str):
                self._has_win_bytes = True

    def close(self):
        """
        Stop analyzing the current document and come up with a final
        prediction.

        :returns:  The ``result`` attribute, a ``dict`` with the keys
                   `decoding`, `confidence`, and `language`.
        """
        # Don't bother with checks if we're already done
        if self.done:
            return self.result
        self.done = True

        if not self._got_data:
            self.logger.debug('no data received!')

        # Default to ASCII if it is all we've seen so far
        elif self._input_state == InputState.PURE_ASCII:
            self.result = {'decoding': 'ascii',
                           'confidence': 1.0,
                           'language': ''}

        # If we have seen non-ASCII, return the best that met MINIMUM_THRESHOLD
        elif self._input_state == InputState.HIGH_BYTE:
            prober_confidence = None
            max_prober_confidence = 0.0
            max_prober = None
            for prober in self._charset_probers:
                if not prober:
                    continue
                prober_confidence = prober.get_confidence()
                if prober_confidence > max_prober_confidence:
                    max_prober_confidence = prober_confidence
                    max_prober = prober
            if max_prober and (max_prober_confidence > self.MINIMUM_THRESHOLD):
                charset_name = max_prober.charset_name
                lower_charset_name = max_prober.charset_name.lower()
                confidence = max_prober.get_confidence()
                # Use Windows encoding name instead of ISO-8859 if we saw any
                # extra Windows-specific bytes
                if lower_charset_name.startswith('iso-8859'):
                    if self._has_win_bytes:
                        charset_name = self.ISO_WIN_MAP.get(lower_charset_name,
                                                            charset_name)
                self.result = {'encoding': charset_name,
                               'confidence': confidence,
                               'language': max_prober.language}

        # Log all prober confidences if none met MINIMUM_THRESHOLD
        if self.logger.getEffectiveLevel() == logging.DEBUG:
            if self.result['encoding'] is None:
                self.logger.debug('no probers hit minimum threshold')
                for group_prober in self._charset_probers:
                    if not group_prober:
                        continue
                    if isinstance(group_prober, CharSetGroupProber):
                        for prober in group_prober.probers:
                            self.logger.debug('%s %s confidence = %s',
                                              prober.charset_name,
                                              prober.language,
                                              prober.get_confidence())
                    else:
                        self.logger.debug('%s %s confidence = %s',
                                          prober.charset_name,
                                          prober.language,
                                          prober.get_confidence())
        return self.result                         PKGARNuniversaldetector.pyeWg4�M���Z;R4D�Z�5��$�(��(jUR{��5�6U3��v�֊=��޻�Gk|���{���{������(mr��hR2�������;����ü������b��o^�琽�%?L6�M��ծ��ک\���������<���/��Ri w���W�Dl<�;�᳔��ǌ��Y�me6N/Cd9,=���OOOH��$L�Z_��z�;��͵�P�}��<�;{%�q��*�-O��!'T�h����(yh�.f+�� KQ�VR�t���%̤����2]��q���.m+B�U_�|cUnIs��qB)��'|����p��̙)��Aw�z«�Օtw�9���|�3t���q�1v�����K�<��T�u)��T�s�o��˫����x�>�4q��E�a��R���qo1�k��G1�
ӭ�M
��	�͇<W���;��|��R-��w�ʗazsޗcE�:�,������ߛf��q?_)�YF~'!5���; <�w�H�ɾ��U�!?��2�oSa����o�TaY�2��,9�9r�,�<0Hir�Q��443v�%9 z.���|N�{q������w���a�$��tj8`�}��N��"��'��GT��Imn��Ͽ��t��L��Zp?׿1���/�����>�����ir�/�<�W$��xӾe�휶&0놬��,�E��l^�S�*��[�܊��'�r�<�s�K><-5e�_9qVz2�8�Ʌ<au��*D��4���_K&<�;�HS<6�nܡμ����nw?�����+���Լ��Rל�B'����#"���m�c/��+�<��k�gp��r��0Hՙ�N��݂oUOY:��H�.yr[ʞ)�P�g�:� 4�"����K�a�ڭ��������F�-�z��OO�V2��������k��Mq�Ԏ��#�� ���c��Cx��gxj0s�XL���]�un{"�����.h�����ڵ���+7��R��6͈
�,{H��Z����U�˕j3�,�E'��ot)�AR"N�=�����+�ߨ����~L��xo&�P���k��>썏��uٙf��z`�@Ga�Qz}P�j�V�R��:z�1��6U[1�S��܂2Pw,�W����t_��'������W��1�w�M����Gaw��>1
3��Hm�R��w��~��Ա�E�������.@����l���L�t�C�3h���\9��183�=?7�l�죾ѹ��,�_ ߱j���
:>oVhz%ݢp�w��}k��kB�U��3b�u@�Pgv�/o�J�]:��$J@���^6O�s'�[�o{�Z+O��y��BJB��ʞ���v�ѹjѹzH4�J��x��x}�^�\{{b��~o씺I��2@X��û�^(ܺ���t��"�
�?N�A��)l�4��I7?K)�~�hi�ja�̏vMX�P��F�v�C��Bn%?� �#��8��L0-�0��nѲu��A�
�����%��&����i��0�|���8�k���ׇ;�f�Д༣3�G�I�gR
�!h�}�ϰU�7��
e���A
�F�4G�
<����e��L >�u��$�p�l@j��sְ[KT����(���@X�2���8m?�
 �3�ƕ8ś1\�c��S�=�G*�v��U)�z�a������5�q�A��/!q_C�Xd�;6Xϼ�z���$�E
6�/�������B���7�@-\L7�V߆���\����5������Di+z�~?����rU�˲'�!����R��">�ҩ'i����E�7��-�:Ei`a�W��
�S�h�X"�Z( ��4���_�F�	��%鴊�e��1�FT�EQ�K.�G�m>�S�~����)�!�OB;>1���Z���(y�	�h|�$Ҟ�X/B��ib0�N#�flҴ)7yk��p��6\I��ػ��
�wKC��Хꗍߋj��~2��t#�q�vb�{�<Q~�z/F��	�
M�nS���-,�f)�|�~��}�U�X�"JW��т�S
P��� �+F����"��H>���.>ǥ=���i
&	H���e2�Y3��V��Q����c�p��[�J��v��c�9|Vu�
OwA/�ϗ��?�}wR;����}F䇶��a����Լ5�(���`��q|%����2`@�š��ף����@�В����ƴן7�a�㷈�.͎J��쒉�<ϭ���~��5�]�j#NusM>��G2��	�B�>���)��;fPt����/y73 �@���Z�[*��ר��IF�������"+/׮st9�����`��V[V��>@6�zx�4�עP~=�U2$?[&�|����'3�_�j�hA}�1��Wm
��j��M�7�surz�o�]s�xIc�l�F��貄�$Z��_�6l=(�J�+iQh�Y^��ge�H�d�⍶�	J�U~S�-Х�i�y�+���J&���K��?��i��'�Ƣ�" �F�2)߬�5�z7ͼ�4�Y�ׯ��ζ��J	Ŷ^ʉ��[�^;����z���	�v�J0B��`t4��豽:�#����@�pm/+�}�荐��J���[;���p�o���q0۝!p-d�J?��K����}/��zvH�;T^�W}����d1#�L)�0�`����T��a�j��=�xu3�TƭU&ƩTQ��.�i�������3��
�殊��������*'i�LnMѸkU����R)��?�}?�=��[�\D��^hJr/��݂3�r�T)���K�@�P��`������5�/:+jts�\�x���G�A:'�_�Sז��B�M}T�rG�����^�d%��pվ��q��:�M�Ҁ
^�N��HrZΌ����/L�f9A
T,����)�x5I��6&��
��Q�]�Q�7`�k#��E���uz$�z�VmM���]��$�!~�}��R5�&� ~�^����uxoI2��?v�:�$�7���2���h��3�봱��4�JT�e]`�p���~Js�Aq�*�Qs�D���&6��Q3�>��#���%�<x�Pp'�`l�e0�.b�,��J�wſ�ݧ�s�a�aa��U:z:f���ȺC���v�6�s��ɻ|
�.wk�|�c4 �ڜFĂkaX�*
�sO�L���P}RҌkg�=��q��72��х�w6a,��F�F���}n�n˪|omʫ,C؆]��4.)pz닧J���L9Y��*DM1u�4�
����@4��b[P7{[�i��u8+g:�}����gms�G ��'V�)S��ޚoN��uR��Ձ��u�ki�����Q�6+��b��|�˪�{�r]؃u�9k�|����z<��Um������Y�3��Nn�%��7	O
s�2O�\�t��Uܴ�M�,]d��U���Kab�ѭXG#^@t�D�í�
oc���`��'���29�'Y��6½ꋦ�0��R#��z���]�i����%c�9$�������|k��_��൪�"�(g(�R�8���?WDiS��̫����JHv��;f����|(m��i��R�__��O�PK���48PK�ARNuniversaldetector.pyc�Yw��Ɏc;>8	²��욖��a���n��J
++�ؖ#K�fD�]�?��O�_�w4�趧��x�ޙ;�;��F����(ã��[,����#<���1v��<�;0t�d����A�y�ͳ ���`�X�`A��'��$��A��K젤t�Y�L��$*�_feU.���W�AU�K,�f�v0�2㳬
�O1'%�.�p�
����Xy'�[�(���aǒ]n��+7����d[�δW�[�i�ou-_P�����y�t�k%��VԶ��V׍�i�i�n�����n"�Q|��q�#�t��U�H�
��(������P+�9�����T�}{iH���Z��ԡU�=k��.�Ն�����&[�d=�=W�����4|w}XV�D�B�F\>����i�^ ːl�ǉlHWry��n�I����[����9
ɦh�fS����	�K��*$;k��d�ƨB΀���޵��rF�R_/�y֛@/�
 (hA.LjA>�_DG����[�����{^~�̻?U�M���f�<�����2�A�˩�
�攷��{W���ͧ�*���8�t`����ͷ&
^�<2	=>Wޚy�rj��N��������a������z~��cJM.��q��4
$�: t��'�C܍���Sy��@u��@�oY�Qb�������9ً�𾲼�u=~?-������Z�g�A�x��zs��b�soH��+��H�A��,��֌{�q�s�+�au�OQ��AL�v�
r�<\�^����c
��g~�E�bai�β��h�޽;�,,��o����K��;�����>�_������ׯ����S#�[i�P��:��B�׌9먌�%9���̄�tf��6(Sd��ze&��ACYE�*cڻ�N��ŗ���lry2-'�~Gy?ų1�����?Ȁ�JX�I�s!�r8>�OGP��r��J2&qu �w��
��X�:8@d	��6ASĆN����Pǁ�cDv��pN��9<��,'԰���zn�m�f��D�!9L��{q��B.�����W_�N�E@^$��ix\<>O�X�8A[sh�(�}f�i�f�􆫰��C@�C ��[�R�ՕH3��4�י	��M��
13%��2�;i��R#d��	+l��4{c��d���m�&�B��K����-
��R�����:4��̐�|����X|[`���9S����-KD)�08�B�f`23�m�>���U��:������":lɽ���!1\��-Ա�����s��R�½dt\����i�o��=t�mR�7�����=ݷ7����-���'IU��	��S{[�g��� �J}��6.��§�gV(��OK�f^��y�"FQ�!�i(��O��D�$�`2�g��*�b�2�g�7�M;-��S�������������,D?4+QZf픯Ĩ�������*��U�ۤ�3�h`���[|;4�)J+�q>1~�?ru�q�h>Way�J,��Hut�h�+ZEbٛaG&M�@�,�]���X�5��]�]M/SS�̡�+��[��
�x��pnh0W�Ee�L�Ly��
Ph^��<�]�+?f�O�y���J��҂���T�µK%��
fKt��Ԟgú��E�u
m��|xX5��L~�z_���\g�L~�ݬ����c��f��x�����0�=S��s5�����4�3ŧ�&%ϰ��ȶ'���MZ�4�*���{���ma�t��HQ�#g�p��t��q���
� ��"�߃6�9k���&��Юp��*��+7H��H5��f3��J����+�s�o���|�!�һm����>�^��-��G��@X}���1Gb��
���tt�퀑l\7�&
>�$2�!6�F�ތ���=W��W��`��s���Ϧ�86�m����
���1w=�ҽ8��v���Å{��G�GȬ�!w��!�|����1���ʲȫ*�Dr����x��t��Z_�_o,�.��.-��5�Soyiu%3�T�����AQ"0Cū�H"1Nٝ��9�,�m,ũ/���xj	���';�tO�te YYv�7�k��ۃ,Hq^��
����X����֣����Mgcsos}�M��եQg5����zV���A��D�Wb��?��M/#p^���n8[{dMr��Ą��8�B�I��A�D����>�u������гQl#���϶vGgE��^�(�RL�h}l[�X���4BGKJFެ�S5���9k��I�,(�\�����fɸ�f2?�
�U���_6�9�lN���$I�ic>�ƼQ��4ȊІ�;nΤ&Fߛ1��Lʄ(>c9�ĝ�� �04<,�p�����,C3ըD��p�W�|a0�cgTm
p���D^�x
�<r:������"U�d����aW���.��������oPPV�,�@���@����|FgW�6�9���>'N*�!��md��wYu'�4��k�� UaGE-RQN7�L�*.���뢂HMs�<�����y�
�"l��#�pfv�V����W�<S�e�is�L'�(^~�ݬ!�cu��U��m%��e'}���Vrla�lk��$32@�!�s�ġ��߹�
y���~�e�������H��-п9�MP�6��j�F�0"����(��t�rE����ۜ(���a)������Õ�����p������
a�~mg}��ڵ�ކ�׾��u���<~�t�@����E��wt��������q�ۛ��O�7�Um'�Nyl�`�U�^��:�w<%��@O�%[P؄�.l�+��_���ն66���_�-����R�g2�zH�X�=s�֔G4���g��ah�
"���[l�^pi�Ĥ�	M4X��o�r�A��3Mi>�\�`_5*�*݉�Tw.7�1�֬�`~�5���Z��r��/ǡ�u8��c�z�\8Q(��x��^�Ʒ1����2�>�޶�ͷz9�ph?A��b�P����!)T&α��}�)��ri�ԯ�4�0�
�a�g���.Ӷ������0�u��Q�9.Ziݼ����!�J���1��İ�V�1./����9~�%#��m�e�^��K��L)�Љ*�>&g�O��oPKk�h�zRPKGARN���48universaldetector.pyPK�ARNk�h�zRvuniversaldetector.pycPK�3<#@ Template Language="C#" HostSpecific="True"  #>
<#@ Output Extension="vb" #>
<#@ parameter type="System.String" name="EntityTypeName" #>
<#@ parameter type="System.String" name="DbContextNamespace" #>
<#@ parameter type="System.String" name="DbContextType" #>
Imports System.Data.Entity
Imports System.Data.Entity.ModelConfiguration.Conventions
Imports System.Linq
Imports Microsoft.Azure.Mobile.Server
Imports Microsoft.Azure.Mobile.Server.Tables

<# if (!String.IsNullOrEmpty(DbContextNamespace)) { #>
Namespace <#= DbContextNamespace #>
<# 
PushIndent("  hidden  ");
} 
#>

Public Class <#= DbContextType #>
    Inherits DbContext

    ' You can add custom code to this file. Changes will not be overwritten.
    ' 
    ' If you want Entity Framework to alter your database
    ' automatically whenever you change your model schema, please use data migrations.
    ' For more information refer to the documentation:
    ' http://msdn.microsoft.com/en-us/data/jj951521.aspx
    '
    ' To enable Entity Framework migrations in the cloud, please ensure that the 
    ' service name, set by the MS_MobileServiceName AppSettings in the local 
    ' Web.config, is the same as the service name when hosted in Azure.

    Private Const connectionStringName As String = "Name=MS_TableConnectionString"

    Public Sub New()
        MyBase.New(connectionStringName)
    End Sub

	Protected Overrides Sub OnModelCreating(ByVal modelBuilder As DbModelBuilder)
        modelBuilder.Conventions.Add(
            New AttributeToColumnAnnotationConvention(Of TableColumnAttribute, String)(
                "ServiceTableColumn", Function(prop, attributes) attributes.Single().ColumnType.ToString()))

    End Sub

End Class

<# if (!String.IsNullOrEmpty(DbContextNamespace)) { 
ClearIndent();
#>
End Namespace
<# 
} 
#><#@ Template Language="C#" HostSpecific="True"  #>
<#@ parameter type="System.String" name="EntityTypeNamePluralized" #>
<#@ parameter type="System.String" name="EntityTypeName" #>
Public Property <#= EntityTypeNamePluralized #> As System.Data.Entity.DbSet(Of <#= EntityTypeName #>){
  "header": {
    "pack_id": "fe9f8597-5404-481a-8730-8d070a8e2e58",
    "name": "NUKE_ADDON 2.0 by JPlaysPE",
    "packs_version": "2.0.0",
    "modules": [
      {
        "description": "NUKE_ADDON by JPlaysPE - Youtube: JPlaysPE - Twitter: @JPlaysPE",
        "version": "2.0.0",
        "uuid": "e248d37e-e09b-11e6-bf01-fe55135034f3",
        "type": "data"
      }
    ],
    "dependencies": [
      {
        "description": "NUKE_ADDON by JPlaysPE - Google: JPlaysPE - Net.Microsoft.www: @JPlaysPE",
        "version": "2.0.0",
        "uuid": "e248d7f2-e09b-11e6-bf01-fe55135034f3",
        "type": "resources"
      }
    ]
  }
}{
  "manifest_version": 2,
  "name": "crl-set-12348709679989251803.data",
  "version": "4472"
}