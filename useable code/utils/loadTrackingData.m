function [DATACELL,frameRecorder] = loadTrackingData(filename, parameters)

    try
        data = dlmread(filename);
    catch
        error('Please change the decimal point in the tracking data from "," to ".". Make sure you have set the right fish number in "parameters" variable. Please delete the incomplete lines in the tracking data')
    end
    
%     data = dlmread(filename);
    
	frameRecorder = zeros(length(data),1);
	DATACELL = cell(1,length(data)-1);


	for i=1 : length(data)-1
		frameRecorder(i) = data(i,1);
		M = reshape(data(i,3:end-1),[5,parameters.numFish]);
		DATACELL{i} = M;
	end

