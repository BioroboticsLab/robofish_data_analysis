function S = OPSmooth(OPCell)
    
   S = OPCell;
   for i=1 : length(OPCell)

       S{i}(:,1:2) = sgolayfilt(OPCell{i}(:,1:2),3,21);
       
   end
