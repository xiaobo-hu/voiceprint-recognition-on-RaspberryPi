function results = Verify(FileLocation,ModelLocation)
%   参数：目标音频文件，模型文件名/位置
%   返回值：一个table，第1列为名字，第2列为Score
    clear;
    load(ModelLocation,iv);
    [adsTest,fs]= audioread(FileLocation);
%   mfcc提取
    afe = audioFeatureExtractor('gtcc',true,'gtccDelta',true,'gtccDeltaDelta',true,'pitch',true,'SampleRate',fs);
    afe.Window = hann(round(0.05*fs),'periodic');
    afe.OverlapLength = round(0.045*fs);
    features = extract(afe,read(adsTest));
%   验证，输出
    results = identify(iv,features,'plda');
