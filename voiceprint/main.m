Train('./SpeakerVerificationLock/CNC2/*/*.wav','./model/BaseModel.mat')
% move file
Enroll('./SpeakerVerificationLock/Enroll/*/*.wav','./model/BaseModel.mat','./model/CheckPoint.mat')
Verify('./SpeakerVerificationLock/Test/*.wav','./model/CheckPoint.mat')