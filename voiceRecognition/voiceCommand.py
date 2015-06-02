#!/usr/bin/env python2
import pocketsphinx as ps
import sys
import pyaudio
import os


hmm = '/usr/local/share/pocketsphinx/model/en-us/en-us/'
dic = '/home/chavdar/Development/projects/sphinx/my_dict/8846.dic' #'/usr/local/share/pocketsphinx/model/en-us/cmudict-en-us.dict'
lm=   '/home/chavdar/Development/projects/sphinx/my_dict/8846.lm'  #'/usr/local/share/pocketsphinx/model/en-us/en-us.lm.dmp'



BUFFER_SIZE = 8192 # pyaudio frame_buffer size



def voiceCommand() :


    config = ps.Decoder.default_config()
    config.set_string('-hmm', hmm)
    config.set_string('-lm', lm)
    config.set_string('-dict', dic)
    #config.set_string('-samprate', '8000')
    config.set_string('-logfn', '/dev/null')
    decoder = ps.Decoder(config)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=BUFFER_SIZE)
    stream.start_stream()


    decoder.start_utt()

    bSpeechInLastBuffer = False
    while True:

        buf = ""

        # Collet 1024 or more bytes
        while(1):
            buf += stream.read(stream.get_read_available())
            if len(buf) >= 1024:
                break


        #print("passing - " + str(len(buf)))
        decoder.process_raw(buf, False, False)
        # try:
        #     if  decoder.hyp().hypstr != '':
        #         print 'Partial decoding result:', decoder.hyp().hypstr
        # except AttributeError:
        #     pass


        # Checks if buf contained speech
        # if decoder.get_in_speech():
        #     sys.stdout.write('.')
        #     sys.stdout.flush()


        # Print the final result only if we go from speech to silence
        # if decoder.get_in_speech() != bSpeechInLastBuffer:
        #     bSpeechInLastBuffer = decoder.get_in_speech()
        #     if (not bSpeechInLastBuffer):
        #         decoder.end_utt()
        #         stream.stop_stream()
        #
        #         try:
        #             if  decoder.hyp().hypstr != '':
        #                 return decoder.hyp().hypstr   #<----
        #             else :
        #                 return 'none'
        #         except AttributeError:
        #             return "error"
        #             pass
        #
        #         stream.close()

    return "error"





if __name__ == '__main__':
    voiceCommand()


