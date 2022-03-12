function Enroll(EnrollFileLocaiton,DetFileLocation,BaseModelLocation,SaveEnrollModelLocation,SaveThresholdLocaiton)
%   函数参数：文件路径Enroll,Det,读取模型路径,保存模型路径Enroll,Det
    fs = 16000;
    load(BaseModelLocation,'iv');%读取
    %读取Location，包括子文件夹下所有FileExtension格式的音频
    adsEnroll = audioDatastore(EnrollFileLocaiton,'LabelSource','foldernames');
    adsDet = audioDatastore(DetFileLocation,'LabelSource','foldernames','FileExtensions','.wav','IncludeSubfolders',true);
    enrollLabels = adsEnroll.Labels;
    detLabels = adsDet.Labels;
%   提取mfcc
    afe = audioFeatureExtractor('gtcc',true,'gtccDelta',true,'gtccDeltaDelta',true,'pitch',true,'SampleRate',fs);
    afe.Window = hann(round(0.05*fs),'periodic');
    afe.OverlapLength = round(0.045*fs);
    adsEnroll = transform(adsEnroll,@(x)extract(afe,x));
    adsDet = transform(adsDet,@(x)extract(afe,x));
%   训练保存
    enroll(iv,adsEnroll,enrollLabels);
    [results, eerThreshold] = detectionErrorTradeoff(iv,adsDet,detLabels);
    save(SaveEnrollModelLocation,'iv','afe');
    save(SaveThresholdLocaiton,'eerThreshold');
return
