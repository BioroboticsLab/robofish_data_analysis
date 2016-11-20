function S = wSmooth(OP)
       [m,n] = size(OP);
       if(n==2)
           X = OP(:,1);
           Y = OP(:,2);

           [F1,F2]= wfilters('db4', 'l');
           [cA,cD] = dwt(X,F1,0);
           X = idwt(cA,cD,'db4');
           [cA,cD] = dwt(Y,F1,0);
           Y = idwt(cA,cD,'db4');
           S(:,1) = X;
           S(:,2) = Y;
       else
           [F1,F2]= wfilters('db4', 'l');
           [cA,cD] = dwt(OP,F1,0);
           S = idwt(cA,cD,'db4');
       end

