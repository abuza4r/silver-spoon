#include <iostream>
#include <ctime>
#include <cstdlib>
#include <cmath>

using namespace std;

int main(){
    int l=7, an, sm;
    srand(time(0));
    for(int i=0; i<20; i++){
        for(int j=0; j<l; j++){
        an=1+rand()%2;
        if(an==1){
                sm=97+rand()%25;
                cout<< (char)sm;
        }else{
                sm=48+rand()%9;
                cout<< (char)sm;}
        }cout<<endl;
        }
    }
