import time
from hashmap import HashMap



def read_birds_hashmap(filename):
   bird_counts = HashMap(size = 100)  
    
   try:
      with open(filename, 'r') as file:
         for line in file:
            bird = line.strip()
            if bird in bird_counts:
               bird_counts[bird] = bird_counts[bird] + 1
            else:
               bird_counts[bird] = 1
        

      for bird in bird_counts.get_keys():
         print(f"{bird} {bird_counts[bird]}")
      return bird_counts
        
   except FileNotFoundError:
      print(f"{filename} not found")
      return HashMap(size = 1)




def read_birds_dictionary(filename):
   bird_counts = {}
    
   try:
      with open(filename, 'r') as file:
         for line in file:
            bird = line.strip()
            
            if bird in bird_counts:
               bird_counts[bird] = bird_counts[bird] + 1
            else:
               bird_counts[bird] = 1
        
        
      
      for bird in bird_counts:
         count = bird_counts[bird]
         print(f"{bird} {count}")
      return bird_counts
        
   except FileNotFoundError:
      print(f"'{filename}' not found.")
      return {}
      
   



if __name__ == "__main__":
   
   start = time.perf_counter()
   print('-' * 3, "Reading bird_observations_small.txt with Python dictionary", '-' * 3)
   results = read_birds_dictionary("bird_observations_small.txt")
   read_time = time.perf_counter() - start
   print('-' * 3, "Total time for reading bird_observations_large.txt with Python dictionary = ", read_time, '-' * 3, '\n')


   start = time.perf_counter()
   print('-' * 3, "Reading bird_observations_small.txt with my HashMap implementation", '-' * 3)
   results = read_birds_hashmap("bird_observations_small.txt")
   read_time = time.perf_counter() - start
   print('-' * 3, "Total time for reading bird_observations_large.txt with my HashMap implementation = ", read_time, '-' * 3, '\n')
