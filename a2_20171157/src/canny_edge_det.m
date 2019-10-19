clc;
img = imread('bell.jpg');
img = rgb2gray(img);
subplot(1,2,1);
imshow(img);
title('Original Image');
img = edge(img,'canny',[0 0.23]);
subplot(1,2,2);
imshow(img);
title('After Canny');
figure;
img = imread('cubes.png');
img = rgb2gray(img);
subplot(1,2,1);
imshow(img);
title('Original image');
img = edge(img,'canny',[0 0.10]);
subplot(1,2,2);
imshow(img);
title('After Canny');