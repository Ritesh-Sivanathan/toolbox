#ifndef PROBABILITY_H
#define PROBABILITY_H

float Factorial(float n);
float BinomialSuccesses(float n, float k, float p);
float HypergeometricSuccesses(float n, float a, float r, float k);
float Combination(float n, float r);
float BinomialExpectedValue(float n, float p);
float HypergeometricExpectedValue(float a, float r, float n);

#endif

