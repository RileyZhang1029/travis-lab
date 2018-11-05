from numpy import *
from PIL import Image, ImageDraw, ImageFilter
import imageio
import time
import os

def image_to_dat(image_file, dat_file):
    img = Image.open(image_file)
    # Convert from RGB to grayscale (0..255)
    img = img.convert('L')
    np_img = array(img)
    # Invert image. Each value set to 255 - value.
    # Black (0) pixels, become 1. White (255) pixels become 0.
    np_img = invert(np_img)
    # Set non-white (non 0) pixels to black.
    np_img[np_img > 0] = 1
    (height, width) = np_img.shape
    header = "%d %d" % (width, height)
    savetxt(dat_file, np_img, fmt="%d", header=header, comments="")
    return np_img

def dat_to_data(dat_file):
    '''This function retrieves the shape and array of the data out of the inputed dat file '''
    #Get array of the landscape
    data_array = genfromtxt(dat_file, skip_header = 1, dtype = int) 
    #Get shape(height, width) of the landscape
    data_shape = data_array.shape
    return(data_shape,data_array)

def initial_rand(data_shape,land_array):
    '''This function creates random density for each grid square in the range from 0.0 to 5.0 '''
    den_array = random.random(data_shape) * 5.0
    den_array[land_array == 0] = 0
    return den_array

def sum_neighbours(data_array,land_array):
    '''This function sums the values of neighbouring grid squares for each specified grid square,
    at positions where the land_array values are non-zero.'''
    data_shape = shape(data_array)
    # Create a copy of the data_array with a halo of zeroes
    zeros_side = zeros((data_shape[0],1))
    zeros_top = zeros((1,data_shape[1]+2))
    middle_block = block([zeros_side, data_array, zeros_side]) 
    halo = block([[zeros_top],
                         [middle_block],
                         [zeros_top]
                         ])
    # This will be the array that will be returned later on
    output_array = zeros(data_shape)
    # Summing of the neighbours starts below
    for i in range(data_shape[0]):
        for j in range(data_shape[1]):
                output_array[i][j] = halo[i][j+1] + halo[i+2][j+1] + halo[i+1][j+2] + halo[i+1][j]
    output_array[land_array == 0] = 0.
    return output_array

def output_PPM(color,H,ppm_name):
    '''This function generates ppm image for the array H '''
    width = shape(H)[1]
    height = shape(H)[0]
    image = Image.new('RGB',(width,height),(255,255,255))
    draw = ImageDraw.Draw(image)
    for i in range(width):
        for j in range(height):
            d = H[j][i]
            if(color == 'red'):
                draw.point((i,j),fill=(255,int(255-d*50),int(255-d*50)))
            elif(color == 'blue'):
                draw.point((i,j),fill=(int(255-d*50),int(255-d*50),255))
                
    image.save(ppm_name,'ppm')

#    with open(ppm_name, 'wb') as f:
#        f.write(bytearray(ppm_header, 'ascii'))
#        H.tofile(f)
#    maxval = 255
#    ppm_header = f'P3 {width} {height} {maxval}\n'
#    print(H,'\n',P)
    # output the ppm files here
    
def average(H):
    '''This function calculates the average value of H. '''
    aver=sum(sum(H[i]) for i in range(len(H)))/H.shape[0]/H.shape[1]
    return aver

def cal(a,b,r,k,l,m,dt,land_array,H,P):
    '''This function updates arrays H and P for each time interval dt '''
    HP = H*P
    # Number of "dry" neighbours for each grid square
    dry_neighbours = sum_neighbours(land_array,land_array)
    H = H + dt*(r*H - a*HP + k*(sum_neighbours(H,land_array) - dry_neighbours * H))
    P = P + dt*(b*HP - m*P + l*(sum_neighbours(P,land_array) - dry_neighbours * P))
    return (H,P)

def output_GIF(H,P,dt,T):
    '''This function outputs gif of arrays H and P for each time interval dt'''
    image_list_H = []
    image_list_P = []
    output_PPM('red',H,'ppm_H_0.0.ppm')
    output_PPM('blue',P,'ppm_P_0.0.ppm')
    print(H,'\n',P)
    t, checker = dt, 1
    # Initialise the time t and count for T timing to the next time interval
    while t < 500.:
        d = round(t/dt)/T
        if checker == T:
            ppm_name_H = 'ppm_H_'+str(d)+'.ppm'
            ppm_name_P = 'ppm_P_'+str(d)+'.ppm'
            image_list_H.append(ppm_name_H)
            image_list_P.append(ppm_name_P)
            H = cal(a,b,r,k,l,m,dt,land_array,H,P)[0]
            P = cal(a,b,r,k,l,m,dt,land_array,H,P)[1]   
            #Ppm function here!
            output_PPM('red',H,ppm_name_H)
            output_PPM('blue',P,ppm_name_P)
            checker = 0
        checker += 1
        t += dt
    create_gif(image_list_H, 'Outputs_H.gif')
    create_gif(image_list_P, 'Outputs_P.gif')
#    return (image_list_H,image_list_P)
 
def create_gif(image_list, gif_name):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif 
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.1)
    return     
   
if __name__ == '__main__':
    # Start timing
    start = time.time()
    a,b,r,k,l,m,dt,T = 0.04,0.02,0.08,0.2,0.2,0.06,0.4,4
    dat_file ="dat_file.dat"
    image_file = "pic_40.bmp"
    image_to_dat(image_file, dat_file)
    land_data = dat_to_data(dat_file)
    # Shape of the landscape
    land_shape = land_data[0]
    # Binary array of the landscape
    land_array = land_data[1]
    # New a folder to place ppm files
    os.getcwd()
    if not os.path.isdir("Outputs"):
        os.mkdir("Outputs")
        os.chdir("Outputs")
    else:
        os.chdir("Outputs")
        for item in os.listdir(str(os.getcwd())):
            os.remove(item)            
    # Initialize the density of Hares and Puma
    H = initial_rand(land_shape,land_array)
    P = initial_rand(land_shape,land_array) 
    output_GIF(H,P,dt,T)
    print("The average value of H is",average(H))
    print("The average value of P is",average(P))
    end = time.time()
    print( "The total time taken for the simulation is", (end - start))   
    os.chdir("..")