# NYCU_3DCV_2024

## How to run?

1. Generate the multi-view stereo iamges from One-2-3-45.

   ``` python
   cd One-2-3-45
   # run for single image
   python run.py --half_precision --img_path <path/to/image>
   # run all images in directory
   ./demo.sh
   ```

2. Transfer the images format to DTU dataset format.

   ``` python
   cd ..
   # transfer zero123 output to DTU format, save in TransMVSNet datasets
   python z2t.py
   ```

3. Generate 3D cloud points from TransMVSNet.

   ``` python
   cd TransMVSNet
   # generate the cloud point prediction
   bash ./scripts/test_dtu.sh
   ```
