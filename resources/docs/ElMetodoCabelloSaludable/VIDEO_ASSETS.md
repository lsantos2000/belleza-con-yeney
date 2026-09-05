# El Método Cabello Saludable promotional-video assets

This document records the assets and validation rules for the current three-minute promotional video.

- `resources/videos/ElMetodoCabelloSaludable/`: final 1280 × 720 MP4 video.
- `resources/images/author/video-source/`: canonical author-photo archive. The current edit uses 23 standalone photographs, audited by SHA-256 and visual similarity, with no repeated files.
- `resources/audio/ElMetodoCabelloSaludable/narracion.m4a`: approved Spanish narration.
- `photo-audit.json`: provenance for selected photographs.
- `verification.json`: automated checks for the latest render.
- `resources/images/books/ElMetodoCabelloSaludable/es/storyboard.jpg`: latest storyboard overview.
- `resources/images/books/ElMetodoCabelloSaludable/es/video-pages/`: 41 distinct Spanish book pages used once in numeric order, including collage pages 17, 19, and 21.

The edit excludes the red-dress kitchen photograph, the white-corset mirror selfie, and the rejected floral portrait. Portraits embedded in supplied collage pages are not repeated as standalone images. Top headings use sentence case, and the final screen preserves the approved design. Yeney alternates between the left and right sides. Every scene contains a book page or, in the closing scene, the physical book. Half-second fades connect scenes and chapters.

The reproducible generator is in `books/ElMetodoCabelloSaludable/video-generator/`. It resolves all assets from this repository. Artwork and portraits printed within book pages remain unchanged; automated uniqueness checks apply to standalone montage photographs and selected page files.
