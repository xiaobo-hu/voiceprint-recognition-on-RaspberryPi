# import nls
def record_with_pyaudio(filename, record_seconds=10, fs = 16000):
    """filename could be absolute path"""
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

def judge_chinese_num_accuracy(string,arrays):
    digit = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    count = 0
    array_index = 0
    for i in range(len(string)):
        if string[i] in digit.keys() and digit[string[i]] == arrays[array_index]:
            count += 1
            array_index += 1
    print(count)
    if count / 4 > 3 / 4:
        return True
    else:
        return False

import sys, os

sys.path.insert(0, os.pardir)
from nls_package import run

name = os.path.join(os.pardir, "voiceprint//SpeakerVerificationLock//Test//authenticate_audio.wav")
record_with_pyaudio(name, 4,16000)
run.getreply(name)
import time
time.sleep(12)
ans = run.my_message
print("ans", ans)
print("msg:", run.my_message)
result = judge_chinese_num_accuracy(ans,[2,3,4,6])
result = judge_chinese_num_accuracy(run.my_message,[2,3,4,6])


#os.remove(name)

