import os

dir_path = r'C:\Users\vitor\OneDrive\Imagens'

photos = []; 
outros = [];

def function():
    return r'\\';

os.mkdir('C:\Users\vitor\OneDrive\Imagens');

for path in os.listdir(dir_path): 
    if os.path.isfile(os.path.join(dir_path, path)):                   
        file_name, file_extension = os.path.splitext(os.path.join(dir_path, path)) 

        match file_extension:
            case ".jpg":
                photos.append(file_name + file_extension);
                print(file_name + file_extension);
            case ".jpg":
                photos.append(file_name + file_extension);
                print(file_name + file_extension);