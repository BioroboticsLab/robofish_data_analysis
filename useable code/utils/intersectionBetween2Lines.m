function P = intersectionBetween2Lines(L1,L2)

dx = diff(L1);
dy = diff(L2);
den = dx(1)*dy(2) - dy(1)*dx(2);
if (den == 0)
	P = [Inf,Inf];
else
	ua = (dx(2)*(L2(1)-L2(3)) - dy(2)*(L1(1)-L1(3)))/den;
	ub = (dx(1)*(L2(1)-L2(3)) - dy(1)*(L1(1)-L1(3)))/den;

	xi = L1(1) + ua*dx(1);
	yi = L2(1) + ua*dy(1);

	P = [xi,yi];
end