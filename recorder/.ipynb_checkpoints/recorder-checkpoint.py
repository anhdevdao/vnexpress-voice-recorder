import argparse
import tempfile
import queue
import sys

import soundfile as sf
import sounddevice as sd

q = queue.Queue()

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

def rec(self, filename=None):
    try:
#         if sr is None:
#             device_info = sd.query_devices(None, 'input')
#         # soundfile expects an int, sounddevice provides a float:
#             sr = int(device_info['default_samplerate'])
        if filename is None:
            filename = tempfile.mktemp(prefix='cau_',
                                            suffix='.wav', dir='')

        # Make sure the file is opened before recording anything:
        with sf.SoundFile(filename, mode='x', samplerate=48000,
                            channels=1, subtype=None) as file:
            with sd.InputStream(samplerate=48000, device=None,
                                channels=1, callback=callback):
                print('#' * 80)
                print('press Ctrl+C to stop the recording')
                print('#' * 80)
                while True:
                    file.write(q.get())
    except KeyboardInterrupt:
        print('\nRecording finished: ' + repr(filename))
    except Exception as e:
        print(type(e).__name__ + ': ' + str(e))
        