import matlab.engine
import os

eng = matlab.engine.start_matlab()
print("matlab_engine open")
eng.cd(os.path.join(os.pardir,"voiceprint"))

eng.Train('./SpeakerVerificationLock/CNC2/*/*.wav','./model/BaseModel.mat',nargout=0)

name = os.path.join(os.pardir, "voiceprint//SpeakerVerificationLock//Test//authenticate_audio.wav")

eng.Enroll('./SpeakerVerificationLock/Enroll/*/*.wav','./SpeakerVerificationLock/Det/','./model/BaseModel.mat','./model/CheckPoint.mat','./model/errThreshold.mat',nargout=0)

for ID in os.listdir(os.path.join(os.pardir,"voiceprint//SpeakerVerificationLock//Enroll")):
    print(ID)
    [result,score] = eng.Verify('./SpeakerVerificationLock/Test/authenticate_audio.wav','./model/CheckPoint.mat','./model/errThreshold.mat',ID,nargout = 2)
    print(result, score)

eng.quit()