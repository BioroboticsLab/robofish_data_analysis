
function N = getStateDataPair(X)

    
    %distance
    DM =  norm(X(1:2) - X(4:5));
    
    P = reshape(X,[3,2]);
    %link angle matrix   
    LAM = linkAngleMatrix(P);

    %included angle matrix

    IM = angleDiff(X(1,3), X(1,6));

    % V = X(4:5) - X(1:2);


    N = [DM reshape(LAM.',1,[]) IM];
    N = N([1,3,4,6]);
    % N = [N V];
    sidewardDistance_i = N(1) * sin( N(2) );
    sidewardDistance_j = N(1) * sin( N(3) );
    N = [N sidewardDistance_i sidewardDistance_j];

end


