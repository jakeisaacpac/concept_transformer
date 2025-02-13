def create_map(data, current_path=None):
   if current_path is None:
       current_path = []
   
   paths = set()
   paths.add(tuple(current_path))
   
   if isinstance(data, list):
       for i, item in enumerate(data):
           new_path = current_path + [i]
           paths.add(tuple(new_path))
           paths.update(tuple(p) for p in create_map(item, new_path))
   
   return [list(p) for p in sorted(paths, key=lambda x: (len(x), x))]

def get_content_from_path(data, path):
   current = data
   try:
       for index in path:
           current = current[index]
       return current
   except (IndexError, TypeError):
       return "Invalid Path"

def reorder_map(paths):
    def path_hierarchy_key(path):
        # Priority based on the full path hierarchy
        return tuple(path)
    
    return sorted(paths, key=path_hierarchy_key)

''' Example usage:
map_crude = create_map(data)
map_crude_reordered = reorder_map(map_crude)
print("Reordered paths:")
for i, path in enumerate(map_crude_reordered, 1):
   path_str = " -> ".join(str(index) for index in path)
   print(f"Path {i}: {path_str}")
   print(get_content_from_path(data, path))
 x '''


''' ARCHIVED CODE

def find_all_index_paths(data, current_path=None):
    if current_path is None:
        current_path = []
    
    paths = set()
    paths.add(tuple(current_path))
    
    if isinstance(data, list):
        for i, item in enumerate(data):
            new_path = current_path + [i]
            paths.add(tuple(new_path))
            paths.update(tuple(p) for p in find_all_index_paths(item, new_path))
    
    # Sort first by length, then by values within each path
    return [list(p) for p in sorted(paths, key=lambda x: (len(x), x))]

# Print paths with proper formatting
paths = find_all_index_paths(data)
print("All possible index paths:")
for i, path in enumerate(paths, 1):
    path_str = " -> ".join(str(index) for index in path)
    print(f"Path {i}: {path_str}")

print(paths)

#######################################################

def get_content_from_path(data, path):
   current = data
   try:
       for index in path:
           current = current[index]
       return current
   except (IndexError, TypeError):
       return "Invalid Path"

paths = find_all_index_paths(data)
for path in paths:
   print(f"{' -> '.join(str(index) for index in path)}: {get_content_from_path(data, path)}\n")



##################################################################################################

def reorder_paths(paths):
    def path_hierarchy_key(path):
        # Priority based on first number
        first_level = path[0] if path else float('inf')
        
        # For paths starting with 1 (topics), organize by topic number
        if first_level == 1 and len(path) > 1:
            topic_num = path[1]  # Which topic (0, 1, etc.)
            remainder = path[2:] # Rest of path
            return (first_level, topic_num, len(path), path)
        
        # For bibliography (2), keep simple ordering
        if first_level == 2:
            return (first_level, 0, len(path), path)
            
        # For title (0), keep at top
        return (first_level, 0, len(path), path)
    
    return sorted(paths, key=path_hierarchy_key)

# Test it
paths = find_all_index_paths(data)
ordered_paths = reorder_paths(paths)
print("Reordered paths:")
for i, path in enumerate(ordered_paths, 1):
    path_str = " -> ".join(str(index) for index in path)
    print(f"Path {i}: {path_str}")
    print(get_content_from_path(data, path))
    '''