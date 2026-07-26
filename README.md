# Multiview Reconstruction

A lightweight COLMAP-based toolkit for preparing image collections, running
multi-view reconstruction workflows, and inspecting generated 3D results.

[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Experimental-orange.svg)](#project-status)
[![Python](https://img.shields.io/badge/Python-3.10-informational.svg)](#requirements)

## Overview

This repository provides focused utilities for preprocessing multi-view image
collections, running reconstruction tasks with
[COLMAP](https://colmap.github.io/), and inspecting reconstructed point clouds.
Datasets and generated artifacts remain outside Git so the repository stays
compact and reusable across experiments.

## Features

- Tools for preprocessing, visualization, and handling 3D reconstruction data.
- Demo scripts to quickly run and visualize reconstruction results.

## Data

Datasets and generated reconstruction artifacts are intentionally excluded from
version control. Place local input images in a directory ignored by Git, such as
`datasets/`.

## Requirements

- COLMAP installed and accessible in your environment.
- Python 3.10 for running utility scripts.
- Standard Python libraries: `numpy`, `opencv-python`, etc.

## Usage

1. Preprocess images and organize them in the dataset folder.  
2. Use provided utility scripts for feature extraction, matching, and visualization.  
3. Run COLMAP for reconstruction following standard pipelines.

## Project Status

Experimental. The utilities are retained for reconstruction research and require
local configuration before use.

## Contact

- Website: [yixuanhuang.com](https://yixuanhuang.com)
- Email: [yixnhuang@gmail.com](mailto:yixnhuang@gmail.com)

## License

Copyright 2025 Yixuan Huang

This project is licensed under the Apache License, Version 2.0.
See the [LICENSE](LICENSE) file for details.
