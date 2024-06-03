# NYCU_3DCV_2024

## How to run?

1. Generate the multi-view stereo iamges from One-2-3-45. The results will save in `One-2-3-45/exp/`

   ``` python
   cd One-2-3-45
   # run for single image
   python run.py --half_precision --img_path <path/to/image>
   # run all images in directory
   ./demo.sh
   ```

2. Transfer the images format to DTU dataset format. The results will save in `TransMVSNet/datasets/one2345_64`

   ``` python
   cd ..
   # transfer zero123 output to DTU format, save in TransMVSNet datasets
   python z2t.py
   ```

3. Generate 3D cloud points from TransMVSNet. The results `.ply` file will save in `TransMVSNet/outputs/one2345_64` and the `depth maps, masks` will save in the corresponding scene directory. You can change the options in `test_dtu.sh`

   ``` python
   cd TransMVSNet
   # generate the cloud point prediction
   bash ./scripts/test_dtu.sh
   ```
