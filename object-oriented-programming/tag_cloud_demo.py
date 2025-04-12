class TagCloud:
    def __init__(self):
        self.__tags = {}
        
    def add(self, tag):
        tag = tag.strip().lower()  # Normalize the tag to lowercase and remove leading/trailing spaces
        if tag in self.__tags:   # alternative : self.tags[tag] = slef.tags.get(tag, 0) + 1
            self.__tags[tag] += 1
        else:
            self.__tags[tag] = 1
            
    def __getitem__(self, tag):
        tag = tag.strip().lower()
        return self.__tags.get(tag, 0)
    
    def __setitem__(self, tag, count):
        tag = tag.strip().lower()
        if count <= 0:
            raise ValueError("Count must be positive")
        self.__tags[tag] = count
        
    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("PythOn")


print(cloud.__tags)