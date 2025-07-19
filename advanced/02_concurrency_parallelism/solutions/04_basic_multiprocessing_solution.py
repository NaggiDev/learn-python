"""
Solution: Basic Multiprocessing

Complete implementation of basic multiprocessing concepts.
"""

import multiprocessing
import time
import os
import math


def cpu_intensive_task(n, task_id):
    """CPU-intensive function that calculates sum of squares"""
    process_id = os.getpid()
    print(f"Task {task_id} (PID: {process_id}) starting with n={n}")
    
    # Calculate sum of squares from 1 to n
    result = sum(i * i for i in range(1, n + 1))
    
    print(f"Task {task_id} (PID: {process_id}) finished, result: {result}")
    return result


def io_simulation_task(task_id, duration):
    """Function that simulates I/O work"""
    process_id = os.getpid()
    print(f"I/O Task {task_id} (PID: {process_id}) starting")
    time.sleep(duration)
    print(f"I/O Task {task_id} (PID: {process_id}) completed")
    return f"Result from I/O task {task_id}"


class CalculatorProcess(multiprocessing.Process):
    """Custom process class that performs calculations"""
    
    def __init__(self, operation, number):
        super().__init__()
        self.operation = operation
        self.number = number
        self.result = None
    
    def run(self):
        process_id = os.getpid()
        print(f"Calculator Process (PID: {process_id}) starting {self.operation} of {self.number}")
        
        if self.operation == 'square':
            self.result = self.calculate_square(self.number)
        elif self.operation == 'factorial':
            self.result = self.calculate_factorial(self.number)
        elif self.operation == 'fibonacci':
            self.result = self.calculate_fibonacci(self.number)
        
        print(f"Calculator Process (PID: {process_id}) completed: {self.operation}({self.number}) = {self.result}")
    
    def calculate_square(self, n):
        """Calculate n squared"""
        return n * n
    
    def calculate_factorial(self, n):
        """Calculate n factorial"""
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def calculate_fibonacci(self, n):
        """Calculate nth Fibonacci number"""
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def demonstrate_basic_processes():
    """Demonstrate basic process creation and execution"""
    print("=== Basic Process Demo ===")
    print(f"Main process PID: {os.getpid()}")
    
    start_time = time.time()
    
    # Create two processes
    process1 = multiprocessing.Process(target=cpu_intensive_task, args=(100000, 1))
    process2 = multiprocessing.Process(target=cpu_intensive_task, args=(150000, 2))
    
    # Start both processes
    process1.start()
    process2.start()
    
    # Wait for completion
    process1.join()
    process2.join()
    
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")


def demonstrate_multiple_processes():
    """Demonstrate creating multiple processes with different tasks"""
    print("\n=== Multiple Processes Demo ===")
    
    processes = []
    
    # Create 2 CPU-intensive tasks
    cpu_process1 = multiprocessing.Process(target=cpu_intensive_task, args=(50000, 1))
    cpu_process2 = multiprocessing.Process(target=cpu_intensive_task, args=(75000, 2))
    processes.extend([cpu_process1, cpu_process2])
    
    # Create 2 I/O simulation tasks
    io_process1 = multiprocessing.Process(target=io_simulation_task, args=(1, 2))
    io_process2 = multiprocessing.Process(target=io_simulation_task, args=(2, 1.5))
    processes.extend([io_process1, io_process2])
    
    # Start all processes
    for process in processes:
        process.start()
    
    # Wait for all to complete
    for process in processes:
        process.join()
    
    print("All processes completed")


def demonstrate_process_class():
    """Demonstrate custom process class"""
    print("\n=== Custom Process Class Demo ===")
    
    # Create 3 CalculatorProcess instances
    calculators = [
        CalculatorProcess('square', 25),
        CalculatorProcess('factorial', 10),
        CalculatorProcess('fibonacci', 20)
    ]
    
    # Start all processes
    for calc in calculators:
        calc.start()
    
    # Wait for all to complete
    for calc in calculators:
        calc.join()
    
    print("All calculations completed")


def sequential_vs_parallel_cpu():
    """Compare sequential vs parallel execution for CPU-bound tasks"""
    print("\n=== Sequential vs Parallel CPU Tasks ===")
    
    def calculate_primes(limit):
        """Calculate prime numbers up to limit"""
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        
        primes = [i for i in range(2, limit) if is_prime(i)]
        return len(primes)
    
    limits = [10000, 15000, 20000, 25000]
    
    # Sequential execution
    print("Sequential execution:")
    start_time = time.time()
    
    sequential_results = []
    for limit in limits:
        result = calculate_primes(limit)
        sequential_results.append(result)
        print(f"  Primes up to {limit}: {result}")
    
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f} seconds")
    
    # Parallel execution
    print("\nParallel execution:")
    start_time = time.time()
    
    # Create processes to collect results
    def worker_with_result(limit, result_dict, index):
        result = calculate_primes(limit)
        result_dict[index] = result
        print(f"  Primes up to {limit}: {result}")
    
    # Use Manager to share results
    with multiprocessing.Manager() as manager:
        result_dict = manager.dict()
        processes = []
        
        for i, limit in enumerate(limits):
            process = multiprocessing.Process(
                target=worker_with_result, 
                args=(limit, result_dict, i)
            )
            processes.append(process)
            process.start()
        
        for process in processes:
            process.join()
        
        parallel_results = [result_dict[i] for i in range(len(limits))]
    
    parallel_time = time.time() - start_time
    print(f"Parallel time: {parallel_time:.2f} seconds")
    
    if sequential_time > 0 and parallel_time > 0:
        print(f"Speedup: {sequential_time / parallel_time:.2f}x")
    
    print(f"Results match: {sequential_results == parallel_results}")


def demonstrate_process_communication():
    """Demonstrate basic process communication using return values"""
    print("\n=== Process Communication Demo ===")
    
    def worker_with_result(n, process_id):
        """Worker that returns a result"""
        result = sum(i * i for i in range(n))
        print(f"Process {process_id}: Calculated sum of squares up to {n} = {result}")
        return result
    
    processes = []
    for i in range(3):
        process = multiprocessing.Process(
            target=worker_with_result, 
            args=(1000 * (i + 1), i + 1)
        )
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    print("Note: Basic Process class doesn't return values directly.")
    print("We'll learn about proper inter-process communication in the next exercise.")


def demonstrate_process_properties():
    """Demonstrate process properties and methods"""
    print("\n=== Process Properties Demo ===")
    
    def long_running_task(duration):
        """A task that runs for a specified duration"""
        print(f"Long running task starting (PID: {os.getpid()})")
        time.sleep(duration)
        print(f"Long running task completed (PID: {os.getpid()})")
    
    process = multiprocessing.Process(target=long_running_task, args=(3,), name="LongTask")
    
    # Check properties before starting
    print(f"Before starting:")
    print(f"  Name: {process.name}")
    print(f"  PID: {process.pid}")  # Will be None before starting
    print(f"  Is alive: {process.is_alive()}")
    
    process.start()
    
    # Check properties after starting
    print(f"\nAfter starting:")
    print(f"  Name: {process.name}")
    print(f"  PID: {process.pid}")
    print(f"  Is alive: {process.is_alive()}")
    
    # Wait a bit and check if still alive
    time.sleep(1)
    print(f"\nAfter 1 second:")
    print(f"  Is alive: {process.is_alive()}")
    
    process.join()
    
    # Check properties after completion
    print(f"\nAfter completion:")
    print(f"  Name: {process.name}")
    print(f"  PID: {process.pid}")
    print(f"  Is alive: {process.is_alive()}")


if __name__ == "__main__":
    print("Starting multiprocessing demonstrations...")
    print(f"Available CPU cores: {multiprocessing.cpu_count()}")
    
    demonstrate_basic_processes()
    demonstrate_multiple_processes()
    demonstrate_process_class()
    sequential_vs_parallel_cpu()
    demonstrate_process_communication()
    demonstrate_process_properties()
    
    print("\n=== Exercise Complete ===")
    print("Key observations:")
    print("1. Each process has its own Process ID (PID)")
    print("2. Processes run independently with separate memory spaces")
    print("3. CPU-bound tasks can benefit significantly from multiprocessing")
    print("4. Process creation has more overhead than thread creation")
    print("5. The 'if __name__ == \"__main__\":' guard is essential")