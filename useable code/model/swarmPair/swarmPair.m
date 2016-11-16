function Pair = swarmPair(OPCell,parameters)
% TODO-Comment




pair = [];
for i = 1 : parameters.numFish-1
    for j = i+1 : parameters.numFish
        temp = [OPCell{i} OPCell{j}];
        pair = [pair ; temp];
    end
end

len = size(OPCell{1},1);
C = num2cell(pair,2);
stateCell = cellfun(@getStateDataPair,C,'UniformOutput',0);
stateData = cell2mat(stateCell);


idx = 1;
for i = 1 : parameters.numFish-1
    for j = i+1 : parameters.numFish 
        Pair{idx} = stateData(len*(idx-1)+1:len*(idx),:) ;
        idx = idx + 1;
    end
end


