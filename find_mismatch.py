class Sol:
    def find_mismatch(self,arr):
        l=[i+1 for  i in range(len(arr))]
        return [sum(arr)-sum(set(arr)),sum(l)-sum(set(arr))]

if __name__ == '__main__':
    p = Sol()
    print(p.find_mismatch([1,3,3]))
