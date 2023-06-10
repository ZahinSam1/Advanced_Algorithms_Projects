

function heapify(arr, n, i) {
    let largest = i;
    let left = 2 * i + 1;
    let right = 2 * i + 2;
  
    if (left < n && arr[left][2] > arr[largest][2]) {  // Comparing finish times
      largest = left;
    }
  
    if (right < n && arr[right][2] > arr[largest][2]) {  // Comparing finish times
      largest = right;
    }
  
    if (largest !== i) {
      [arr[i], arr[largest]] = [arr[largest], arr[i]];
      heapify(arr, n, largest);
    }
  }
  
function heapSort(arr) {
    const arraySize = arr.length;
  
    // Build a max heap
    for (let i = Math.floor(arraySize / 2) - 1; i >= 0; i--) {
      heapify(arr, arraySize, i);
    }
  
    // Extract elements one by one
    for (let i = arraySize - 1; i > 0; i--) {
      [arr[i], arr[0]] = [arr[0], arr[i]];
      heapify(arr, i, 0);
    }
    
    return arr;
  }
  