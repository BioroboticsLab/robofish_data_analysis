function S = getAngle(OPCell)

S = OPCell;


[m,~] = size(OPCell{1});
for i =1 : length(S)
    for j=1 : m-1

            S{i}(j,3) = atan2(S{i}(j+1,2)-S{i}(j,2),S{i}(j+1,1)-S{i}(j,1));
            S{i}(j,3) = normalizeAngle(S{i}(j,3));
    end
end

