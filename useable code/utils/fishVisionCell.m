function VisionCell = fishVisionCell(OPCell,parameters)

	VisionCell = cell(1, parameters.numFish);

    for i=1 : length(VisionCell)
        VisionCell{i} = zeros(1,4*(parameters.numFish-1)+5);
    end

% disp(4*(parameters.numFish-1)+5);
	for i=1 : length(OPCell{1,1})
		%fishSwarm store the position and orientation of all fish at line i 
		fishSwarm = zeros(parameters.numFish,3);
		for k=1:parameters.numFish
            fishSwarm(k,:) = OPCell{1,k}(i,:);
        end
		for j=1 : parameters.numFish
			VisionCell{1,j}(i,:) = fishVision(fishSwarm, j, parameters);
        end
     
	end