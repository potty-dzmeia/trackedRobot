#!/usr/bin/env python2
import pocketsphinx as ps
import pyaudio
import beep as b
import sys
import time

hmm = '/usr/local/share/pocketsphinx/model/en-us/en-us/' # '/root/development/sphinx/cmusphinx-en-us-ptm-8khz-5.2'   #'
dic = '/root/development/sphinx/sphinx_knowledge_base/2472.dic' #'/usr/local/share/pocketsphinx/model/en-us/cmudict-en-us.dict'
lm=   '/root/development/sphinx/sphinx_knowledge_base/2472.lm'  #'/usr/local/share/pocketsphinx/model/en-us/en-us.lm.dmp'



BUFFER_SIZE = 2048 # pyaudio frame_buffer size



def voiceCommand() :


    config = ps.Decoder.default_config()
    config.set_string('-hmm', hmm)
    config.set_string('-lm', lm)
    config.set_string('-dict', dic)
    #config.set_string('-samprate', '8000')
    #config.set_string('-logfn', '/dev/null')
    decoder = ps.Decoder(config)
    decoder.start_utt()

    p = pyaudio.PyAudio()

    bSpeechInLastBuffer = False

    b.beep()
    time.sleep(0.3) # add some delay because the beep might introduce interference

    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=BUFFER_SIZE)
    stream.start_stream()
    while True:

        buf = ""

        # Collect 1024 or more bytes
        while(1):
            data = stream.read(stream.get_read_available())
            # print("data read - "+str(len(data)))
            buf += data
            if len(buf) >= 1024:
                break


        # print("passing - " + str(len(buf)))
        decoder.process_raw(buf, True, False)
        # try:
        #     if  decoder.hyp().hypstr != '':
        #         print 'Partial decoding result:', decoder.hyp().hypstr
        # except AttributeError:
        #     pass


        # Checks if buf contained speech
        if decoder.get_in_speech():
            sys.stdout.write('.')
            sys.stdout.flush()


        # Print the final result only if we go from speech to silence
        if decoder.get_in_speech() != bSpeechInLastBuffer:
            bSpeechInLastBuffer = decoder.get_in_speech()
            if (not bSpeechInLastBuffer):
                print("End of speech")
                decoder.end_utt()
                stream.stop_stream()

                try:
                    if  decoder.hyp().hypstr != '':
                        return decoder.hyp().hypstr   #<----
                    else :
                        return 'none'
                except AttributeError:
                    return "error"
                    pass

                stream.close()

    return "error"





if __name__ == '__main__':
    print(voiceCommand())


