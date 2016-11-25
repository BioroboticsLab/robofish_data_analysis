function FishMotion = egoMotion(OPCell,parameters)
% TODO-Comment
% v = velocity per second
% vTurn = turn angle per sceond


    FishMotion = cell(1, parameters.numFish);
    [m,~] = size(OPCell{1});


    for i = 1 : length(OPCell)
        FishMotion{i} = zeros(m-1,2);

        for j = 1 : m-1
            %cm/s
            v=norm(OPCell{i}(j+1,1:2)-OPCell{i}(j,1:2))*parameters.fps;
            %radians/frame
%             vTurn = angleDiff(deg2rad(OPCell{i}(j,3)),deg2rad(OPCell{i}(j+1,3)));
            % vTurn = rad2deg(angleDiff(deg2rad(OPCell{i}(j,3)),deg2rad(OPCell{i}(j+1,3))));
            vTurn = angleDiff(OPCell{i}(j,3),OPCell{i}(j+1,3));
            FishMotion{i}(j,:) = [v,vTurn*parameters.fps];
        end
    end
