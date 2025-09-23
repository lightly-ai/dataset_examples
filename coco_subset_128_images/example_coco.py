from pathlib import Path

import lightly_studio as ls

current_dir = Path(__file__).resolve().parent

# Create a dataset and add the samples from the coco format
dataset = ls.Dataset.create("coco_example")
dataset.add_samples_from_coco(
    annotations_json=current_dir / "instances_train2017.json",
    images_path=current_dir / "images",
    annotation_type=ls.AnnotationType.INSTANCE_SEGMENTATION,
)

# Start the UI application on the port defined with the LIGHTLY_STUDIO_PORT env variable or 8001 by default.
ls.start_gui()
