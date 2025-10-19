class Patient:
    def __init__(self, description, priroity):
        self.description = description
        self.priority = priroity



class MinHeap:
    def __init__(self):
        self.data = []
        
    def heapify_up(self, index):
        while index > 0:

            parent_index = (index - 1)

            current_task = self.data[index]
            parent_task = self.data[parent_index]

            if current_task.priroity < parent_task.priority:

                temp = self.data[index]
                self.data[index] = self.data[parent_index]
                self.data[parent_index] = temp

                index = parent_index
            else:
                break

    def heapify_down(self, index):

        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left].priority < self.data[smallest].priority:
            smallest = left
        if right < len(self.data) and self.data[right].priority < self.data[smallest].priority:
            smallest = right
        if smallest != index:
            temp = self.data[index]

            self.data[index] = self.data[smallest]
            self.data[smallest] = temp


            self.heapify_down(smallest)

    def remove_min(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        min_value = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return min_value

    def insert(self, task):
        self.data.append(task)
        self.heapify_up(len(self.data) - 1)    


# Test your MinHeap class here including edge cases
p1 = Patient("Riley", 2)
