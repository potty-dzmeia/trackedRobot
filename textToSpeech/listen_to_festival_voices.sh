#!/bin/bash

cfg_file="/$USER/.festivalrc"


echo "(set! voice_default 'voice_nitech_us_awb_arctic_hts)" >  $cfg_file
(echo "Festival offers a general framework for building speech synthesis systems as well as including examples of various modules. ") | festival --tts


echo "(set! voice_default 'voice_nitech_us_bdl_arctic_hts)" >  $cfg_file
(echo "Festival offers a general framework for building speech synthesis systems as well as including examples of various modules. ") | festival --tts

echo "(set! voice_default 'voice_nitech_us_clb_arctic_hts)" >  $cfg_file
(echo "Festival offers a general framework for building speech synthesis systems as well as including examples of various modules. ") | festival --tts

echo "(set! voice_default 'voice_nitech_us_jmk_arctic_hts)" >  $cfg_file
(echo "Festival offers a general framework for building speech synthesis systems as well as including examples of various modules. ") | festival --tts

echo "(set! voice_default 'voice_nitech_us_rms_arctic_hts)" >  $cfg_file
(echo "Festival offers a general framework for building speech synthesis systems as well as including examples of various modules. ") | festival --tts

echo "(set! voice_default 'voice_nitech_us_slt_arctic_hts)" >  $cfg_file
(echo "Festival offers a general framework for building speech synthesis systems as well as including examples of various modules. ") | festival --tts


















