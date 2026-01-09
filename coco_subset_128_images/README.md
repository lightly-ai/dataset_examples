This is a subset of 128 images of the [COCO 2017 Train/Val dataset](https://cocodataset.org/#download).
It contains not only object detections, but also instance segmentations.

The predictions in `/predictions` are generated using `lightly-train` with `dinov3/convnext-tiny-ltdetr-coco`. Pseudo code:

```
import json
from PIL import Image

import lightly_train
from lightly_train._commands import predict_task_helpers

...
image_path ="path/to/image"
model = lightly_train.load_model("dinov3/convnext-tiny-ltdetr-coco")
image = Image.open(image_path).convert("RGB")
preds = model.predict(image)
entries = predict_task_helpers.prepare_coco_entries(
    predictions=preds,
    image_size=image.size,
)
# Save entries in Lightly format as json.
output_payload = {
    "file_name": image_path.name,
    "predictions": entries,
}
output_path = predictions_dir / f"{image_path.stem}.json"
with output_path.open("w", encoding="utf-8") as f:
    json.dump(output_payload, f)
```
