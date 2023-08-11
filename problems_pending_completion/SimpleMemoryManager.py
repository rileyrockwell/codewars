class MemoryManager:
    def __init__(self, memory):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self.memory = memory

    def allocate(self, size):
        """
        Allocates a block of memory of requested size.
        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """

        # Attempt 1
        # return self.memory[size]

        # Attempt 2
        # how is block defined?
        # how is pointer defined?
        return self.memory * size


    def release(self, pointer):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """
        # does not return anything? updates list in place?
        self.memory.remove(self.memory[pointer])


    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """

    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """

if __name__ == "__main__":
	instance = MemoryManager([None] * 2)
	print(instance.memory)
	print(instance.allocate(2))
	print(instance.memory)
	print(instance.release(0))