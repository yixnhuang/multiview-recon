# Multiview Reconstruction

The first working version of the RGB-D capture and COLMAP reconstruction
workflow that later became [**VisRecon**](https://github.com/yixnhuang/visrecon).
It holds the working record of that stage, including three utilities that exist
only here.

[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#project-status)
[![Successor](https://img.shields.io/badge/Successor-VisRecon-4C8BF5)](https://github.com/yixnhuang/visrecon)
[![Python](https://img.shields.io/badge/Python-3.10-informational.svg)](#requirements)

## Overview

The pipeline: capture aligned RGB-D frames
from an Intel RealSense camera, mask the subject by depth and colour, run an
eight-stage COLMAP reconstruction from features through to a mesh, and inspect
the result in Open3D.

The workflow continued as [VisRecon](https://github.com/yixnhuang/visrecon).

## Repository layout

```text
.
├── utils/
│   ├── get_images.py         # RealSense capture
│   ├── new_image_geting.py   # capture + masking
│   ├── download_dataset.py   # Hugging Face subset download
│   ├── run_colmap_full.sh    # 8-stage COLMAP pipeline
│   ├── view_colmap_pcd.py    # Open3D viewer
│   ├── judge.py              # COLMAP database inspector
│   ├── point_cloud.py        # RGB-D → point cloud, OpenCV path
│   ├── pc.py                 # RGB-D → point cloud, Open3D path
│   └── try.py                # early capture script
├── demo/human/               # three screenshots from an early human-subject test
└── LICENSE
```

## Requirements

- COLMAP on `PATH`, with a CUDA build for the dense stages.
- Python 3.10, with `numpy`, `opencv-python`, `open3d`, `pyrealsense2` and
  `huggingface-hub`.

Install the packages above into a Python 3.10 environment.

## Data

Datasets and reconstruction outputs are deliberately excluded from version
control; the repository holds tools, not data. `demo/human/` is the exception —
three screenshots from an early test on a human subject, kept because they show
what the workflow produced at this stage.

## Project Status

Complete. The workflow continued as [VisRecon](https://github.com/yixnhuang/visrecon).

## License

Copyright 2025 Yixuan Huang

Licensed under the Apache License, Version 2.0 — see [LICENSE](LICENSE).

COLMAP, Open3D, librealsense and any downloaded dataset remain under their own
licenses.

## Contact

- Website: [yixuanhuang.com](https://yixuanhuang.com)
- Email: [yixnhuang@gmail.com](mailto:yixnhuang@gmail.com)
