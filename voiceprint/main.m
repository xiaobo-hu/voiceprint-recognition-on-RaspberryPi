% Train('./SpeakerVerificationLock/CNC2/*/*.wav','./model/BaseModel.mat')
% move file
Enroll('./SpeakerVerificationLock/Enroll/*/*.wav','./SpeakerVerificationLock/Det/','./model/BaseModel.mat','./model/CheckPoint.mat','./model/errThreshold.mat')
Verify('./SpeakerVerificationLock/Test/authenticate_audio.wav','./model/CheckPoint.mat','./model/errThreshold.mat','fbc')