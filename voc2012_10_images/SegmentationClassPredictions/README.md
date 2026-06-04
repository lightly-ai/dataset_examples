Synthetic prediction masks for semantic-segmentation evaluation testing.

These files are derived from `../SegmentationClass` and intentionally altered:
- partial foreground removal to background (class 0),
- small spatial shifts for some masks,
- class swaps in local regions for others,
- sparse foreground pixel dropouts.

Use this folder as prediction masks while `SegmentationClass` remains ground truth.
