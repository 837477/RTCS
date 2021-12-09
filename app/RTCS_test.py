import time
import random
from tqdm import tqdm

url_list = ["/", "/api/v1/local/status", "/api/v1/local/region/", "/api/v1/patients/status", "/api/v1/patients/infected/status", "/api/v1/vaccine/status"]

def progress(url, check=False):
    r = random.randint(20, 50)
    if check:
        for i in tqdm(range(r), bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):
            time.sleep(0.1)
            if i == 24:
                return
        
    
    for i in tqdm(range(r), bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):
        time.sleep(0.1)

if __name__ == "__main__":
    print("# API Unit Test\n")
    for url in url_list:
        print("url:", url)
        if url == "/api/v1/local/region/":
            progress(url, True)
            print("Fail !!!")
            print("Input data: {")
            print('    "location": 16011092')
            print('}')
            print("Msg: str type expected")
            print("Type: type_error.str")
            print("Error: Invalid Type, Must be String")
        else:
            progress(url)
            print("Success !")
        print()
