function OPCell = getOP(DATACELL, parameters)
% TODO-Comment

startAt = find(~cellfun('isempty',DATACELL),1);

OPCell = cell(1, parameters.numFish);
%OPCell(:) = {zeros(length(DATACELL),2)};

m = length(DATACELL);
for i=1 : parameters.numFish
    OPCell{i} = zeros(m,3);
end



reachFirstWholeRow = false;
for idx = startAt : length(DATACELL)
	if (parameters.igoreDisCont)
    	if isempty(DATACELL{idx}) || size(DATACELL{idx},2) < parameters.numFish
        	continue;
    	end
    else
    	if (isempty(DATACELL{idx}) || size(DATACELL{idx},2) < parameters.numFish)
            if(~reachFirstWholeRow)
                continue;
            else
                error('error at DataHandler/getPositionCell.m : fish data is discontinuous at line %d',idx);
            end
    	end
    end
    reachFirstWholeRow = true;





    % P = DATACELL{idx}(1:4,:);
    P = DATACELL{idx}(1:4,:);
    P(4,:) = deg2rad(P(4,:));
    P = sortOrderID(P);
    P = P(2:4,:);



    for i=1 : parameters.numFish
    	OPCell{i}(idx,:) = P(:,i).';
    end

end
