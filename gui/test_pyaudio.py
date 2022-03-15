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

if __name__ == '__main__':
    import os,time
    name = input("input the user name: ")
    my_path = os.path.join(os.getcwd(),name)
    if not os.path.exists(my_path):
        os.makedirs(my_path)
    for i in range(3):
        print('the ', i+1,' time will begin after 2s')
        time.sleep(2)
        record_with_pyaudio(my_path+'//'+name+'_record'+str(i+1)+'.wav')
        print('the ', i+1,' time record ends')
