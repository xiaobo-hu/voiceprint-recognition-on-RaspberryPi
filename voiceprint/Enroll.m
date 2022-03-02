function Enroll(Location,FileExtension,TargetFile)
%   函数参数：文件路径,文件格式(.wav/.mp3/.m4a/...)，保存模型名，采样率 = 48000
    clear;
    addParameter(inputParser,'fs',48000);
    load('BaseModel.mat',iv);%读取
    %读取Location，包括子文件夹下所有FileExtension格式的音频
    adsEnroll = audioDatastore(Location,'LabelSource','foldernames','FileExtensions',FileExtension,'IncludeSubfolders',true);
    enrollLabels = adsEnroll.Labels;
%   提取mfcc
    afe = audioFeatureExtractor('gtcc',true,'gtccDelta',true,'gtccDeltaDelta',true,'pitch',true,'SampleRate',fs);
    afe.Window = hann(round(0.05*fs),'periodic');
    afe.OverlapLength = round(0.045*fs);
    adsEnroll = transform(adsEnroll,@(x)extract(afe,x));
%   训练保存
    enroll(iv,adsEnroll,enrollLabels);
    save(TargetFile,iv)
return
