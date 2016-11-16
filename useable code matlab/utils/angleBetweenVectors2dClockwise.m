function Angle = angleBetweenVectors2dClockwise(v1,v2)


ang = atan2(v1(1)*v2(2)-v2(1)*v1(2),v1(1)*v2(1)+v1(2)*v2(2));
Angle = mod(-180/pi * ang, 360);