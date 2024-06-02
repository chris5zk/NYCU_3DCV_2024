import os 
import json
import shutil

# stage1 -> 8
# stage2 -> 32

z_path = './One-2-3-45/exp/'
t_path = './TransMVSNet/datasets/'
list_path = './TransMVSNet/lists/one2345'
pair_path = './TransMVSNet/datasets/pair.txt'

objs = os.listdir(z_path)
objs = sorted(objs)

os.makedirs(list_path+'_64', exist_ok=True)

f2_list = open(list_path+'_64' + '/' + 'test.txt', 'w')
print(len(objs), objs)
for scan_id, obj in enumerate(objs):
    # prepare testing list
    f2_list.write(f'scan{scan_id}\n')

    # path
    obj_path = z_path + obj
    img2_path = os.path.join(obj_path, 'stage2_8')
    
    # read pose file
    f = open(obj_path + '/' + 'pose.json')
    poses = json.load(f)
    f.close()
    
    # stage2 file generation
    output_path = os.path.join(t_path + 'one2345_64', f'scan{scan_id}')
    cam_path = os.path.join(output_path, 'cams')
    image_path = os.path.join(output_path, 'images')
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(cam_path, exist_ok=True)
    os.makedirs(image_path, exist_ok=True)
    
    shutil.copy(pair_path, output_path)
    
    p = -1
    cams2 = sorted(os.listdir(img2_path))
    for idx, cam in enumerate(cams2):
        if idx % 4 == 0:
            p += 1
        
        input_img = os.path.join(img2_path, cam)
        # copy images
        shutil.copy(input_img, image_path + '/' + f'{str(p*4+int(cam[-5])):0>8}.jpg')
        
        # camera parameters
        cam_file = cam_path + '/' + f'{str(p*4+int(cam[-5])):0>8}_cam.txt'
        with open(cam_file, 'w', encoding='utf-8') as f:
            f.write('extrinsic\n')
            for ext in poses['c2ws'][cam]:
                for e in ext:
                    f.write('{:.6f} '.format(e))
                f.write('\n')
            f.write('\n')
            
            f.write('intrinsics\n')
            for intr in poses['intrinsics']:
                for it in intr:
                    f.write('{} '.format(it))
                f.write('\n')
            f.write('\n')
            f.write('1.8 0.01\n')

f2_list.close()