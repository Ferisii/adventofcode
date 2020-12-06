from time import time

def ExecutionTime(method):
    def timed(*args, **kwargs):
        start_time = time()
        result = method(*args, **kwargs)
        finish_time = time()

        print(f"{method.__name__} finished in {finish_time - start_time}")
        
        return result
    
    return timed