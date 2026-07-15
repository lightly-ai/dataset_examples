This is a 10-video subset of [ActivityNet v1.3](http://activity-net.org/download.html)
with temporal action segments in the official ``database`` JSON format.

The subset mixes longer videos with multiple temporal labels and shorter clips. Several
activity labels intentionally appear in more than one video so filtering by category
returns multiple samples (e.g. ``Playing water polo``, ``Polishing shoes``, ``Throwing darts``).

Layout::

    activitynet_10_videos/
        videos/{video_id}.mp4
        activity_net.v1-3.min.json

Import in Lightly Studio::

    dataset.add_videos_from_path(path="dataset_examples/activitynet_10_videos/videos")
    dataset.add_annotations_from_activitynet(
        annotations_json="dataset_examples/activitynet_10_videos/activity_net.v1-3.min.json",
        annotation_source="activitynet",
    )
