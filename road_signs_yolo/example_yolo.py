# We import the DatasetLoader class from the lightly_studio module
from pathlib import Path

from lightly_studio import DatasetLoader

# Create a DatasetLoader instance
loader = DatasetLoader()

data_yaml_path = Path(__file__).resolve().parent / "data.yaml"
loader.from_yolo(
    data_yaml_path=str(data_yaml_path),
    input_split="test",
)

# We start the UI application on port 8001
loader.start_gui()
