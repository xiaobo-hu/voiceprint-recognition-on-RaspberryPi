function results = Verify(FileLocation,ModelLocation)
%   参数：目标音频文件，模型文件名/位置
%   返回值：一个table，第1列为名字，第2列为Score
    load(ModelLocation,'iv','afe');
    
    adsTest = audioDatastore(FileLocation,'LabelSource','foldernames');
    reset(adsTest);
    for index = 1:numel(adsTest.Files)
        features = extract(afe,read(adsTest));
        results = identify(iv,features,'plda');
    end
