adsTrain = audioDatastore('./SpeakerVerificationLock/CNC2/*/*.wav','FileExtensions','.wav','LabelSource','foldernames');
trainLabels = adsTrain.Labels;
fs = 16000;
afe = audioFeatureExtractor('gtcc',true,'gtccDelta',true,'gtccDeltaDelta',true,'pitch',true,'SampleRate',fs);
afe.Window = hann(round(0.05*fs),'periodic');
afe.OverlapLength = round(0.045*fs);
adsTrain = transform(adsTrain,@(x)extract(afe,x));
iv = ivectorSystem('SampleRate',fs,'InputType','features');
trainExtractor(iv,adsTrain,'UBMNumComponents',64, 'UBMNumIterations',5,'TVSRank',32,'TVSNumIterations',5);
trainClassifier(iv,adsTrain,trainLabels, 'NumEigenvectors',16, "PLDANumDimensions",16, "PLDANumIterations",5);


adsEnroll = audioDatastore('./SpeakerVerificationLock/Enroll/*/*.wav','LabelSource','foldernames');
enrollLabels = adsEnroll.Labels;
fs = 48000;
afe = audioFeatureExtractor('gtcc',true,'gtccDelta',true,'gtccDeltaDelta',true,'pitch',true,'SampleRate',fs);
afe.Window = hann(round(0.05*fs),'periodic');
afe.OverlapLength = round(0.045*fs);
adsEnroll = transform(adsEnroll,@(x)extract(afe,x));
enroll(iv,adsEnroll,enrollLabels);

adsTest = audioDatastore('./SpeakerVerificationLock/Test/*.wav','LabelSource','foldernames');
numCorrect = 0;
reset(adsTest);
for index = 1:numel(adsTest.Files)
    features = extract(afe,read(adsTest));
    results = identify(iv,features,'plda');
    trueLabel = adsTest.Labels(index);
    predictedLabel = results.Label(1);
    isPredictionCorrect = trueLabel==predictedLabel;
    numCorrect = numCorrect + isPredictionCorrect;
end