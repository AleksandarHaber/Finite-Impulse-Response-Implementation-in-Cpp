#include<vector>
#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int load_data(vector<double>& loaded_data,const string& file_name)
{
    ifstream inputStream;

    double value;

    // open the file 

    inputStream.open(file_name);

    if(inputStream.fail())
    {
        cout<<"Failed to open the input file!"<<endl;
        return 1;
    }

    while(inputStream>>value)
    {
        loaded_data.push_back(value);
    }

    inputStream.close();

    return 0;
}

int save_data(vector<double>& data, const string& file_name)
{
    ofstream outStream;
    outStream.open(file_name);

    if(outStream.fail())
    {
        cout<<"Could not open the file"<<endl;
        return 1;
    } 

    for(unsigned int i=0; i<data.size(); i++)
    {
        outStream<<data[i]<<endl;
    }

    outStream.close();

    return 0;

}