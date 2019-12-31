using System.Linq;
using System;
class MaxNetworkRank {
    // static void Main() {
    //     //I need to store the top pairs of cities that have the highest nodes connected to the pair
    //     MaxNetworkRank mnr = new MaxNetworkRank();
    //     int answer = mnr.networkMax(new int[]{1,2,3,3}, new int[]{2,3,1,4}, 4);
    //     Console.WriteLine(answer);
    // }
    public int networkMax(int[] A, int[] B, int roads)
    {
        int[] edgeCount = new int[A.Count()];

        for(int i = 0; i < roads; i++)
        {
            edgeCount[A[i]-1]++;
            edgeCount[B[i]-1]++;
        }
        int maxRank = Int32.MinValue;
        for(int i = 0; i < roads; i++)
        {
            int rank = edgeCount[A[i]-1] + edgeCount[B[i]-1] -1;
            if(rank > maxRank)
            maxRank = rank;
        }
        return maxRank;
    }
}