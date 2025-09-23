from pathlib import Path

import lightly_studio as ls

current_dir = Path(__file__).resolve().parent

# Create a DatasetLoader instance
dataset = ls.Dataset.create("coco_example")
dataset.add_samples_from_coco(
    annotations_json=str(current_dir / "instances_train2017.json"),
    images_path=str(current_dir / "images"),
    annotation_type=ls.AnnotationType.INSTANCE_SEGMENTATION,
)

# We start the UI application on the port defined with the LIGHTLY_STUDIO_PORT env variable or 8001 by default.
ls.start_gui()