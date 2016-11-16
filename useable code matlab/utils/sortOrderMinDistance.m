function sorted = sortOrderMinDistance(fishArray)


	P = fishArray(2:4,:);
	DM = distanceMatrix(P(1:2,:));
	DM2 = DM+DM';
	disSum = sum(DM2,2);

	tempA = [fishArray;disSum'];

	sorted = (sortrows(tempA.',5)).';

	sorted = sorted(1:4,:);