class RemoveDigits {
    static void Main() {
        RemoveDigits sln = new RemoveDigits();
        string a = "10200";
        int digits = 1;
        string answer = sln.RemoveKDigits(a, digits);
        System.Console.WriteLine(answer);
    }
    public string RemoveKDigits(string input, int k)
    {
        int newLength = input.Length - k;
        //I need a new character array to keep track of what my new string will look like, it will be k digits smaller
        char[] smallerString = new char[newLength];
        //I need two pointers one at the beginning one at the end
        int begin = 0; // this is the beginnign of the sliding window
        int end = k; //this is the end of the sliding window 
        
        //loop through the list and look at 
        for(int i = 0; i < newLength; i++)
        {
            int min = begin;
            
            //go through as many digits as you can remove
            for(int j = begin; j<=end; j++)
            {
                //compare current value to value at the smallest index
                if(input[j]< input[min])
                {
                    min = j; //update smallest index
                }
            }
            //if(input[i])
            //build up smallerString
            smallerString[i] = input[min];//smallest value that is next
            begin = min +1; // move the sliding window forward
            end++; // move the sliding window forward
        }
        var result = new string(smallerString);
        //result.TrimStart('0');
        return(result.TrimStart('0'));
    }
}