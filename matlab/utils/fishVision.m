function vision = fishVision(fishSwarm,fishID,parameters)

	fishwidth = parameters.fishwidth;
	fishLength = parameters.fishLength;

	% the unit vector of fish
% 	fishUnitV = getFishUnitVector(fishSwarm(fishID,1:2),fishSwarm(fishID,3));
    fishUnitV = zeros(1,2);
    [fishUnitV(1),fishUnitV(2)] = pol2cart(fishSwarm(fishID,3),1);
	% the position of fish eye
% 	fishEyeP = [fishSwarm(fishID,1)+parameters.fishEyeOffset*fishLength(fishID)*fishUnitV(1),...
% 				fishSwarm(fishID,2)+parameters.fishEyeOffset*fishLength(fishID)*fishUnitV(2)];

    fishEyeP = fishSwarm(fishID,1:2);

    viewStartV = getViewStartV(fishEyeP,0.5*parameters.viewingAngle,...
                                   [fishEyeP(1)+fishUnitV(1),fishEyeP(2)+fishUnitV(2)]);


    A = [];
    V = [];

	for i=1 : parameters.numFish
		if i == fishID
			continue;
		end

		%OUnitVec : the unit vector of observed fish 
		% OUnitVec = getFishUnitVector(fishSwarm(i,1:2),fishSwarm(i,3));
        OUnitVec = zeros(1,2);
		[OUnitVec(1),OUnitVec(2)] = pol2cart(fishSwarm(i,3),1);
			
		% observed fish position
	    fP = fishSwarm(i,1:2);
		% observed fish head position
		fhP =[fishSwarm(i,1)+0.5*fishLength(i)*OUnitVec(1),...
			  fishSwarm(i,2)+0.5*fishLength(i)*OUnitVec(2)];
		% observed fish tail position
		ftP =[fishSwarm(i,1)-0.5*fishLength(i)*OUnitVec(1),...
			  fishSwarm(i,2)-0.5*fishLength(i)*OUnitVec(2)];


		
		a = angleBetweenVectors2dClockwise(viewStartV,ftP-fishEyeP);
		A = [A a];


        v1 = ftP-fishEyeP;
        v2 = fhP-fishEyeP;
        V = [V v1 v2];
	end

	[~,idx] = sort(A);
	sortV = V;
	for i = 1: length(idx)
		sortV(2*(i-1)+1:2*i) = V(2*(idx(i)-1)+1:2*idx(i));
    end


	ob1 = radtodeg(fishSwarm(fishID,3)) - 90;
	ob2 = radtodeg(fishSwarm(fishID,3)) - 45;
	ob3 = radtodeg(fishSwarm(fishID,3));
	ob4 = radtodeg(fishSwarm(fishID,3)) + 45;
	ob5 = radtodeg(fishSwarm(fishID,3)) + 90;

	ob1 = normalizeAngle(degtorad(ob1));
	ob2 = normalizeAngle(degtorad(ob2));
	ob3 = normalizeAngle(degtorad(ob3));
	ob4 = normalizeAngle(degtorad(ob4));
	ob5 = normalizeAngle(degtorad(ob5));

	r1 = createRay(fishEyeP, ob1);
	r2 = createRay(fishEyeP, ob2);
	r3 = createRay(fishEyeP, ob3);
	r4 = createRay(fishEyeP, ob4);
	r5 = createRay(fishEyeP, ob5);

	tankWidth = parameters.tankWidth;
	tankHight = parameters.tankHight;

	tank = [0,0; parameters.tankWidth,0; parameters.tankWidth,parameters.tankHight; 0,parameters.tankHight];


	[intersect1, ~] = intersectRayPolygon(r1,tank);
	[intersect2, ~] = intersectRayPolygon(r2,tank);
	[intersect3, ~] = intersectRayPolygon(r3,tank);
	[intersect4, ~] = intersectRayPolygon(r4,tank);
	[intersect5, ~] = intersectRayPolygon(r5,tank);

	intersects = [intersect1; intersect2; intersect3; intersect4; intersect5];
    fishEyePArray = repmat(fishEyeP,[5,1]);
    dif = intersects - fishEyePArray;
    dists = sqrt(sum(dif.^2,2));
	vision = [sortV dists'];
	

