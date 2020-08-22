#include <iostream>



int gcd (int a, int b){
	return b? gcd(b,a%b):a;
}

int lcm (int a, int b){
	return a/gcd(a,b)*b;
}

int main (){
	int a,b; std::cin >> a >> b;
	std:: cout << gcd(a,b) << ' ' << lcm (a,b) << '\n';
	
	
	return 0;
}