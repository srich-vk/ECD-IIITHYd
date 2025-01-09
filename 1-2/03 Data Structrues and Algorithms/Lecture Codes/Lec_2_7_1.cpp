//Lecture 2: 7/1/25

// Merge Sort

// Merging: Combining 2 sorted arrays

/** 
 * To merge 2 sorted arrays, set 2 pointers to the start of 2 arrays, compare and select the smaller element
 * Append the element to the final array, and iterate the pointer of THAT array ONLY
 * Continue until either of the array runs out of elements
 */

/** Merge Sort:-
 * Divide the arrays into 2 smaller arrays 
 * If the 2 arrays are sorted, MERGE them
 * If they aren't, divide again.
 * Using recursion, since array of length 1 is always sorted, we can sort the array fully
 *-----------------------------------------
 * PseudoCode:-
 * 
 * mergeSort(arr, int left, int right){
 *  if (left >= right){
 *      return;
 *  }
 *  
 *  int mid = (left + right)/2;
 *  mergeSort(arr, mid + 1, right);
 *  mergeSort(arr, left, mid);
 *  merge(arr, left, mid, right);
 *                                                                                   
 * }
 * 
 *  In the above code, the mid index divides the main array into 2 subarrays, in order to reduce memory usage                            
 * ------------------------------------------
 * Time Complexity of Merge Sort
 *  
 *  Time taken for n size array = T(n)
 * 
 *  T(n) = T(n/2) + T(n/2) + <Merging Time>
 * 
 *  Merging has O(n) time complexity = c.n
 * 
 *  => T(n/4) + T(n/4) + c.(n/2) + T(n/4) + T(n/4) + c.(n/2) + c.n
 *  => 4T(n/4) + 2c.n
 *                                 
 *  => n.T(1) + log2(n).c.n = n.k + nlog(n).c
 * 
 *  Since nlog(n) is the bigger term, O notation of Merge Sort is nlog2(n)
 * 
 */

#include <iostream>
#include <vector>

using namespace std;

void vectorPrint(vector<int> v) {
    for (int i : v) {
        cout << i << " ";
    }
    cout << endl;
}

void merge(vector<int>* v, int left, int mid, int right) {
    int start1 = left, start2 = mid + 1;
    vector<int> o;

    while (start1 <= mid && start2 <= right) {
        o.push_back((*v)[start1] < (*v)[start2] ? (*v)[start1++] : (*v)[start2++]);
    }

    while (start1 <= mid) {
        o.push_back((*v)[start1++]);
    }
    while (start2 <= right) {
        o.push_back((*v)[start2++]);
    }

    for (int i = 0; i < o.size(); ++i) {
        (*v)[left + i] = o[i];
    }
}

void mergeSort(vector<int>* v, int left, int right) {
    if (left >= right) {
        return;
    }
    int mid = left + (right - left) / 2;
    mergeSort(v, left, mid);
    mergeSort(v, mid + 1, right);
    merge(v, left, mid, right);
}

int main() {
    vector<int> v1 = {5, 9, 10, 15, 53, 4, 17, 26, 58, 90};
    mergeSort(&v1, 0, 9);
    vectorPrint(v1);
    return 0;
}
