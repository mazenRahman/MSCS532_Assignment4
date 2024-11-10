import heapq

class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # Define comparison for min-heap based on priority
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority}, Arrival={self.arrival_time}, Deadline={self.deadline})"


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        heapq.heappush(self.heap, task)
        print(f"Inserted: {task}")

    def extract_min(self):
        if self.is_empty():
            print("Priority queue is empty.")
            return None
        task = heapq.heappop(self.heap)
        print(f"Extracted task with highest priority: {task}")
        return task

    def increase_priority(self, task_id, new_priority):
        for i, task in enumerate(self.heap):
            if task.task_id == task_id and new_priority < task.priority:
                self.heap[i].priority = new_priority
                heapq.heapify(self.heap)  # Restore the heap property after priority change
                print(f"Updated task {task_id} to new priority: {new_priority}")
                return
        print(f"Task with ID {task_id} not found or new priority is not higher.")

    def display(self):
        print("Current priority queue:")
        for task in self.heap:
            print(task)


def main():
    pq = PriorityQueue()

    # Sample inputs for the Priority Queue
    while True:
        print("\n1. Insert task")
        print("2. Extract task with highest priority")
        print("3. Increase task priority")
        print("4. Display priority queue")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            task_id = input("Enter Task ID: ")
            priority = int(input("Enter Task Priority (lower number = higher priority): "))
            arrival_time = int(input("Enter Arrival Time: "))
            deadline = int(input("Enter Deadline: "))
            task = Task(task_id, priority, arrival_time, deadline)
            pq.insert(task)

        elif choice == 2:
            pq.extract_min()

        elif choice == 3:
            task_id = input("Enter Task ID to increase priority: ")
            new_priority = int(input("Enter new priority (lower number = higher priority): "))
            pq.increase_priority(task_id, new_priority)

        elif choice == 4:
            pq.display()

        elif choice == 5:
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main function
main()
