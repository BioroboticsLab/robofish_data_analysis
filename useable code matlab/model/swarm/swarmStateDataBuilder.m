
function [stateData,idRecord] = swarmStateDataBuilder(DATACELL,parameters)

idRecord = zeros(length(DATACELL),parameters.numFish);
%stateData = zeros(length(DATACELL),);

stateData = [];

for idx = 1 : length(DATACELL)
 %   if isempty(DATACELL{idx}) || size(DATACELL{idx},2) < 7
 %       continue;
 %   end
    
    P = DATACELL{idx}(1:4,:);
    P = sortOrderMinDistance(P);
 %   dlmwrite(strcat('idRecord',outputFile),P(1,:),'delimiter',',','-append');
    idRecord(idx,:) = P(1,:);
    P = P(2:4,:);
    
    % if ignoreID
    %     id_idx = DATACELL{idx}(1,:) == ignoreID;
    %     P(:, id_idx) = [];
    % end
    
    %distance matrix
    DM = distanceMatrix(P(1:2,:));
    DM2 = DM + DM';
      
    %link angle matrix   
    LAM = linkAngleMatrix(P);

    %included angle matrix
    IAM = includedAngleMatrix(P(3,:));


    N = [reshape(DM2.',1,[]) reshape(LAM.',1,[]) reshape(IAM.',1,[])];

    % no distance matrix
%    N = [reshape(LAM.',1,[]) reshape(IAM.',1,[])];
 %   dlmwrite(outputFile,N,'delimiter',',','-append');
    stateData = [stateData;N];
end


