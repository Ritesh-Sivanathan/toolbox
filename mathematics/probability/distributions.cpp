#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

class Math {

	public:
		float Factorial(float n);
		float BinomialSuccesses(float n, float k, float p);
		float HypergeometricSuccesses(float n, float a, float r, float k);
		float Combination(float n, float r);
		float BinomialExpectedValue(float n, float p);
		float HypergeometricExpectedValue(float a, float r, float n);
};

float Math::Combination(float n, float r) {

	float res = (Factorial(n))/(Factorial(n-r)*Factorial(r));

	return res;

}

float Math::BinomialExpectedValue(float n, float p) {

	return n*p;

}

float Math::HypergeometricExpectedValue(float a, float r, float n) {

	return ((a*r)/(n));

}

float Math::Factorial(float n) { // Really only integers..

	float res = 1;

	for (int i=1; i<=n; i++) {
		res *= i;
	}

	return res;

}

float Math::BinomialSuccesses(float n, float k, float p) {

	float res = Combination(n,k) * pow(p, k) * pow(1-p, n-k);

	return res;

}

float Math::HypergeometricSuccesses(float n, float a, float r, float k) {	

	float num = (Combination(a,k)) * (Combination(n-a,r-k));

	float den = Combination(n,r);


	return num/den;
}

int main() {

	Math math;

	// Usage: math.SomeFunction()
	
	return 0;

}

