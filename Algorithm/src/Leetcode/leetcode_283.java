package Leetcode;

import java.util.ArrayList;
import java.util.Arrays;

public class leetcode_283 {

    public static void main(String[] args) {
        int[] nums = {0};
        int count =0;
        ArrayList<Integer> arrayList = new ArrayList<>();
        for(int a:  nums){
            if(a==0){
                count++;
                continue;
            }
            arrayList.add(a);

        }
            int [] result = new int[nums.length];
            int index;
            for(index =0;index<nums.length-count;index++){
                result[index] = arrayList.get(index);
            }
            for(int i= index;i<nums.length;i++){
                result[i]= 0;
            }

        System.out.println(Arrays.toString(result));


    }
}
