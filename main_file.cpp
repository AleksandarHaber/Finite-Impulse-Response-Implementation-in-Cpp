#include<vector>
#include<iostream>
#include<fstream>
#include<string>

using namespace std;

#include "functions.cpp"

int main()
{
    // input data vector 
    vector<double> u;
    // output vector 
    vector<double> y;
    //filter coefficients 
    vector<double> b={0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1};
    // strings for input and output data files 
    string file_name_input="input_data.txt";
    string file_name_output="output_data.txt";

    unsigned int N=b.size()-1;

    double output_value;

    int status=load_data(u,file_name_input);

    if(status==1)
    {
        exit(1);
    }

    for(unsigned int k=0; k<u.size(); k++)
    {
        if (k<=N-1)
        {
            output_value=0.0;
        }
        else 
        {
            output_value=0.0;
            for (unsigned int j=0; j<=N; j++)
            {
                output_value=output_value+b[j]*u[k-j];
            }

        }
        y.push_back(output_value);
    }

    status=save_data(y,file_name_output);
    
    if(status==1)
    {
        exit(1);
    }

    return 0;
}