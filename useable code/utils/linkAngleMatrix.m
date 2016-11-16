% M = linkAngleMatrix(P)
% computes link angle for all pairs, returns matrix M
% P has n columns containing fish coordinates and angles (x,y,angle)'
function M = linkAngleMatrix(P)
n = size(P,2);
M = zeros(n);
for i = 1:n
    for j = 1:n
        
        % i_direction = deg2rad(P(3,i));
        % j_direction = deg2rad(P(3,j));
        i_direction = P(3,i);
        j_direction = P(3,j);
        [x,y]=pol2cart(i_direction,1);
        v_i = [x y];
   
  
        
        v_i_to_j = P(1:2,j) - P(1:2,i);
        
        M(i,j) = angleBetweenTwoVectors(v_i, v_i_to_j);
        

    end
end

