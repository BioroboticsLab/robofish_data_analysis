function S = waveletSmooth(OPCell,wname)
    
   S = OPCell;
   for i=1 : length(OPCell)
       X = OPCell{i}(:,1);
       Y = OPCell{i}(:,2);

       [F1,F2]= wfilters(wname, 'l');
       [cA,cD] = dwt(X,F1,0);
       X = idwt(cA,cD,wname);
       [cA,cD] = dwt(Y,F1,0);
       Y = idwt(cA,cD,wname);

       S{i}(:,1) = X(1:end-1);
       S{i}(:,2) = Y(1:end-1);
       
   end
