function Y = fftSmooth(X,r)

Y = fft(X);
rectangle = zeros(size(Y));
rectangle(1:r+1) = 1;               

rectangle(end-r+1:end) = 1;      
Y = ifft(Y.*rectangle); 
 
t = 1:1:length(Y);

plot(t,Y,'r-');