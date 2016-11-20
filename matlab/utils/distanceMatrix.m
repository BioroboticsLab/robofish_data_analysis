% M = distanceMatrix(P)
% computes eucledian distances for all pairs, returns matrix M
% P has n columns containing coordinates (x,y)' 
function M = distanceMatrix(P)
n = size(P,2);
M = zeros(n);
for i = 1:n
    for j = i:n
        M(i,j) = norm( P(:,i) - P(:,j) );
    end
end

