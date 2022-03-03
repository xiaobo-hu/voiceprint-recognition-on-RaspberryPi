function Train(FileLocation, SaveModelLocation)
%   函数参数：文件路径，模型保存路径
    fs = 16000;
    
    %读取Location，包括子文件夹下所有FileExtension格式的音频
    adsTrain = audioDatastore(FileLocation,'FileExtensions','.wav','LabelSource','foldernames');
    trainLabels = adsTrain.Labels;
%   mfcc提取
    afe = audioFeatureExtractor('gtcc',true,'gtccDelta',true,'gtccDeltaDelta',true,'pitch',true,'SampleRate',fs);
    afe.Window = hann(round(0.05*fs),'periodic');
    afe.OverlapLength = round(0.045*fs);
    adsTrain = transform(adsTrain,@(x)extract(afe,x));
%   训练ivector系统，保存    
    iv = ivectorSystem('SampleRate',fs,'InputType','features');
    trainExtractor(iv,adsTrain,'UBMNumComponents',64, 'UBMNumIterations',5,'TVSRank',32,'TVSNumIterations',5);
    trainClassifier(iv,adsTrain,trainLabels, 'NumEigenvectors',16, "PLDANumDimensions",16, "PLDANumIterations",5);
    save(SaveModelLocation,'iv', 'afe');

return
