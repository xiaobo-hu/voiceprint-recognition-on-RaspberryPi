function [result,score] = Verify(FileLocation,ModelLocation,ThresholdLocation,SpeakerID)
%   参数：目标音频文件，模型文件名/位置，Det保存位置，识别对象ID
%   返回值：result(true/false)，score得分
    % clear;
    load(ModelLocation,'iv');
    load(ThresholdLocation,'eerThreshold')
    [adsTest,fs]= audioread(FileLocation);
%   mfcc提取
    afe = audioFeatureExtractor('gtcc',true,'gtccDelta',true,'gtccDeltaDelta',true,'pitch',true,'SampleRate',fs);
    afe.Window = hann(round(0.05*fs),'periodic');
    afe.OverlapLength = round(0.045*fs);
    features = extract(afe,adsTest);
%   验证，输出
    [result,score] = verify(iv,features,SpeakerID,'css',eerThreshold.CSS);