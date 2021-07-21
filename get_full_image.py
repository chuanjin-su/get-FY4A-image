from satellite_image import *
import PIL.Image as Image

IMAGE_SIZE = 512

# west = 67.5
# east = 135
# south = 11.25
# north = 45

west = 56.25
east = 146.25
south = 0
north = 56.25

# resolution = 11.25
resolution = 5.625

PATH = '/home/chuanjin/workspace/satellite'

n_x = round((east-west)/resolution)
n_y = round((north-south)/resolution)

ds_data = get_data()[-1]

def get_images():
    for y in range(0,n_y):
        for x in range(0,n_x):
            bbox = str(west+resolution*x)+','+str(south+resolution*y)+','+str(west+resolution*(x+1))+','+str(south+resolution*(y+1))
            img_content = get_image(BBOX=bbox,DATE=ds_data['dataDate'], TIME=ds_data['dataTime'][0:4], ENDTIME=ds_data['endTime'])
            img_name = PATH + '/images/image_'+str(x)+'_'+str(y)+'.jpg'
            with open(img_name,'wb') as fp:
                fp.write(img_content)
            print('get images : '+str(y*n_x+x+1)+'/'+str(n_x*n_y))
    return 1

def merge_images():

    to_image = Image.new('RGB', (n_x * IMAGE_SIZE, n_y * IMAGE_SIZE))  # 创建一个新图

    for y in range(0,n_y):
        for x in range(0,n_x):
            img_name = PATH+'/images/image_'+str(x)+'_'+str(y)+'.jpg'
            from_image = Image.open(img_name).resize(
                (IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)
            to_image.paste(from_image, (x * IMAGE_SIZE, (n_y-1-y) * IMAGE_SIZE))
    
    print('Merged into -> ' + img_name)
    return to_image.save(PATH+'/'+ds_data['dataDate']+ds_data['dataTime'][0:4]+'.jpg')

if __name__=="__main__":
    get_images()
    merge_images()
