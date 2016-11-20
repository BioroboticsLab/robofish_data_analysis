% [cA,cH,cV,cD] = dwt2(X,2,0);
load('../OP.mat')

%wavelet filter
[F1,F2]= wfilters('db4', 'l');
[cA,cD] = dwt(OP(:,1),F1,0);
A0 = idwt(cA,cD,'db4');
hold on;
plot(OP(1:2000,1),'g-'); plot(A0(1:2000),'b-')
% legend('orginal','wavelet filter')


% %% %%%fft
X = OP(1:20000,1);
Y = fft(X);
t = 1:1:20000;
r = 300;
% % %% gauss filter
% % r = 300;
% % gauss = zeros(size(Y));
% % sigma = 8;                           % just a guess for a range of ~20
% % gauss(1:r+1) = exp(-(1:r+1).^ 2 / (2 * sigma ^ 2));  % +ve frequencies
% % gauss(end-r+1:end) = fliplr(gauss(2:r+1));           % -ve frequencies
% % y_gauss = ifft(Y.*gauss);
% % 
% % hold on;
% % plot(t,X,'g-');
% % plot(t,y_gauss,'b-')
% 
%%% low pass
rectangle = zeros(size(Y));
rectangle(1:r+1) = 1;               % preserve low +ve frequencies
y_half = ifft(Y.*rectangle);   % +ve low-pass filtered signal
rectangle(end-r+1:end) = 1;         % preserve low -ve frequencies
y_rect = ifft(Y.*rectangle);   % full low-pass filtered signal


plot(t(1:2000),y_rect(1:2000),'m-');
% 
% 
% 
% 
%%smooth
z = sgolayfilt(X,3,11);
plot(t(1:2000),z(1:2000),'k-')

legend('original x coord.','wavelet filter','fft low-pass x coord.', 'sgolayfilt x coord.')