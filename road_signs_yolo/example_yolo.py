from pathlib import Path

import lightly_studio as ls

data_yaml_path = Path(__file__).resolve().parent / "data.yaml"

# Create a dataset and add the samples from the yolo format
dataset = ls.Dataset.create("yolo_example")
dataset.add_samples_from_yolo(
    data_yaml=data_yaml_path,
    input_split="train",
)

# Start the GUI to explore the dataset
ls.start_gui()