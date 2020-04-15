/*
结合的两张图片type和size必须一致
*/

#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
	Mat src1, src2, dst;
	src1 = imread("C:/Users/MI/Pictures/white.png");
	src2 = imread("C:/Users/MI/Pictures/logo_combin.jpg");
	if (!src1.data) {
		cout << "could not load image Linux Logo..." << endl;
		return -1;
	}
	if (!src2.data) {
		cout << "could not load image WIN7 Logo..." << endl;
		return -1;
	}

	double alpha = 0.5;
	if (src1.rows == src2.rows && src1.cols == src2.cols && src1.type() == src2.type()) {
		addWeighted(src1, alpha, src2, (1.0 - alpha), 0.0, dst);
		// multiply(src1, src2, dst, 1.0);

		namedWindow("linuxlogo", WINDOW_AUTOSIZE);
		imshow("linuxlogo", src1);
		namedWindow("win7logo", WINDOW_AUTOSIZE);
		imshow("win7logo", src2);
		namedWindow("blend demo", WINDOW_AUTOSIZE);
		imshow("blend demo", dst);
	}
	else {
		printf("could not blend images , the size of images is not same...\n");
		return -1;
	}

	waitKey(0);
	return 0;
}
