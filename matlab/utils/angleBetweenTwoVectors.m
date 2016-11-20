function angle = angleBetweenTwoVectors(v1,v2)
% from v1 to v2
% if counterclockwise angle return positiv, then negativ

dotv = v1(1)*v2(1) + v1(2)*v2(2);
detv = v1(1)*v2(2) - v1(2)*v2(1);

angle = atan2(detv,dotv);
