# We import the DatasetLoader class from the lightly_studio module
from pathlib import Path

from lightly_studio import DatasetLoader

# Create a DatasetLoader instance
loader = DatasetLoader()

current_dir = Path(__file__).resolve().parent
loader.from_coco_instance_segmentations(
    annotations_json_path=str(current_dir / "instances_train2017.json"),
    img_dir=str(current_dir / "images"),
)

# We start the UI application on port 8001
loader.start_gui()
