import React, { useState } from "react";

function HeapSortVisualizer() {
  const [array, setArray] = useState([]); // Array to be sorted
  const [delay, setDelay] = useState(1000); // Delay in milliseconds

  // Heapify function
  function heapify(arr, n, i) {
    let largest = i;
    let left = 2 * i + 1;
    let right = 2 * i + 2;

    if (left < n && arr[left].data > arr[largest].data) {  // Comparing data values
      largest = left;
    }

    if (right < n && arr[right].data > arr[largest].data) {  // Comparing data values
      largest = right;
    }

    if (largest !== i) {
      swap(arr, i, largest);
      setTimeout(() => heapify(arr, n, largest), delay);
    }
  }

  // Helper function to swap elements in the array
  function swap(arr, i, j) {
    const temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;

    setArray([...arr]);
  }

  // Heap sort function
  function heapSort() {
    const arr = [...array];
    const arraySize = arr.length;

    // Build a max heap
    for (let i = Math.floor(arraySize / 2) - 1; i >= 0; i--) {
      heapify(arr, arraySize, i);
    }

    // Extract elements one by one
    for (let i = arraySize - 1; i > 0; i--) {
      swap(arr, 0, i);
      setTimeout(() => heapify(arr, i, 0), delay);
    }
  }

  // Function to generate a random array for visualization
  function generateRandomArray() {
    const newArray = [];
    for (let i = 0; i < 10; i++) {
      const randomElement = {
        id: i,
        data: Math.floor(Math.random() * 100),
      };
      newArray.push(randomElement);
    }
    setArray(newArray);
  }

  return (
    <div>
      <button onClick={generateRandomArray}>Generate Random Array</button>
      <button onClick={heapSort}>Heap Sort</button>
      <ul>
        {array.map((item) => (
          <li key={item.id}>{item.data}</li>
        ))}
      </ul>
    </div>
  );
}

export default HeapSortVisualizer;
