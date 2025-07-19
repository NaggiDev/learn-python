"""
Solution: Thread Pools and Advanced Threading

Complete implementation of thread pools and advanced threading patterns.
"""

import threading
import time
import random
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed, Future
from queue import Queue, Empty
import json


def simulate_io_task(task_id, duration=None):
    """Simulate an I/O-bound task like file reading or network request"""
    if duration is None:
        duration = random.uniform(0.5, 2.0)
    
    print(f"Task {task_id} starting (duration: {duration:.1f}s)")
    time.sleep(duration)
    result = f"Result from task {task_id}"
    print(f"Task {task_id} completed")
    return result


def simulate_cpu_task(n):
    """Simulate a CPU-bound task (calculating sum of squares)"""
    print(f"CPU task starting: sum of squares up to {n}")
    result = sum(i * i for i in range(n))
    print(f"CPU task completed: sum of squares up to {n} = {result}")
    return result


def fetch_url_info(url):
    """Fetch URL information and return details"""
    start_time = time.time()
    
    try:
        response = requests.get(url, timeout=5)
        response_time = time.time() - start_time
        
        return {
            'url': url,
            'status_code': response.status_code,
            'response_time': response_time,
            'content_length': len(response.content),
            'success': True
        }
    except Exception as e:
        response_time = time.time() - start_time
        return {
            'url': url,
            'status_code': None,
            'response_time': response_time,
            'content_length': 0,
            'success': False,
            'error': str(e)
        }


def demonstrate_basic_thread_pool():
    """Demonstrate basic ThreadPoolExecutor usage"""
    print("=== Basic Thread Pool Demo ===")
    
    tasks = list(range(1, 6))
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit all tasks
        futures = [executor.submit(simulate_io_task, task_id) for task_id in tasks]
        
        # Collect results
        results = []
        for future in futures:
            result = future.result()
            results.append(result)
        
        print(f"Completed {len(results)} tasks")


def demonstrate_thread_pool_with_different_args():
    """Demonstrate thread pool with different arguments for each task"""
    print("\n=== Thread Pool with Different Arguments ===")
    
    task_configs = [
        (1, 1.0),
        (2, 0.5),
        (3, 1.5),
        (4, 0.8),
        (5, 1.2)
    ]
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks with different arguments
        future_to_config = {
            executor.submit(simulate_io_task, task_id, duration): (task_id, duration)
            for task_id, duration in task_configs
        }
        
        # Process results as they complete
        for future in as_completed(future_to_config):
            task_id, duration = future_to_config[future]
            try:
                result = future.result()
                print(f"Task {task_id} (duration {duration}s) result: {result}")
            except Exception as e:
                print(f"Task {task_id} failed: {e}")


def demonstrate_url_fetching():
    """Demonstrate concurrent URL fetching"""
    print("\n=== Concurrent URL Fetching ===")
    
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/status/200",
        "https://httpbin.org/status/404",
        "https://httpbin.org/json",
        "https://httpbin.org/headers"
    ]
    
    # Sequential fetching
    print("Sequential fetching:")
    start_time = time.time()
    
    sequential_results = []
    for url in urls:
        result = fetch_url_info(url)
        sequential_results.append(result)
        print(f"  {result['url']}: {result['status_code']} ({result['response_time']:.2f}s)")
    
    sequential_time = time.time() - start_time
    print(f"Sequential time: {sequential_time:.2f} seconds")
    
    # Concurrent fetching
    print("\nConcurrent fetching:")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_to_url = {executor.submit(fetch_url_info, url): url for url in urls}
        
        concurrent_results = []
        for future in as_completed(future_to_url):
            result = future.result()
            concurrent_results.append(result)
            status = "SUCCESS" if result['success'] else "ERROR"
            print(f"  {result['url']}: {result.get('status_code', 'N/A')} ({result['response_time']:.2f}s) [{status}]")
    
    concurrent_time = time.time() - start_time
    print(f"Concurrent time: {concurrent_time:.2f} seconds")
    print(f"Speedup: {sequential_time / concurrent_time:.2f}x")


class WorkerPool:
    """Custom worker pool implementation using Queue and threads"""
    
    def __init__(self, num_workers=3):
        self.task_queue = Queue()
        self.workers = []
        self.shutdown_flag = False
        
        # Create and start worker threads
        for i in range(num_workers):
            worker = threading.Thread(target=self._worker, name=f"Worker-{i}")
            worker.start()
            self.workers.append(worker)
    
    def _worker(self):
        """Worker thread function"""
        while not self.shutdown_flag:
            try:
                # Get task from queue with timeout
                task = self.task_queue.get(timeout=1)
                
                if task is None:  # Shutdown sentinel
                    break
                
                func, args, kwargs = task
                try:
                    func(*args, **kwargs)
                except Exception as e:
                    print(f"Task failed: {e}")
                finally:
                    self.task_queue.task_done()
                    
            except Empty:
                continue  # Timeout, check shutdown flag
    
    def submit(self, func, *args, **kwargs):
        """Submit a task to the worker pool"""
        if not self.shutdown_flag:
            self.task_queue.put((func, args, kwargs))
    
    def shutdown(self):
        """Shutdown the worker pool"""
        self.shutdown_flag = True
        
        # Send shutdown signals to all workers
        for _ in self.workers:
            self.task_queue.put(None)
        
        # Wait for all workers to finish
        for worker in self.workers:
            worker.join()


def demonstrate_custom_worker_pool():
    """Demonstrate custom worker pool implementation"""
    print("\n=== Custom Worker Pool Demo ===")
    
    pool = WorkerPool(3)
    
    # Submit 8 I/O tasks to the pool
    for i in range(1, 9):
        pool.submit(simulate_io_task, i, 0.5)
    
    # Wait a bit for tasks to complete
    time.sleep(3)
    
    # Shutdown the pool
    pool.shutdown()
    print("Custom worker pool demo completed")


class TaskScheduler:
    """Task scheduler that can run tasks at specific intervals"""
    
    def __init__(self):
        self.scheduled_tasks = {}
        self.task_counter = 0
        self.scheduler_thread = None
        self.shutdown_flag = threading.Event()
        self.lock = threading.Lock()
        
        # Start scheduler thread
        self.scheduler_thread = threading.Thread(target=self._scheduler_loop)
        self.scheduler_thread.start()
    
    def schedule_once(self, func, delay, *args, **kwargs):
        """Schedule a function to run once after a delay"""
        with self.lock:
            self.task_counter += 1
            task_id = self.task_counter
            
            run_time = time.time() + delay
            self.scheduled_tasks[task_id] = {
                'func': func,
                'args': args,
                'kwargs': kwargs,
                'run_time': run_time,
                'recurring': False,
                'interval': None
            }
            
            return task_id
    
    def schedule_recurring(self, func, interval, *args, **kwargs):
        """Schedule a function to run repeatedly at intervals"""
        with self.lock:
            self.task_counter += 1
            task_id = self.task_counter
            
            run_time = time.time() + interval
            self.scheduled_tasks[task_id] = {
                'func': func,
                'args': args,
                'kwargs': kwargs,
                'run_time': run_time,
                'recurring': True,
                'interval': interval
            }
            
            return task_id
    
    def cancel_task(self, task_id):
        """Cancel a scheduled task"""
        with self.lock:
            if task_id in self.scheduled_tasks:
                del self.scheduled_tasks[task_id]
                return True
            return False
    
    def _scheduler_loop(self):
        """Main scheduler loop"""
        while not self.shutdown_flag.is_set():
            current_time = time.time()
            tasks_to_run = []
            tasks_to_reschedule = []
            
            with self.lock:
                for task_id, task_info in list(self.scheduled_tasks.items()):
                    if current_time >= task_info['run_time']:
                        tasks_to_run.append((task_id, task_info))
                        
                        if task_info['recurring']:
                            # Reschedule recurring task
                            task_info['run_time'] = current_time + task_info['interval']
                        else:
                            # Remove one-time task
                            del self.scheduled_tasks[task_id]
            
            # Execute tasks outside of lock
            for task_id, task_info in tasks_to_run:
                try:
                    task_info['func'](*task_info['args'], **task_info['kwargs'])
                except Exception as e:
                    print(f"Scheduled task {task_id} failed: {e}")
            
            time.sleep(0.1)  # Check every 100ms
    
    def shutdown(self):
        """Shutdown the scheduler and all running tasks"""
        self.shutdown_flag.set()
        if self.scheduler_thread:
            self.scheduler_thread.join()


def demonstrate_task_scheduler():
    """Demonstrate custom task scheduler"""
    print("\n=== Task Scheduler Demo ===")
    
    def print_message(message):
        print(f"[{time.strftime('%H:%M:%S')}] {message}")
    
    scheduler = TaskScheduler()
    
    # Schedule some tasks
    task1 = scheduler.schedule_once(print_message, 1, "One-time task executed!")
    task2 = scheduler.schedule_recurring(print_message, 2, "Recurring task executed!")
    
    # Let it run for 8 seconds
    time.sleep(8)
    
    # Cancel the recurring task
    scheduler.cancel_task(task2)
    print("Cancelled recurring task")
    
    # Wait a bit more
    time.sleep(3)
    
    # Shutdown the scheduler
    scheduler.shutdown()
    print("Task scheduler demo completed")


def demonstrate_thread_local_storage():
    """Demonstrate thread-local storage"""
    print("\n=== Thread-Local Storage Demo ===")
    
    thread_local_data = threading.local()
    
    def worker(worker_id):
        """Each worker sets and reads thread-local data"""
        # Set a unique value in thread-local storage
        thread_local_data.worker_id = worker_id
        thread_local_data.start_time = time.time()
        thread_local_data.random_value = random.randint(1, 1000)
        
        print(f"Worker {worker_id}: Set values - ID: {thread_local_data.worker_id}, "
              f"Random: {thread_local_data.random_value}")
        
        # Sleep for a random time
        sleep_time = random.uniform(0.5, 1.5)
        time.sleep(sleep_time)
        
        # Read and verify the values are still the same
        print(f"Worker {worker_id}: After sleep - ID: {thread_local_data.worker_id}, "
              f"Random: {thread_local_data.random_value}, "
              f"Duration: {time.time() - thread_local_data.start_time:.2f}s")
        
        # Verify the value is still the same
        assert thread_local_data.worker_id == worker_id
        print(f"Worker {worker_id}: Thread-local data integrity verified!")
    
    # Create 5 threads running the worker function
    threads = []
    for i in range(1, 6):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()


def performance_comparison():
    """Compare different threading approaches"""
    print("\n=== Performance Comparison ===")
    
    def run_tasks_sequential(tasks):
        """Run tasks sequentially"""
        results = []
        for task_id in tasks:
            result = simulate_io_task(task_id, 0.5)
            results.append(result)
        return results
    
    def run_tasks_manual_threads(tasks):
        """Run tasks using manual thread creation"""
        results = []
        results_lock = threading.Lock()
        
        def task_wrapper(task_id):
            result = simulate_io_task(task_id, 0.5)
            with results_lock:
                results.append(result)
        
        threads = []
        for task_id in tasks:
            thread = threading.Thread(target=task_wrapper, args=(task_id,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        return results
    
    def run_tasks_thread_pool(tasks):
        """Run tasks using ThreadPoolExecutor"""
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(simulate_io_task, task_id, 0.5) for task_id in tasks]
            results = [future.result() for future in futures]
        return results
    
    tasks = list(range(1, 11))  # 10 tasks
    
    # Test each approach
    approaches = [
        ("Sequential", run_tasks_sequential),
        ("Manual Threads", run_tasks_manual_threads),
        ("Thread Pool", run_tasks_thread_pool)
    ]
    
    for name, func in approaches:
        print(f"\nTesting {name}:")
        start_time = time.time()
        
        try:
            results = func(tasks)
            end_time = time.time()
            print(f"{name} completed in {end_time - start_time:.2f} seconds")
            print(f"Results: {len(results) if results else 0} tasks completed")
        except Exception as e:
            print(f"{name} failed: {e}")


if __name__ == "__main__":
    demonstrate_basic_thread_pool()
    demonstrate_thread_pool_with_different_args()
    demonstrate_url_fetching()
    demonstrate_custom_worker_pool()
    demonstrate_task_scheduler()
    demonstrate_thread_local_storage()
    performance_comparison()
    
    print("\n=== Exercise Complete ===")
    print("Key learnings:")
    print("1. ThreadPoolExecutor simplifies concurrent task execution")
    print("2. as_completed() allows processing results as they finish")
    print("3. Thread pools are more efficient than creating threads manually")
    print("4. Thread-local storage provides per-thread data isolation")
    print("5. Different threading patterns suit different use cases")