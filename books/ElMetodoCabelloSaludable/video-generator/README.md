# Current promotional-video generator

Everything required to reproduce the video lives in this repository. The generator does not depend on Downloads or other external directories.

From the repository root, using Python 3.12:

```powershell
python -m venv books/ElMetodoCabelloSaludable/video-generator/.venv
books/ElMetodoCabelloSaludable/video-generator/.venv/Scripts/python -m pip install -r books/ElMetodoCabelloSaludable/video-generator/requirements.txt
books/ElMetodoCabelloSaludable/video-generator/.venv/Scripts/python books/ElMetodoCabelloSaludable/video-generator/generate.py
```

Add `--preview` to validate duplicates and create the storyboard overview without rendering the final video. On Linux or macOS, use `.venv/bin/python`. FFmpeg is provided by `imageio-ffmpeg`. Windows uses Arial; Linux uses DejaVu Sans. `PROMO_FONT` and `PROMO_FONT_BOLD` may point to custom TTF files.

Generate the English promotional video on Windows with:

```powershell
books/ElMetodoCabelloSaludable/video-generator/.venv/Scripts/python books/ElMetodoCabelloSaludable/video-generator/generate_en.py
```

The English generator uses the original high-resolution English book pages, renders directly at 1920 × 1080, and creates an English neural narration with Edge TTS. Its storyboard is `storyboard-en.json` and its output is `resources/videos/ElMetodoCabelloSaludable/the-healthy-hair-method-promo-3-minutes.mp4`.

## Source files

- `storyboard.json`: Spanish on-screen titles, reference narration, and the photo/page sequence.
- `resources/images/author/video-source/`: canonical source photographs.
- `resources/images/books/ElMetodoCabelloSaludable/es/video-pages/`: Spanish book pages.
- `resources/audio/ElMetodoCabelloSaludable/narracion.m4a`: approved Spanish narration.

The validator checks paths, SHA-256 hashes, dHash visual similarity, left/right alternation, and book presence. Individual portraits embedded in the three supplied collage pages are excluded from standalone use. Illustrations and portraits printed inside other pages remain part of the original book. The generator does not duplicate portraits as blurred backgrounds. Every scene includes a book page except the approved closing scene, where Yeney holds the physical book. Half-second fades connect scenes and chapters without black frames.

## Outputs

The video is 180 seconds long and contains six 30-second chapters. Current artifacts are written to `resources/videos/`, `resources/images/books/`, and `resources/docs/`. Temporary generator output is excluded from Git.
