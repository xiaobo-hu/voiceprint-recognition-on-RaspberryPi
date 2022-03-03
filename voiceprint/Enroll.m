function Enroll(FileLocation,BaseModelLocation,SaveModelLocation)
%   函数参数：文件路径，读取模型路径，保存模型路径
    fs = 48000;
    load(BaseModelLocation,'iv');%读取
    
    %读取Location，包括子文件夹下所有FileExtension格式的音频
    adsEnroll = audioDatastore(FileLocation,'LabelSource','foldernames');
    enrollLabels = adsEnroll.Labels;
%   提取mfcc
    afe = audioFeatureExtractor('gtcc',true,'gtccDelta',true,'gtccDeltaDelta',true,'pitch',true,'SampleRate',fs);
    afe.Window = hann(round(0.05*fs),'periodic');
    afe.OverlapLength = round(0.045*fs);
    adsEnroll = transform(adsEnroll,@(x)extract(afe,x));
%   训练保存
    enroll(iv,adsEnroll,enrollLabels);
    save(SaveModelLocation,'iv','afe');
return
