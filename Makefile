all:
	g++ -I/usr/include/opencv local_adaptive_binarization/binarizewolfjolion.cpp -o binarization `pkg-config opencv --libs` -lstdc++

clean:
	rm -f binarization


