file = '../Data/cDataWithoutRobo.mat';
addpath(genpath('../egoMotion/'));
addpath(genpath('../OPsmoothing'));
addpath(genpath('../'))

parameters = [];
parameters.timeSlot = 25;
parameters.fps = 1;
parameters = setRunParameters(parameters);

load(file);
OPCell = getOP(cDATACELL,parameters);

smooth = {'wavelet';'sgolay'};

WOP = waveletSmooth(OPCell,'db5');
SOP = OPSmooth(OPCell);

WOP = genAngle(WOP);
SOP = genAngle(SOP);

save('../output/SOP.mat','SOP');
save('../output/WOP.mat','WOP');