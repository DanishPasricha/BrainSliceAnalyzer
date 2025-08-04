
🧠 **BrainSliceAnalyzer**

> *Extract. Detect. Analyze.*
> **MRI Brain Slice Processor using OpenCV & Template Matching**

---

## 🚀 Features

| 💡 Feature               | 📋 Description                                        |
| ------------------------ | ----------------------------------------------------- |
| 🎯 **Template Matching** | Detects brain regions using a reference image         |
| ✂️ **Slice Extraction**  | Crops brain regions with pixel-accurate precision     |
| 🧩 **Contour Detection** | Highlights anatomical structures using edge detection |
| 🧹 **Noise Filtering**   | Removes low-information/blank regions using erosion   |
| 📂 **Batch Processing**  | Designed for bulk image workflows from folders        |

---

## 📦 Requirements

* 🐍 Python 3.6+
* 📸 OpenCV: `pip install opencv-python`
* 🔢 NumPy: `pip install numpy`

---

## ⚙️ Usage

```python
from brain_analyzer import brainExtraction

brainExtraction(
    path_of_image="input/mri_scan.png",
    image_slice_folder_A1="output/slices",
    image_Boundaries_folder="output/contours",
    image_folder_A1="patient_001"
)
```

---

## 🧪 Parameters Explained

| 🔧 Parameter              | 📝 Description                          |
| ------------------------- | --------------------------------------- |
| `path_of_image`           | Input MRI scan path                     |
| `image_slice_folder_A1`   | Output path for cropped brain slices    |
| `image_Boundaries_folder` | Output path for contour-detected images |
| `image_folder_A1`         | Prefix used in saved output filenames   |

---

## 📁 Output Structure

```
output/
├── slices/
│   ├── patient_001_1.png
│   └── patient_001_2.png
└── contours/
    ├── patient_001_1.png
    └── patient_001_2.png
```

---

## 🛠️ Customization Tips

| 🔄 What to Change    | 💬 How                                                            |
| -------------------- | ----------------------------------------------------------------- |
| 🧠 Crop Region       | Change slicing in `[point[1]-90:point[1], point[0]:point[0]+115]` |
| 🎯 Match Accuracy    | Modify `ans >= 0.8` threshold                                     |
| 🧹 Erosion Strength  | Tune erosion kernel in `image_erosion`                            |
| 🧪 Contour Sharpness | Change Gaussian blur kernel (e.g., `(3, 3)`)                      |
