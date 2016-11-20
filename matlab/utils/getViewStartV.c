#include "mex.h"
#include <math.h>

void mexFunction( int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[])
{
	double *ori_point,*angle,*point;
	double *rotated_point;

	if(nrhs != 3)
	{
		mexErrMsgTxt("Must have three input arguments.");
	}

	plhs[0] = mxCreateDoubleMatrix(1,2,mxREAL);
	rotated_point = mxGetPr(plhs[0]);


	ori_point = mxGetPr(prhs[0]);
	angle = mxGetPr(prhs[1]);
	point = mxGetPr(prhs[2]);

	double alpha = angle[0];

	// coordinate of ori_point
	double x = ori_point[0];
	double y = ori_point[1];

	// coordinate of point
	double x_shift = point[0];
	double y_shift = point[1];

    double s = sin(alpha*M_PI/180);
    double c = cos(alpha*M_PI/180);

	x_shift -=x;
	y_shift -=y;

	double x_new = x_shift * c - y_shift * s;
    double y_new = x_shift * s + y_shift * c;

    // x_shift = x_new + x;
    // y_shift = y_new + y;

    // rotated_point[0] = x_shift - x; 
    // rotated_point[1] = y_shift - y;
    rotated_point[0] = x_new;
    rotated_point[1] = y_new;

}