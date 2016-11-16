% M = includedAngle(P)
% computes included angle for all pairs, returns matrix M
% P has n columns containing fish included angles (angle)
function M = includedAngleMatrix(P)
n = size(P,2);
M = zeros(n);
for i = 1:n
    for j = i:n
        % x = P(i)-P(j);
        % if abs(x)>180 && abs(x)<360
        %     x = (360-abs(x))*(abs(x)/x);
        % end
        % M(i,j)=x;
        M(i,j) = angleDiff(P(i),P(j));
    end
end

M = M + -1*M';