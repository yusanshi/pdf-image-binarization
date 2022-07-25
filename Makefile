all:
	g++ local_adaptive_binarization/binarizewolfjolion.cpp -o binarization `pkg-config --libs --cflags opencv4` -lstdc++

clean:
	rm -f binarization


